import random
import string
import copy


def create_one_rand_string(length):
    output_string = ""

    for i in range(length):
        output_string += random.choice(alphabet)

    return output_string


def create_n_random_strings(n, length):
    all_strings = [0] * n

    for i in range(n):
        all_strings[i] = list(create_one_rand_string(length))

    return all_strings


def create_copies(n, array):
    output_array = [0] * n

    for i in range(n):
        output_array[i] = copy.deepcopy(array)

    return output_array


def mutate(array, probability, target):
    # Initalise variables
    trg = list(target)
    copies = len(array)
    length = len(target)
    success = [0] * copies

    # Selectively mutate each array
    for i in range(copies):
        for j in range(length):

            # If character matches target, continue
            if array[i][j] == trg[j]:
                success[i] += 1
                continue

            p = random.random()

            # Character mutates with probability p
            if p <= probability:
                array[i][j] = random.choice(alphabet)

    # Select best performing array for re-breeding
    max_score = max(success)
    max_index = success.index(max_score)
    array_to_evolve = array[max_index]
    # Clone target array
    new_population = create_copies(copies, array_to_evolve)

    return new_population, max_score


def evolve(probability, target, population):
    length = len(target)
    max_score = 0
    iterations = 0

    # Create random starting population
    array = create_n_random_strings(population, length)

    # Keep mutating until
    while max_score < length:
        print(array[0])
        array, max_score = mutate(array, probability, target)
        iterations += 1

    print("Success! Took " + str(iterations) + " iterations.")
    print("Target message: ")

    for i in range(length):
        print(array[0][i], end="")

    return array