from flask import Flask
from flask import render_template, request
app = Flask(__name__)
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()
import json, random

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer')
def answer():
    f = open('list.json', 'r', encoding = 'utf-8')
    json_string = f.read()
    f.close()
    d = json.loads(json_string)
    phrase = request.args['phrase']
    phrase = phrase.strip('.,!?')
    words = phrase.split()
    new_words = []
    new_phrase = ''
    for word in words:
        ana = morph.parse(word)
        first = ana[0]
        norm = first.normalized
        prt = str(norm.tag.POS)
        tagg = str(first.tag)
        if prt in ['NOUN', 'INFN', 'ADJF', 'NPRO', 'NUMR']:
            tg = tagg.split()
            tgs = tg[1].split(',')
            tags = set(tgs)
            tag1 = str(norm.tag)
            number = random.randint(0, len(d[prt])-1)
            an = morph.parse(d[prt][number])
            frst = an[0]
            tag2 = str(frst.tag)
            if tag2 == tag1:
                frst = frst.inflect(tags)
                new_word = frst.word
            else:
                while tag2 != tag1:
                    number = random.randint(0, len(d[prt])-1)
                    new_word = d[prt][number]
                    an = morph.parse(d[prt][number])
                    frst = an[0]
                    tag2 = str(frst.tag)
                    if tag2 == tag1:
                        frst = frst.inflect(tags)
                        new_word = frst.word
        elif prt in d:
            number = random.randint(0, len(d[prt])-1)
            new_word = d[prt][number]
        else:
            new_word = word
        new_words.append(new_word)
    for word in new_words:
        new_phrase = new_phrase + word + ' '
    new_phrase = new_phrase.capitalize()
    return render_template('answer.html', new_phrase = new_phrase, phrase = phrase)

if __name__ == '__main__':
    app.run(debug=True)




