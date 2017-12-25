from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    f = open('eng_thai_dictionary.json', 'r', encoding = 'utf-8')
    d = json.load(f)
    f.close()
    word = request.args['word']
    if word in d:
        res = d[word]
    else:
        res = []
    return render_template('result.html', word = word, res = res)

if __name__ == '__main__':
    app.run(debug=True)
