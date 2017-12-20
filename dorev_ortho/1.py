import json, urllib.request, re
from pymystem3 import Mystem
from flask import Flask, url_for, render_template, request
import orthography
from weather import weather  
    
app = Flask(__name__)

@app.route('/')
def index():
    weather_skopje = weather()
    return render_template('index.html', weather_skopje = weather_skopje)

@app.route('/answer')
def answerss():
    word = request.args['word']
    new_word = ''
    f = open('dictionary.json', 'r', encoding = 'utf-8')
    d = json.load(f)
    f.close()
    if word in d:
        new_word = d[word]
    return render_template('answer.html', word = word, new_word = new_word)

@app.route('/ortho')
def ortho():
    return render_template('ortho.html')

@app.route('/ortho_answer')
def ortho_answer():
    link = request.args['link']
    req = urllib.request.Request(link)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    regP = re.compile('<p>.*?</p>', re.DOTALL)
    regTag = re.compile('<.*?>', re.DOTALL)
    regSpace = re.compile('\s{2,}', re.DOTALL)
    text = regP.findall(html)
    new_text = []
    for t in text:
        clean_t = regTag.sub('',t)
        clean_t = regSpace.sub(' ', clean_t)
        clean_t = re.sub('-', ' ', clean_t)
        new_text.append(clean_t)
    f = open('text.txt', 'w', encoding = 'utf-8')
    text_list = orthography.change_orthography(new_text)
    for t in text_list:
        f.write(t)
    f.close()
    return render_template('ortho_answer.html')

@app.route('/yat_test')
def test():
    return render_template('yat_test.html')

@app.route('/test_result')
def test_result():
    res = request.args
    count = 0
    for key, val in res.items():
        if val == 'correct':
            count += 1
    return render_template('test_result.html', count = count)

if __name__ == '__main__':
    app.run(debug=True)
