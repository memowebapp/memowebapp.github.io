import os
import json
import re

second_to_first_map = {}
third_to_first_map = {}
first_max_citations = {}
first_min_citations = {}
second_citations = {}
third_citations = {}
all_verbs_list = []

verbs_table = {}

with open(os.path.join(os.getcwd(), "verbs_table.txt"), 'r') as f:
    for line in f.readlines():
        words = line.split()
        if len(words) == 3:
            second_to_first_map[words[1]] = words[0]
            third_to_first_map[words[2]] = words[0]
        elif len(words) == 4:
            second_to_first_map[words[1]] = words[0]
            second_to_first_map[words[2]] = words[0]
            third_to_first_map[words[3]] = words[0]


with open('2ndForm_books.txt') as f:
    dictionary = json.loads(f.read())
    for key in dictionary:
        key = key.strip()
        firstForm = second_to_first_map[key]
        examplesNum = len(dictionary[key])
        first_max_citations[firstForm] = examplesNum
        first_min_citations[firstForm] = examplesNum
        second_citations[key] = examplesNum


with open('3dForm_books.txt') as f:
    dictionary = json.loads(f.read())
    for key in dictionary:
        key = key.strip()
        firstForm = third_to_first_map[key]
        examplesNum = len(dictionary[key])
        first_max_citations[firstForm] = max(examplesNum, first_max_citations[firstForm])
        first_min_citations[firstForm] = min(examplesNum, first_min_citations[firstForm])
        third_citations[key] = examplesNum

with open(os.path.join(os.getcwd(), "verbs_table.txt"), 'r') as f:
    for line in f.readlines():
        words = line.split()
        if first_min_citations[words[0]] > 5:
            if len(words) == 3:
                verbs_table[words[0]] = {"second" : [words[1]], "third" : [words[2]]}
                all_verbs_list.append((words[1], words[0], 'second', second_citations[words[1]]))
                all_verbs_list.append((words[2], words[0], 'third', third_citations[words[2]]))
            elif len(words) == 4:
                verbs_table[words[0]] = {"second" : [words[1], words[2]], "third" : [words[3]]}
                all_verbs_list.append((words[1], words[0], 'second', second_citations[words[1]]))
                all_verbs_list.append((words[2], words[0], 'second', second_citations[words[2]]))
                all_verbs_list.append((words[3], words[0], 'third', third_citations[words[3]]))

second_to_first_map = dict(sorted(second_to_first_map.items(), key=lambda item: first_max_citations[item[1]], reverse=True))
third_to_first_map = dict(sorted(third_to_first_map.items(), key=lambda item: first_max_citations[item[1]], reverse=True))
verbs_table = dict(sorted(verbs_table.items(), key=lambda item: first_max_citations[item[0]], reverse=True))
all_verbs_list = sorted(all_verbs_list, key=lambda item: item[3], reverse=True)
print("verbs table len: ", len(verbs_table))

def getSentences(file):
    result = {}
    with open(file) as f:
        dictionary = json.loads(f.read())
        for key in dictionary:
            result[key] = []
            for sentence in dictionary[key]:
                sentence = ' '.join(sentence.split())
                result[key].append(sentence)
    return result

def getSynonyms():
    result = {}
    with open("irregular_verbs.txt") as f:
        data = f.read()
        verbs = re.findall(r"[a-z]* / [a-z]*", data)
        for verb in verbs:
            synonyms = verb.split(" / ")
            result[synonyms[0]] = synonyms[1]
    return result


with open('verbs_list.js', 'w') as f:
     f.write("const second_form = " + json.dumps(second_to_first_map))
     f.write("\n")
     f.write("const third_form = " + json.dumps(third_to_first_map))
     f.write("\n")
     f.write("const verbs_table = " + json.dumps(verbs_table))
     f.write("\n")
     f.write("const all_verbs_list = " + json.dumps(all_verbs_list))
     f.write("\n")
     f.write("const second_sentences = " + json.dumps(getSentences("2ndForm_selected.txt")))
     f.write("\n")
     f.write("const third_sentences = " + json.dumps(getSentences("3dForm_selected.txt")))
     f.write("\n")
     f.write("const synonyms = " + json.dumps(getSynonyms()))
