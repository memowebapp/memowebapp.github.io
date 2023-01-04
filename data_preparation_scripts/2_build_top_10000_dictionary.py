
import os
import json

dictionary = {}
exceptionCounter = 0
path = os.path.join(os.getcwd(), "books")
for filename in os.listdir(path):
    try:
        with open(os.path.join(path, filename), 'r') as f:
            for line in f.readlines():
                for word in line.split():
                    word = word.lower()
                    if word.isalpha():
                        if word in dictionary:
                            dictionary[word] += 1
                        else:
                            dictionary[word] = 1
    except Exception as err:
        exceptionCounter += 1
        #print(f"Unexpected {err=}, {type(err)=}")

dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

tmp = {}
counter = 0
for key in reversed(dictionary):
    tmp[key] = dictionary[key]
    counter += 1
    if counter == 10000:
        break
dictionary = tmp


with open('dictionary.txt', 'w') as f:
     f.write(json.dumps(dictionary))



    