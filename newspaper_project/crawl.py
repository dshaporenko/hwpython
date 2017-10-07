import urllib.request
import re

def get_html(link):
    req = urllib.request.Request(link)
    with urllib.request.urlopen(req) as response:
        text = response.read().decode('utf-8')
    return text

def crawler():
    links_list = []
    regNextPage = re.compile('<link rel="next" href="(http://tomsk-novosti.ru/category/news/page/[0-9]+/)" />', flags = re.DOTALL)
    regPostTitle = re.compile('<h2 class="archiveTitle">.*?</h2', flags= re.DOTALL)
    regLink = re.compile('http://tomsk-novosti.ru/.*?/', flags= re.DOTALL)
    newspaper = 'http://tomsk-novosti.ru/category/news/'
    text = get_html(newspaper)
    while (len(links_list) < 1000):
        titles = regPostTitle.findall(text)
        for t in titles:
            result = re.search(regLink, t)
            link = result.group(0)
            if link not in links_list:
                links_list.append(link)
        res = re.search(regNextPage, text)
        if res:
            next_page = res.group(1)
            text = get_html(next_page)
        else:
            break
    return(links_list)
