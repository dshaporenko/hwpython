import urllib.request, re, json
from pymystem3 import Mystem

def change_orthography(text):
    f = open('dictionary.json', 'r', encoding = 'utf-8')
    d = json.load(f)
    f.close()
    m = Mystem()
    new_text = []
    for t in text:
        new_words = []
        an = m.analyze(t)
        for i, a in enumerate(an):
            word = a['text']
            if 'analysis' not in a:
                new_word = word
            else:
                if a['analysis'] != []:
                    lemma = a['analysis'][0]['lex']
                    if lemma in d:
                        if d[lemma] == lemma:
                            new_word = word
                        else:
                            new_word = word
                            if 'ѣ' in d[lemma]:
                                for ind, let in enumerate(d[lemma]):
                                    if let == 'ѣ' and ind < len(word):
                                        new_word = word[:ind] + d[lemma][ind] + word[ind+1:]
                            if 'ѳ' in d[lemma]:
                                for ind, let in enumerate(d[lemma]):
                                    if let == 'ѳ' and ind < len(word):
                                        new_word = word[:ind] + d[lemma][ind] + word[ind+1:]
                            if 'ѵ' in d[lemma]:
                                for ind, let in enumerate(d[lemma]):
                                    if let == 'ѵ' and ind < len(word):
                                        new_word = word[:ind] + d[lemma][ind] + word[ind+1:]
                            if 'Ѳ' in d[lemma]:
                                for ind, let in enumerate(d[lemma]):
                                    if let == 'Ѳ' and ind < len(word):
                                        new_word = word[:ind] + d[lemma][ind] + word[ind+1:]
                    else:
                        new_word = word
                else:
                    new_word = word
            if new_word.lower()[len(new_word)-1] in 'бвгджзклмнпрстфхцчшщ':
                new_word = new_word + 'ъ'
            if'analysis' in a:
                if a['analysis'] != []:
                    for ind in range(len(new_word)-1):
                        if ((word.lower()[ind] == 'и' or word.lower()[ind] == 'й') and (word.lower()[ind+1] in 'ауеыюоэияёѣй')):
                            new_word = new_word[:ind] + 'і' + new_word[ind+1:]
                            if word[0].isupper():
                                new_word = new_word.title()
                    gr = a['analysis'][0]['gr']
                    if 'S' in gr:
                        if 'дат,ед' in gr or 'пр,ед' in gr:
                            new_word = new_word[:len(new_word)-1] + 'ѣ'
                    if 'A' in gr:
                        if new_word.endswith('іе') or new_word.endswith('ые'):
                            b = an[i+2]
                            if 'S' in b['analysis'][0]['gr']:
                                if 'сред' in b['analysis'][0]['gr'] or 'жен' in b['analysis'][0]['gr']:
                                    new_word = new_word[:len(new_word)-1] + 'я'
            if new_word.startswith('бес'):
                new_word = new_word[:2] + 'з' + new_word[3:]
            if new_word.startswith('черес'):
                new_word = new_word[:2] + 'з' + new_word[3:]
            if new_word.startswith('чрес'):
                new_word = new_word[:2] + 'з' + new_word[3:]
            new_words.append(new_word)
        txt = ''
        for word in new_words:
            txt = txt + word
        new_text.append(txt)
    return(new_text)

