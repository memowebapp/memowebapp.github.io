import os
import re
import json

second = set(('abode', 'arose', 'awoke', 'was', 'were', 'bore', 'beat', 'became', 'begot', 'began', 'bent', 'bet', 'bade', 'bit', 'bled', 'blew', 'broke', 'brought', 'broadcast', 'built', 'burned', 'burst', 'bought', 'could', 'cast', 'caught', 'chode', 'chose', 'clung', 'clothed', 'came', 'cost', 'crept', 'cut', 'dealt', 'dug', 'dived', 'did', 'drew', 'dreamed', 'drank', 'drove', 'dwelt', 'ate', 'fell', 'fed', 'felt', 'fought', 'found', 'fled', 'flung', 'flew', 'forbade', 'forecast', 'foresaw', 'forgot', 'forgave', 'forsook', 'froze', 'got', 'gave', 'went', 'ground', 'grew', 'hung', 'had', 'heard', 'hid', 'hit', 'held', 'hurt', 'kept', 'knelled', 'knew', 'laid', 'led', 'leaned', 'leaped', 'learnt', 'left', 'lent', 'let', 'lay', 'lighted', 'lost', 'made', 'meant', 'met', 'mowed', 'offset', 'overcame', 'partook', 'paid', 'pleaded', 'preset', 'proved', 'put', 'quit', 'read', 'relaid', 'rent', 'rid', 'rang', 'rose', 'ran', 'sawed', 'said', 'saw', 'sought', 'sold', 'sent', 'set', 'shook', 'shed', 'shone', 'shod', 'shot', 'showed', 'shut', 'sang', 'sunk', 'sat', 'slew', 'slept', 'slid', 'slit', 'smelt', 'sowed', 'spoke', 'sped', 'spelt', 'spent', 'spilled', 'spun', 'spit', 'split', 'spoilt', 'spread', 'sprang', 'stood', 'stole', 'stuck', 'stung', 'stank', 'strewed', 'struck', 'strove', 'swore', 'sweated', 'swept', 'swelled', 'swam', 'swung', 'took', 'taught', 'tore', 'told', 'thought', 'thrived', 'threw', 'thrust', 'typeset', 'underwent', 'understood', 'woke', 'wore', 'wept', 'wetted', 'won', 'wound', 'withdrew', 'wrung', 'wrote'))
third = set(('abode', 'arisen', 'awoken', 'been', 'born', 'beaten', 'become', 'begotten', 'begun', 'bent', 'bet', 'bidden', 'bitten', 'bled', 'blown', 'broken', 'brought', 'broadcast', 'built', 'burned', 'burst', 'bought', 'could', 'cast', 'caught', 'chidden', 'chosen', 'clung', 'clothed', 'come', 'cost', 'crept', 'cut', 'dealt', 'dug', 'dove', 'done', 'drawn', 'dreamed', 'drunk', 'driven', 'dwelled', 'eaten', 'fallen', 'fed', 'felt', 'fought', 'found', 'fled', 'flung', 'flown', 'forbidden', 'forecast', 'foreseen', 'forgot', 'forgiven', 'forsaken', 'frozen', 'got', 'given', 'gone', 'ground', 'grown', 'hung', 'had', 'heard', 'hidden', 'hit', 'held', 'hurt', 'kept', 'kneeled', 'known', 'laid', 'led', 'leaned', 'leaped', 'learnt', 'left', 'lent', 'let', 'lain', 'lighted', 'lost', 'made', 'meant', 'met', 'mown', 'offset', 'overcome', 'partaken', 'paid', 'pleaded', 'preset', 'proved', 'put', 'quit', 'read', 'relaid', 'rent', 'rid', 'rung', 'risen', 'run', 'sawed', 'said', 'seen', 'sought', 'sold', 'sent', 'set', 'shaken', 'shed', 'shone', 'shod', 'shot', 'shown', 'shut', 'sung', 'sunken', 'sat', 'slain', 'slept', 'slid', 'slit', 'smelt', 'sowed', 'spoken', 'sped', 'spelt', 'spent', 'spilled', 'spun', 'spit', 'split', 'spoilt', 'spread', 'sprung', 'stood', 'stolen', 'stuck', 'stung', 'stunk', 'strewed', 'struck', 'striven', 'sworn', 'sweated', 'swept', 'swollen', 'swum', 'swung', 'taken', 'taught', 'torn', 'told', 'thought', 'thrived', 'thrown', 'thrust', 'typeset', 'undergone', 'understood', 'woken', 'worn', 'wept', 'wetted', 'won', 'wound', 'withdrawn', 'wrung', 'written'))
all_verbs = {}

patterns = []
for verb in third:
    patterns.append((re.compile(".* have .* " + verb + " .*"), verb))
    patterns.append((re.compile(".* has .* " + verb + " .*"), verb))

def pariciplePast(str):
    for pattern, verb in patterns:
        if pattern.match(str):
            return (True, verb)
    return (False, "")

def simlpePast(str):
    if 'has' not in str and 'have' not in str and "'s" not in str and "'ve" not in str: 
        for word in str.split():
            if word in second:
                return (True, word)
    return (False, "")

def irregular_verb_in(str):
    for word in str.split():
        if word in all_verbs:
            all_verbs[word] += 1
            return True
    return False

path = os.path.join(os.getcwd(), "books")
exceptionCounter = 0
second_sentences = {}
for verb in second:
    second_sentences[verb] = set()
    all_verbs[verb] = 0

third_sentences = {}
for verb in third:
    third_sentences[verb] = set()
    all_verbs[verb] = 0

for filename in os.listdir(path):
    try:
        with open(os.path.join(path, filename), 'r') as f:
            data = f.read().replace('\n', ' ')
            sentences = re.findall(r"[A-Z]{1}[A-Za-z,'\s]*[\.!?]{1}", data)
            for sentence in sentences:
                sentenceLower = sentence.lower()
                wordsNumber = len(sentence.split())
                if wordsNumber > 4 and wordsNumber < 11 and irregular_verb_in(sentenceLower):
                    isThird, verb = pariciplePast(sentenceLower)
                    if isThird:
                        third_sentences[verb].add(sentence)
                    else:
                        isSecond, verb = simlpePast(sentenceLower)
                        if isSecond:
                            second_sentences[verb].add(sentence)
            print(filename)
    except Exception as err:
        exceptionCounter += 1

all_verbs = dict(sorted(all_verbs.items(), key=lambda item: item[1]))
for verb in all_verbs:
    print(verb, " - ", all_verbs[verb])

second_sentences = dict(sorted(second_sentences.items(), key=lambda item: len(item[1])))
for verb in second_sentences:
    second_sentences[verb] = list(second_sentences[verb])
    #print(verb, ' - ', len(second_sentences[verb]))
print("Exception counter: ", exceptionCounter)
with open('2ndForm_books.txt', 'w') as f:
     f.write(json.dumps(second_sentences))

third_sentences = dict(sorted(third_sentences.items(), key=lambda item: len(item[1])))
for verb in third_sentences:
    third_sentences[verb] = list(third_sentences[verb])
    #print(verb, ' - ', len(third_sentences[verb]))
print("Exception counter: ", exceptionCounter)
with open('3dForm_books.txt', 'w') as f:
     f.write(json.dumps(third_sentences))