import re
import os
import html
import json

##Папка со страницами должна лежать в папке с программой

regRow = re.compile('<tr>.*?</tr>', flags = re.DOTALL)
regThai = re.compile('<td.*?class=th>.*?</td>', flags = re.DOTALL)
regSentence = re.compile('<td class=pos>example sentence</td>', flags = re.DOTALL)
regCategory = re.compile('<td class=pos>.*?</td>', flags = re.DOTALL)
regEnglish = re.compile('<td class=pos>.*?</td></tr>', flags = re.DOTALL)
regTag = re.compile('<.*?>', re.DOTALL)
d = {}

for file in os.listdir('./thai_pages'):
    filename = 'thai_pages/' + file
    f = open(filename, 'r', encoding = 'utf-8')
    page = f.read()
    f.close()
    page = html.unescape(page)
    rows = regRow.findall(page)
    for row in rows:
        sentence = regSentence.search(row)
        if sentence:
            continue
        res = regThai.search(row)
        if res:
            thai = res.group(0)
            eng_res = regEnglish.search(row)
            eng = eng_res.group(0)
            eng = regCategory.sub('', eng)
            eng = regTag.sub('', eng)
            english = eng.split('; ')
            thai = regTag.sub('', thai)
            thai = thai.replace(u'\xa0', u'')
            d[thai] = english

f = open('thai_eng_dictionary.json', 'w', encoding = 'utf-8')
json.dump(d, f, ensure_ascii=False)
f.close()

eng_thai_d = {}
for key, value in d.items():
    for v in value:
        if v not in eng_thai_d:
            eng_thai_d[v] = []
            eng_thai_d[v].append(key)
        else:
            if key not in eng_thai_d[v]:
                eng_thai_d[v].append(key)

f = open('eng_thai_dictionary.json', 'w', encoding = 'utf-8')
json.dump(eng_thai_d, f, ensure_ascii=False)
f.close()
