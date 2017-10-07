from crawl import crawler, get_html
from clean import clean_text
from meta import get_meta, metadata, create_name
from folders import plain, mystem_plain, mystem_xml
import time, os

def main():
    links_list = crawler()
    for l in links_list:
        text = get_html(l)
        title, topic, author, date, month, year = get_meta(text)
        text = clean_text(text)
        path = r'C:\TomskieNovosti\plain' + os.sep + year + os.sep + month
        if not os.path.exists(path):
            os.makedirs(path)
        name = create_name(path)
        path = os.path.join(path, name)
        metadata(path, author, title, date, topic, l, year)
        plain(text, author, title, date, topic, l, path)
        time.sleep(2)
    path = r'C:\TomskieNovosti\plain'
    mystem_xml(path)
    mystem_plain(path)

if __name__ == '__main__':
    main()
