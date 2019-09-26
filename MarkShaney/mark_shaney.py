import re
import random


def extract_text(filename):
    with open(filename, "r") as file:
        sample_text = file.read()
        sample_text = sample_text.replace("\n", "\n ")
        word_array = re.split("[ ]", sample_text)
        return word_array


def create_triples_dictionary(array):
    triples_dictionary = {}

    for i in range(len(array) - 2):
        w1 = array[i]
        w2 = array[i+1]
        w3 = array[i+2]

        if w1 not in triples_dictionary:
            triples_dictionary[w1] = [(w2, w3)]
        elif w1 in triples_dictionary and (w2, w3) in triples_dictionary[w1]:
            continue
        else:
            triples_dictionary[w1].append((w2, w3))

    return triples_dictionary


def mark_shaney(dictionary, text_length):
    text =[random.choice(list(dictionary.keys()))]

    for i in range(text_length -1):
        search_word = text[-1]
        return_words = random.choice(dictionary[search_word])
        word2 = return_words[0]
        word3 = return_words[1]

        text.extend([word2, word3])

        output_text = ""

        for i in text:
            if i[-1] == "\n":
                output_text += i
            else:
                output_text += i + " "

    return output_text


#### Tests ###
training_text_file ="all_tswift_lyrics.txt"
training_text = extract_text(training_text_file)
text_dictionary = create_triples_dictionary(training_text)
text_length = 50

mark_shaney_text = mark_shaney(text_dictionary, text_length)
print(mark_shaney_text)

# b= "hello\nHow\nare\nyou"
# b= b.replace("\n", "\n ")
# c = b.split(" ")
# print(b)
# print(c)