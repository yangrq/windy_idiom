import json
import os
import shutil


def load_and_reduce(path):
    data = json.load(open(path, encoding="utf-8"))
    for item in data:
        del item["derivation"]
        del item["example"]
        del item["explanation"]
    return data


map = {'ā': ['a', 1],
       'á': ['a', 2],
       'ǎ': ['a', 3],
       'à': ['a', 4],
       'ē': ['e', 1],
       'é': ['e', 2],
       'ě': ['e', 3],
       'è': ['e', 4],
       'ō': ['o', 1],
       'ó': ['o', 2],
       'ǒ': ['o', 3],
       'ò': ['o', 4],
       'ī': ['i', 1],
       'í': ['i', 2],
       'ǐ': ['i', 3],
       'ì': ['i', 4],
       'ū': ['u', 1],
       'ú': ['u', 2],
       'ǔ': ['u', 3],
       'ù': ['u', 4],
       'ǖ': ['v', 1],
       'ǘ': ['v', 2],
       'ǚ': ['v', 3],
       'ǜ': ['v', 4]}


def pinyin_character_to_normal(pinyin_str):
    temp = []
    for word in pinyin_str.split(' '):
        for char in word:
            res = map.get(char, [' ', 0])
            if res != [' ', 0]:
                word = word.replace(char, res[0])
                break
        temp.append(word.replace('，', ''))
    return ' '.join(temp)


def append_to_file(data):
    try:
        os.mkdir("output")
    except:
        pass
    shutil.copyfile("origin/windy_idiom.dict.yaml.origin",
                    "output/windy_idiom.dict.yaml")
    shutil.copyfile("origin/windy_idiom.schema.yaml.origin",
                    "output/windy_idiom.schema.yaml")
    fp = open("output/windy_idiom.dict.yaml", mode="a+", encoding="utf-8")
    for item in data:
        pinyin = pinyin_character_to_normal(item["pinyin"])
        line = item["word"] + "\t" + \
            pinyin + "\n"
        fp.write(line)
        line = item["word"] + "\t" + \
            pinyin.split(' ')[0] + "\n"
        fp.write(line)
        line = item["word"] + "\t" + \
            item["abbreviation"] + "\n"
        fp.write(line)
    fp.close

def crlf2lf(target):
    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'
    with open(target, 'rb') as open_file:
        content = open_file.read()
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    with open(target, 'wb') as open_file:
        open_file.write(content)

def start_convert():
    data = load_and_reduce("idiom.json")
    append_to_file(data)
    crlf2lf("origin/windy_idiom.dict.yaml.origin")
    crlf2lf("output/windy_idiom.dict.yaml")
    crlf2lf("origin/windy_idiom.schema.yaml.origin")
    crlf2lf("output/windy_idiom.schema.yaml")


if __name__ == "__main__":
    start_convert()
