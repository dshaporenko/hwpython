import json, os
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

@app.route('/stat')
def stats_1():
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
            if key == 'old1':
                if 'word1' not in res[lang]:
                    res[lang]['word1'] = []
                res[lang]['word1'].append(value.lower())
            elif key == 'old2':
                if 'word1' not in res[lang]:
                    res[lang]['word1'] = []
                res[lang]['word1'].append(value.lower())
            elif key == 'old3':
                if 'word2' not in res[lang]:
                    res[lang]['word2'] = []
                res[lang]['word2'].append(value.lower())
            elif key == 'old4':
                if 'word3' not in res[lang]:
                    res[lang]['word3'] = []
                res[lang]['word3'].append(value.lower())
            elif key == 'old5':
                if 'word3' not in res[lang]:
                    res[lang]['word3'] = []
                res[lang]['word3'].append(value.lower())
            elif key == 'old6':
                if 'word4' not in res[lang]:
                    res[lang]['word4'] = []
                res[lang]['word4'].append(value.lower())
            elif key == 'old7':
                if 'word5' not in res[lang]:
                    res[lang]['word5'] = []
                res[lang]['word5'].append(value.lower())
            elif key == 'old8':
                if 'word6' not in res[lang]:
                    res[lang]['word6'] = []
                res[lang]['word6'].append(value.lower())
            elif key == 'old9':
                if 'word7' not in res[lang]:
                    res[lang]['word7'] = []
                res[lang]['word7'].append(value.lower())
            elif key == 'old10':
                if 'word8' not in res[lang]:
                    res[lang]['word8'] = []
                res[lang]['word8'].append(value.lower())
            elif key == 'old11':
                if 'word5' not in res[lang]:
                    res[lang]['word5'] = []
                res[lang]['word5'].append(value.lower())
            elif key == 'old12':
                if 'word5' not in res[lang]:
                    res[lang]['word5'] = []
                res[lang]['word5'].append(value.lower())
            elif key == 'old13':
                if 'word8' not in res[lang]:
                    res[lang]['word8'] = []
                res[lang]['word8'].append(value.lower())
            elif key == 'old14':
                if 'word5' not in res[lang]:
                    res[lang]['word5'] = []
                res[lang]['word5'].append(value.lower())
            elif key == 'old15':
                if 'word10' not in res[lang]:
                    res[lang]['word10'] = []
                res[lang]['word10'].append(value.lower())
            elif key == 'old16':
                if 'word9' not in res[lang]:
                    res[lang]['word9'] = []
                res[lang]['word9'].append(value.lower())
            elif key == 'old17':
                if 'word3' not in res[lang]:
                    res[lang]['word3'] = []
                res[lang]['word3'].append(value.lower())
    for key, value in res.items():
        for key1, value1 in value.items():
            count = {}
            for value2 in value1:
                if value2 not in count:
                    count[value2] = 0
                count[value2]+=1
            statistics[key][key1] = count
    return render_template('stat.html', statistics = statistics, num = num)
        
@app.route('/json')
def json_page():
    f = open('answers.json', 'r', encoding = 'utf-8')
    answers = json.load(f)
    f.close()
    return render_template('json.html', answers = answers)  


if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
