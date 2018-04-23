import urllib.request
import json
import os
import re
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib import style
style.use('ggplot')

def vk(link):
    req = urllib.request.Request(link)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
    return data

def get_posts():
    posts = []
    texts = []
    authors = []
    lengths = []
    while len(posts) < 200:
        link = 'https://api.vk.com/method/wall.get?owner_id=-35595350&count=100&v=5.74&access_token=8423c2448423c2448423c244d08441f2a1884238423c244dee1644d9e90529494134bf8&offset=' + str(len(posts))
        data = vk(link)
        for item in data['response']['items']:
            posts.append(item)
    for post in posts:
        texts.append(post['text'])
        if 'signer_id' in post.keys():
            authors.append(post['signer_id'])
        else:
            authors.append('None')
    for text in texts:
        lengths.append(len(text.split()))
    for i, text in enumerate(texts):
        f_name = 'post' + str(i)
        if not os.path.exists(f_name):
            os.mkdir(f_name)
        name = os.path.join(f_name, 'text.txt')
        f = open(name, 'w', encoding = 'utf-8')
        f.write(text + '\n')
        f.close()
    return posts, texts, authors, lengths

def get_comments(posts):
    comments = []
    comments_per_post = []
    texts = []
    authors = []
    lengths = []

    for post in posts:
        while len(comments_per_post)< post['comments']['count'] and len(comments_per_post) < 200:
            link = 'https://api.vk.com/method/wall.getComments?owner_id=-35595350&post_id=' + str(post['id']) + '&count=100&v=5.74&access_token=8423c2448423c2448423c244d08441f2a1884238423c244dee1644d9e90529494134bf8&offset=' + str(len(comments_per_post))
            data = vk(link)
            for item in data['response']['items']:
                comments_per_post.append(item)
            for comment in comments_per_post:
                authors.append(comment['from_id'])
                lengths.append(len(comment['text'].split()))
        comments.append(comments_per_post)
        comments_per_post = []

    for comment in comments:
        c_texts = []
        for c in comment:
            c_texts.append(c['text'])
        texts.append(c_texts)

    for i, text in enumerate(texts):
        for index, t in enumerate(text):
            name = 'post' + str(i) + '/' + 'comment' + str(index) + '.txt'
            f = open(name, 'w', encoding='utf-8')
            f.write(t + '\n')
            f.close()
    return authors, lengths, texts

def length(p_texts, c_texts):
    d = {}
    d1 = {}

    for i, text in enumerate(p_texts):
        d[len(text.split())] = [0, 0]
        
    for i, text in enumerate(p_texts):
        l = 0
        n = 0
        for c in c_texts[i]:
            l += len(c.split())
        n = len(c_texts[i])
        d[len(text.split())][0] += l
        d[len(text.split())][1] += n

    for key, value in d.items():
        if value[1] != 0:
            d1[key] = value[0]/value[1]
        else:
            d1[key] = 0

    for key, value in sorted(d1.items()):
        p_len.append(key)
        c_len.append(value)
    return p_len, c_len

def graph_lengths(p_len, c_len):
    plt.plot(p_len, c_len)
    plt.title("Связь средней длины комментария с длиной поста")
    plt.xlabel("Длина поста")
    plt.ylabel("Средняя длина комментария")
    plt.savefig('graph1.png')
    plt.show()

def get_age(authors, lengths):
    ids = []
    lens = []
    for i, author in enumerate(authors):
        if author != 'None':
            if author > 0:  #паблики тоже могут комментить
                ids.append(author)
                lens.append(lengths[i])
    bdates = []
    ages = []
    reDate = re.compile('([0-9]+)\.([0-9]+)\.([0-9]+)')

    for user in ids:
        link = 'https://api.vk.com/method/users.get?v=5.74&user_ids={}&fields=bdate'.format(str(user))
        data = vk(link)
        for i in data['response']:
            if 'bdate' in i:
                bdates.append(i['bdate'])
            else:
                bdates.append('None')
    for date in bdates:
        res = re.search(reDate, date)
        if res:
            if (int(res.group(1)) < 24 and int(res.group(2)) == 4) or (int(res.group(2)) < 4):
                ages.append(2018 - int(res.group(3)))
            else:
                ages.append(2018 - int(res.group(3)) - 1)
        else:
            ages.append('None')
    new_ages = []
    new_lens = []
    for i, age in enumerate(ages):
        if age != 'None':
            new_ages.append(age)
            new_lens.append(lens[i])
    ages_freq = Counter(new_ages)
    dict_ages = {}

    for i, age in enumerate(new_ages):
        if age in dict_ages:
            dict_ages[age] += new_lens[i]
        else:
            dict_ages[age] = new_lens[i]

    for age in dict_ages.keys():
        dict_ages[age] = dict_ages[age] / ages_freq[age]
    return dict_ages

def get_city(authors, lengths):
    users = []
    lens = []
    for i, author in enumerate(authors):
        if author != 'None':
            if author > 0:  #паблики тоже могут комментить
                users.append(author)
                lens.append(lengths[i])
    cities = []
    new_cities = []
    new_lens = []
    for user in users:
        link = 'https://api.vk.com/method/users.get?v=5.74&user_ids={}&fields=city'.format(str(user))
        data = vk(link)
        for i in data['response']:
            if 'city' in i:
                cities.append(i['city']['title'])
            else:
                cities.append('None')
    for i, city in enumerate(cities):
        if city != 'None':
            new_cities.append(city)
            new_lens.append(lens[i])
    cities_freq = Counter(new_cities)
    dict_cities = {}

    for i, city in enumerate(new_cities):
        if city in dict_cities:
            dict_cities[city] += new_lens[i]
        else:
            dict_cities[city] = new_lens[i]

    for city in dict_cities.keys():
        dict_cities[city] = dict_cities[city] / cities_freq[city]
    return dict_cities

def graph_age(dict_ages, s, name):
    ages = []
    lens = []
    for key, value in sorted(dict_ages.items()):
        ages.append(key)
        lens.append(value)
    plt.plot(ages, lens)
    plt.title("Связь возраста и средней длины " + s)
    plt.xlabel("Возраст")
    plt.ylabel("Средняя длина " + s)
    plt.savefig(name)
    plt.show()

def graph_cities(dict_cities, s, name):
    cities = []
    lens = []
    for key, value in dict_cities.items():
        cities.append(key)
        lens.append(value)
    plt.bar(range(len(cities)), lens)
    plt.title("Связь города и средней длины " + s)
    plt.xlabel("Город")
    plt.ylabel("Средняя длина " + s)
    plt.xticks(range(len(cities)), cities, rotation=90)
    plt.legend()
    plt.savefig(name)
    plt.show()


posts, texts, authors, lengths = get_posts()
authors_c, lengths_c, texts_c = get_comments(posts)
p_len, c_len= length(texts, texts_c)
graph_lengths(p_len, c_len)
dict_ages = get_age(authors, lengths)
graph_age(dict_ages, 'поста', 'graph2.png')
dict_cities = get_city(authors, lengths)
graph_cities(dict_cities, 'поста', 'graph3.png')
dict_comm_ages = get_age(authors_c, lengths_c)
graph_age(dict_comm_ages, 'комментария', 'graph4.png')
dict_comm_cities = get_city(authors_c, lengths_c)
graph_cities(dict_comm_cities, 'комментария', 'graph5.png')
