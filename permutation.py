import random
import math

class Permutation:

    def __init__(self, mapping):
        self.mapping = mapping

    def get_neighbor(self):
        new_mapping = self.mapping.copy()
        char1 = (random.choice(list(new_mapping.keys())))
        char2 = char1
        while char2==char1:
            char2 = (random.choice(list(new_mapping.keys())))
        temp = new_mapping[char1]
        new_mapping[char1] = new_mapping[char2]
        new_mapping[char2] = temp
        return new_mapping

    def translate(self, str):
        str_tran = ""
        for char in str:
            str_tran = str_tran + self.mapping[char]
        return str_tran

    def get_energy(self, str, lan_model):
        translation = self.translate(str)
        energy = -math.log2(lan_model.unigramProb[translation[0]])
        for i in range(1,len(translation)):
            energy -= math.log2(lan_model.bigramProb[(translation[i-1],translation[i])])
        return energy



