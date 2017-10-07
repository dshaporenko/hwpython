from crawl import crawler
from clean import clean_text
from meta import get_meta, create_name
import folders, time, re, os, urllib.request, html

def main():
    links_list = crawler()
    for l in links_list:
        req = urllib.request.Request(l)
        with urllib.request.urlopen(req) as response:
            text = response.read().decode('utf-8')
        name = create_name(l)
        title, topic, author, date, month, year = get_meta(text)
        text = clean_text(text)
        path = r'C:\Tomskie_Novosti\plain' + os.sep + year + os.sep + month
        if not os.path.exists(path):
            os.makedirs(path)
        folders.metadata(path, author, title, date, topic, l, year, name)
        folders.plain(text, author, title, date, topic, l, path, name)
        time.sleep(2)
    path = r'C:\Tomskie_Novosti\plain'
    folders.mystem_xml(path)
    folders.mystem_plain(path)

        
main()
