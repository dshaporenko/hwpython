import re
import html

def clean_text(text):
    regText = re.compile('<div id="container">.*?<div class="similarity">', flags = re.DOTALL)
    res = re.search(regText, text)
    text = res.group(0)
    regTag = re.compile('<.*?>', re.DOTALL)
    regSpace = re.compile('\s{2,}', flags = re.DOTALL)
    regDiv = re.compile('<div class.*?>.*?</div>', flags = re.DOTALL)
    regTitle = re.compile('<h1 class="entry_title">.*?</h1>', flags = re.DOTALL)
    text = regTitle.sub('', text)
    text = regDiv.sub('', text)
    text = regTag.sub('', text)
    text = regSpace.sub(' ', text)
    text = html.unescape(text)
    return text
