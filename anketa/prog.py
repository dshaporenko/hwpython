import json, os, sqlite3
from flask import Flask
from flask import url_for, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answers')
def answerss():
    if os.path.exists('answers.json'):
        f = open('answers.json', 'r', encoding = 'utf-8')
        answ = json.load(f)
        f.close()
    else:
        answ = []
    answ.append(request.args)
    f = open('answers.json', 'w', encoding = 'utf-8')
    json.dump(answ, f, ensure_ascii=False)
    f.close()
    return render_template('answers.html')

@app.route('/stats')
def stats1():
    res = {}
    statistics = {}
    f = open('answers.json', 'r', encoding = 'utf-8')
    answers = json.load(f)
    f.close()
    num = len(answers)
    for answer in answers:
        for key, value in answer.items():
            if key == 'language':
                if value not in res:
                    res[value] = {}
    for key in res:
        statistics[key] = {}
    for answer in answers:
        lang = answer['language']
        for key, value in answer.items():
            if key == 'color1':
                if 'black' not in res[lang]:
                    res[lang]['black'] = []
                res[lang]['black'].append(value.lower())
            elif key == 'color2':
                if 'white' not in res[lang]:
                    res[lang]['white'] = []
                res[lang]['white'].append(value.lower())
            elif key == 'color3':
                if 'red' not in res[lang]:
                    res[lang]['red'] = []
                res[lang]['red'].append(value.lower())
            elif key == 'color4':
                if 'blue' not in res[lang]:
                    res[lang]['blue'] = []
                res[lang]['blue'].append(value.lower())
            elif key == 'color5':
                if 'green' not in res[lang]:
                    res[lang]['green'] = []
                res[lang]['green'].append(value.lower())
            elif key == 'color6':
                if 'yellow' not in res[lang]:
                    res[lang]['yellow'] = []
                res[lang]['yellow'].append(value.lower())
            elif key == 'color7':
                if 'purple' not in res[lang]:
                    res[lang]['purple'] = []
                res[lang]['purple'].append(value.lower())
            elif key == 'color8':
                if 'pink' not in res[lang]:
                    res[lang]['pink'] = []
                res[lang]['pink'].append(value.lower())
    for key, value in res.items():
        for key1, value1 in value.items():
            count = {}
            for value2 in value1:
                if value2 not in count:
                    count[value2] = 0
                count[value2]+=1
            statistics[key][key1] = count
    return render_template('stats.html', statistics = statistics, num = num)
        
@app.route('/json')
def json_page():
    f = open('answers.json', 'r', encoding = 'utf-8')
    answers = json.load(f)
    f.close()
    return render_template('json.html', answers = answers)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/result')
def result_word():
    word = request.args['query'].lower()
    colors = {}
    colors1 = {}
    check = 0
    f = open('answers.json', 'r', encoding = 'utf-8')
    answers = json.load(f)
    out = {}
    f.close()
    for answer in answers:
        for key, value in answer.items():
            if value == word:
                if key not in colors:
                    colors[key] = []
                if answer['language'] not in colors[key]:
                    colors[key].append(answer['language'])
    if colors != {}:
        check = 1
        for color in colors:
            out = {}
            for answer in answers:
                lang = answer['language']
                if lang not in out:
                    out[lang] = []
                if answer[color] not in out[lang]:
                    out[lang].append(answer[color])
            colors1[color] = out
    return render_template('result.html', colors1 = colors1, word = word, colors = colors, check = check)    


if __name__ == '__main__':
    app.run(debug=True)
