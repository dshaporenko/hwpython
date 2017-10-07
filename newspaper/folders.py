import os

def metadata(path, author, title, date, topic, link, year, name):
    path = os.path.join(path, name)
    row = '%s\t%s\t\t\t%s\t%s\tпублицистика\t\t\t%s\t\tнейтральный\tн-возраст\tн-уровень\tгородская\t%s\tТомские Новости\t\t%s\tгазета\tРоссия\tТомская область\tru\n'
    meta_path = r'C:\Tomskie_Novosti\metadata.csv'
    with open(meta_path, 'a', encoding = 'utf-8') as meta:
        meta.write(row % (path, author, title, date, topic, link, year))

def plain(text, author, title, date, topic, link, path, name):
    path = os.path.join(path, name)
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
