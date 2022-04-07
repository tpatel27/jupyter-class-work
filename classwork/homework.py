import string

file = open("Macbeth.txt", "r")
dictionary = dict()

for single_line in file:
    single_line = single_line.strip()
    single_line = single_line.replace("“", "")
    single_line = single_line.replace("”", "")
    single_line = single_line.lower().translate(single_line.maketrans("", "", string.punctuation.replace("'", "")))
    words = single_line.split()
    for word in words:
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1

print("Word count are as follows:\n")

for key in list(dictionary.keys()):
    print(key, ":", dictionary[key])
