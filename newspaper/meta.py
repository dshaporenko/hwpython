import re
import html

def get_meta(text):
    regTitle = re.compile('<h1 class="entry_title">.*?</h1>', flags= re.DOTALL)
    regTag = re.compile('<.*?>', re.DOTALL)
    regSpace = re.compile('\s{2,}', re.DOTALL)
    regTopic = re.compile('<span class="tLabel"></span>.*?</a>', flags = re.DOTALL)
    regAuthor = re.compile('<span class="postAuthor">.*?</span>', flags = re.DOTALL)
    regDate = re.compile('<span class="date">.*?</span>', flags = re.DOTALL)
    res = re.search(regTitle, text)
    if res:
        title = res.group(0)
        title = regTag.sub("", title)
        title = html.unescape(title)
    else:
        title = 'no title'
    res = re.search(regTopic, text)
    if res:
        topic = res.group(0)
        topic = regSpace.sub("", topic)
        topic = regTag.sub("", topic)
    else:
        topic = 'no topic'
    res = re.search(regAuthor, text)
    if res:
        author = res.group(0)
        author = regTag.sub("", author)
    else:
        author = 'Noname'
    res = re.search(regDate, text)
    if res:
        date = res.group(0)
        date = regTag.sub("", date)
        d = date.split('.', 2)
        month = d[1]
        if month[0] == '0':
            month = month[1]
        year = d[2]
    else:
        date = "unknown"
        month = "unknown"
        year = "unknown"
    return title, topic, author, date, month, year

def create_name(link):
    regName = re.compile('([0-9A-Za-z-]+)/$', flags = re.DOTALL)
    res = re.search(regName, link)
    name = res.group(1) + '.txt'
    return name
