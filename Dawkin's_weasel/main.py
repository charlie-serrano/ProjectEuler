from dawkins_weasel import *
import timeit
import string

def main():
    # Set variables
    alphabet = list(string.ascii_uppercase + " ")
    target_string = 'METHINKS IT IS LIKE A WEASEL'
    probability = 0.05
    population = 100

    # Run evolution
    x = evolve(probability, target_string, population)


print(timeit.timeit(main(), 1))
