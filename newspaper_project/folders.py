import os

def plain(text, author, title, date, topic, link, path):
    row = '@au %s\n@ti %s\n@da %s\n@topic %s\n@url %s\n%s'
    with open(path, 'w', encoding = 'utf-8') as art:
        art.write(row % (author, title, date, topic, link, text))

def mystem_xml(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            new_root = root.replace('plain', 'mystem-xml')
            f1 = f.replace('txt', 'xml')
            if not os.path.exists(new_root):
                os.makedirs(new_root)
            file = os.path.join(root, f)
            new_file = os.path.join(new_root, f1)
            os.system(r"C:\mystem.exe -cid --format xml " + file + " " + new_file)

def mystem_plain(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            new_root = root.replace('plain', 'mystem-plain')
            if not os.path.exists(new_root):
                os.makedirs(new_root)
            file = os.path.join(root, f)
            new_file = os.path.join(new_root, f)
            os.system(r"C:\mystem.exe -cid " + file + " " + new_file)
