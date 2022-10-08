import permutation
import random
import math


class SimulatedAnnealing:

    def __init__(self,  initial_temperature, threshold, cooling_rate):
        self.initial_temperature = initial_temperature
        self.threshold = threshold
        self.cooling_rate = cooling_rate

    def run(self, hypothesis, encrypted_message, lan_model):
        H = hypothesis
        T = self.initial_temperature
        while T > self.threshold:
            H_ = permutation.Permutation(H.get_neighbor())
            delta = H_.get_energy(encrypted_message, lan_model) - H.get_energy(encrypted_message, lan_model)
            if delta < 0:
                p = 1
            else:
                p = math.exp(-delta/T)
            rnd = random.random()
            if rnd < p:
                H = H_
            T = T*self.cooling_rate
        return H
