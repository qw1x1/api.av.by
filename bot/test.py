import json, io


with io.open("brand.json",encoding='utf-8') as js_file:
    d=json.load(js_file)


    for key, value in d.items():
        print(key, value)