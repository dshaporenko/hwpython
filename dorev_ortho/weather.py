import urllib.request, re

def weather():
    wthr = []
    req = urllib.request.Request('https://yandex.ru/pogoda/skopje')
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    regTime = re.compile('<time class="time fact__time".*?</time>', flags= re.DOTALL)
    regTemp = re.compile('<div class="temp fact__temp">.*?</div>', flags= re.DOTALL)
    regCondition = re.compile('<div class="fact__condition day-anchor i-bem".*?</div>', flags= re.DOTALL)
    regFeelsLike = re.compile('<dl class="term term_orient_h fact__feels-like">.*?</dl>', flags= re.DOTALL)
    regFeelsLikeYest = re.compile('<dl class="term term_orient_h fact__yesterday">.*?</dl>', flags= re.DOTALL)
    regWind = re.compile('<dl class="term term_orient_v fact__wind-speed">.*?</dl>', flags = re.DOTALL)
    regPressure = re.compile('<dl class="term term_orient_v fact__pressure">.*?</dl>', flags = re.DOTALL)
    regHumidity = re.compile('<dl class="term term_orient_v fact__humidity">.*?</dl>', flags = re.DOTALL)
    regTag = re.compile('<.*?>', re.DOTALL)
    k = regTime.findall(html)
    l = regTag.sub('',k[0])
    wthr.append(l)
    k = regTemp.findall(html)
    l = regTag.sub('',k[0])
    wthr.append(l)
    k = regCondition.findall(html)
    l = regTag.sub('',k[0])
    wthr.append(l)
    k = regFeelsLike.findall(html)
    l = regTag.sub('',k[0])
    wthr.append(l)
    k = regFeelsLikeYest.findall(html)
    l = regTag.sub('',k[0])
    wthr.append(l)
    k = regWind.findall(html)
    l = regTag.sub('',k[0])
    wthr.append(l)
    k = regPressure.findall(html)
    l = regTag.sub('',k[0])
    wthr.append(l)
    k = regHumidity.findall(html)
    l = regTag.sub('',k[0])
    wthr.append(l)
    return wthr

        
