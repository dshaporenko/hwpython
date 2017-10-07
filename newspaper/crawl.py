import urllib.request
import re

def crawler():
    links_list = []
    regNextPage = re.compile('<link rel="next" href="(http://tomsk-novosti.ru/category/news/page/[0-9]+/)" />', flags = re.DOTALL)
    regPostTitle = re.compile('<h2 class="archiveTitle">.*?</h2', flags= re.DOTALL)
    regLink = re.compile('http://tomsk-novosti.ru/.*?/', flags= re.DOTALL)
    newspaper = 'http://tomsk-novosti.ru/category/news/'
    req = urllib.request.Request(newspaper)
    with urllib.request.urlopen(req) as response:
        text = response.read().decode('utf-8')
    while (len(links_list) < 1500):
        titles = regPostTitle.findall(text)
        for t in titles:
            result = re.search(regLink, t)
            link = result.group(0)
            if link not in links_list:
                links_list.append(link)
        res = re.search(regNextPage, text)
        if res:
            next_page = res.group(1)
            req = urllib.request.Request(next_page)
            with urllib.request.urlopen(req) as response:
                text = response.read().decode('utf-8')
        else:
            break
    return(links_list)
