import re
import html

def clean_text(text):
    regText = re.compile('<div id="container">.*?<div class="similarity">', flags = re.DOTALL)
    regTopic = re.compile('<span class="tLabel"></span>.*?</a>', flags = re.DOTALL)
    regAuthor = re.compile('<div>\s*<span class="postAuthor">.*?</div>', flags = re.DOTALL)
    regDate = re.compile('<span class="date">.*?</span>', flags = re.DOTALL)
    regTag = re.compile('<.*?>', re.DOTALL)
    regSpace = re.compile('\s{2,}', flags = re.DOTALL)
    regTitle = re.compile('<h1 class="entry_title">.*?</h1>', flags = re.DOTALL)
    regComment = re.compile('<!--.*?-->', flags = re.DOTALL)
    res = re.search(regText, text)
    if res:
        text = res.group(0)
    else:
        res = re.search(regText, text)
        text = res.group(0)      
    text = regTitle.sub('', text)
    text = regTopic.sub('', text)
    text = regAuthor.sub('', text)
    text = regDate.sub('', text)
    text = regComment.sub('', text)
    text = regTag.sub('', text)
    text = regSpace.sub('', text)
    text = html.unescape(text)
    return text
