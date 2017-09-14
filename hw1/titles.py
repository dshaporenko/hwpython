import urllib.request
import re

url = 'http://tomsk-novosti.ru/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

req = urllib.request.Request('http://tomsk-novosti.ru/', headers={'User-Agent':user_agent})
with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')

regPostTitle = re.compile('<h2 class="postTitle">.*?</h2>', flags= re.DOTALL)
titles = regPostTitle.findall(html)

new_titles = []
regTag = re.compile('<.*?>', re.DOTALL)
regSpace = re.compile('\s{2,}', re.DOTALL)
for t in titles:
    clean_t = regSpace.sub("", t)
    clean_t = regTag.sub("", clean_t)
    new_titles.append(clean_t)

for t in new_titles:
    t = t.replace("&#171;", "«")
    t = t.replace("&#187;", "»")
    print(t)
