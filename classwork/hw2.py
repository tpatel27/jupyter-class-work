import re
from string import punctuation


readfile = open('Macbeth.txt', "r")
content_file = readfile.read()
type(punctuation)
my_punctuation = punctuation.replace("'" ,"")

for c in content_file:
    if c in my_punctuation:
        content_file = content_file.replace(c, " ")
content = content_file.lower()
words = content_file.split()
dictionary_file = {}
for word in words:
    dictionary_file[word] = dictionary_file.get(word,0) + 1
print(dictionary_file)
readfile.close()