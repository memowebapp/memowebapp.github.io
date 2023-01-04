import os
import json
import re

from itertools import islice
bad_words = ['fuck', 'shit', 'dick', 'ass', 'bitch', 'cunt', '  ']
third_form_verbs = [' abode ', ' arisen ', ' awoken ', ' been ', ' born ', ' beaten ', ' become ', ' begotten ', ' begun ', ' bent ', ' bet ', ' bidden ', ' bitten ', ' bled ', ' blown ', ' broken ', ' brought ', ' broadcast ', ' built ', ' burned ', ' burst ', ' bought ', ' could ', ' cast ', ' caught ', ' chidden ', ' chosen ', ' clung ', ' clothed ', ' come ', ' cost ', ' crept ', ' cut ', ' dealt ', ' dug ', ' dove ', ' done ', ' drawn ', ' dreamed ', ' drunk ', ' driven ', ' dwelled ', ' eaten ', ' fallen ', ' fed ', ' felt ', ' fought ', ' found ', ' fled ', ' flung ', ' flown ', ' forbidden ', ' forecast ', ' foreseen ', ' forgot ', ' forgiven ', ' forsaken ', ' frozen ', ' got ', ' given ', ' gone ', ' ground ', ' grown ', ' hung ', ' heard ', ' hidden ', ' hit ', ' held ', ' hurt ', ' kept ', ' kneeled ', ' known ', ' laid ', ' led ', ' leaned ', ' leaped ', ' learnt ', ' left ', ' lent ', ' let ', ' lain ', ' lighted ', ' lost ', ' made ', ' meant ', ' met ', ' mown ', ' offset ', ' overcome ', ' partaken ', ' paid ', ' pleaded ', ' preset ', ' proved ', ' put ', ' quit ', ' read ', ' relaid ', ' rent ', ' rid ', ' rung ', ' risen ', ' run ', ' sawed ', ' said ', ' seen ', ' sought ', ' sold ', ' sent ', ' set ', ' shaken ', ' shed ', ' shone ', ' shod ', ' shot ', ' shown ', ' shut ', ' sung ', ' sunken ', ' sat ', ' slain ', ' slept ', ' slid ', ' slit ', ' smelt ', ' sowed ', ' spoken ', ' sped ', ' spelt ', ' spent ', ' spilled ', ' spun ', ' spit ', ' split ', ' spoilt ', ' spread ', ' sprung ', ' stood ', ' stolen ', ' stuck ', ' stung ', ' stunk ', ' strewed ', ' struck ', ' striven ', ' sworn ', ' sweated ', ' swept ', ' swollen ', ' swum ', ' swung ', ' taken ', ' taught ', ' torn ', ' told ', ' thought ', ' thrived ', ' thrown ', ' thrust ', ' typeset ', ' undergone ', ' understood ', ' woken ', ' worn ', ' wept ', ' wetted ', ' won ', ' wound ', ' withdrawn ', ' wrung ', ' written']
second_form_verbs = ['abode ', ' arose ', ' awoke ', ' was ', ' were ', ' bore ', ' beat ', ' became ', ' begot ', ' began ', ' bent ', ' bet ', ' bade ', ' bit ', ' bled ', ' blew ', ' broke ', ' brought ', ' broadcast ', ' built ', ' burned ', ' burst ', ' bought ', ' could ', ' cast ', ' caught ', ' chode ', ' chose ', ' clung ', ' clothed ', ' came ', ' cost ', ' crept ', ' cut ', ' dealt ', ' dug ', ' dived ', ' did ', ' drew ', ' dreamed ', ' drank ', ' drove ', ' dwelt ', ' ate ', ' fell ', ' fed ', ' felt ', ' fought ', ' found ', ' fled ', ' flung ', ' flew ', ' forbade ', ' forecast ', ' foresaw ', ' forgot ', ' forgave ', ' forsook ', ' froze ', ' got ', ' gave ', ' went ', ' ground ', ' grew ', ' hung ', ' had ', ' heard ', ' hid ', ' hit ', ' held ', ' hurt ', ' kept ', ' knelled ', ' knew ', ' laid ', ' led ', ' leaned ', ' leaped ', ' learnt ', ' left ', ' lent ', ' let ', ' lay ', ' lighted ', ' lost ', ' made ', ' meant ', ' met ', ' mowed ', ' offset ', ' overcame ', ' partook ', ' paid ', ' pleaded ', ' preset ', ' proved ', ' put ', ' quit ', ' read ', ' relaid ', ' rent ', ' rid ', ' rang ', ' rose ', ' ran ', ' sawed ', ' said ', ' saw ', ' sought ', ' sold ', ' sent ', ' set ', ' shook ', ' shed ', ' shone ', ' shod ', ' shot ', ' showed ', ' shut ', ' sang ', ' sunk ', ' sat ', ' slew ', ' slept ', ' slid ', ' slit ', ' smelt ', ' sowed ', ' spoke ', ' sped ', ' spelt ', ' spent ', ' spilled ', ' spun ', ' spit ', ' split ', ' spoilt ', ' spread ', ' sprang ', ' stood ', ' stole ', ' stuck ', ' stung ', ' stank ', ' strewed ', ' struck ', ' strove ', ' swore ', ' sweated ', ' swept ', ' sweated ', ' swam ', ' swung ', ' took ', ' taught ', ' tore ', ' told ', ' thought ', ' thrived ', ' threw ', ' thrust ', ' typeset ', ' underwent ', ' understood ', ' woke ', ' wore ', ' wept ', ' wetted ', ' won ', ' wound ', ' withdrew ', ' wrung ', ' wrote']

def count_substrings(str, substrings):
    counter = 0
    for substring in substrings:
        if substring in str:
            counter += 1
    return counter

def is_one_irregular_verb_in(str):
    verbs_in_str = count_substrings(str, second_form_verbs)
    verbs_in_str += count_substrings(str, third_form_verbs)
    return verbs_in_str == 1
    

def take(n, dict):
    skip = len(dict) - n
    result = {}
    for key in dict:
        if skip > 0:
            skip -= 1
        else:
            result[key] = dict[key]
    return result

letters = re.compile('[^a-zA-Z]')

citation = {}
with open('dictionary.txt') as f:
    data = f.read()
    citation = json.loads(data)

def getScore(str, repeated, verbs, verb, form):
    score = 1000000
    wordsNumber = len(str.split())
    for bad_word in bad_words:
        if bad_word in str:
            return 0
    if not is_one_irregular_verb_in(str):
        return 0
    if (form == 3) and (verb == 'had') and ('ed ' in str):
        return 0

    unic = 0
    for word in str.split():
        word = word.lower()
        word = letters.sub('', word)
        if word not in citation:
            return 0
        if word not in repeated:
            unic += 1
            repeated.append(word)
        if word not in verbs:
            score = min(score, citation[word])
    return score*unic

def select_sentences(from_file, to_file, form):
    verbs = {}
    with open(from_file) as f:
        data = f.read()
        verbs = json.loads(data)

    verbs = dict(sorted(verbs.items(), key=lambda item: len(item[1])))
    selectedVerbs = {}
    for verb in verbs:
        sentences = verbs[verb]
        repeated = []
        verb = verb.strip()
        sentences = sorted(sentences, key=lambda line: getScore(line, repeated, verbs, verb, form))
        print(verb, " - ", len(sentences))
        selectedVerbs[verb] = sentences[-20:]

    with open(to_file, 'w') as f:
        f.write(json.dumps(selectedVerbs))

select_sentences('2ndForm_books.txt', '2ndForm_selected.txt', 2)
select_sentences('3dForm_books.txt', '3dForm_selected.txt', 3)
    
