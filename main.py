import language_model
import permutation
import simulated_annealing
import random
import math
import urllib
import urllib.request

def main():

    corpus = language_model.CorpusReader("https://www.gutenberg.org/files/76/76-0.txt")
    lan_model = language_model.LanguageModel(corpus)
    file = open("problemset_07_encrypted_input.txt", "r")
    encrypted_message = file.read()
    file.close()
    mapping = create_simple_mapping()
    imitial_perm = permutation.Permutation(mapping)
    init_temp = 1000
    threshold = 0.00001
    cool_rate = 0.9995
    wining = simulated_annealing.SimulatedAnnealing(init_temp,threshold,cool_rate).run(imitial_perm,encrypted_message,lan_model)

    print("The initial temperature, threshold and cooling rate used: ",init_temp,",",threshold,",",cool_rate)
    print("The winning permutation: ")
    print(wining.mapping)
    print("The content of the deciphered message is: ")
    print(wining.translate(encrypted_message))


def create_simple_mapping():
    mapping = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    sigma = [',', '.', ':', '\n', '#', '(', ')', '!', '?', '\'', '\"', " "]
    for char in alpha:
        mapping[char] = char
    for char in sigma:
        mapping[char] = char
    return mapping

main()


