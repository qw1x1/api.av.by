import json, io


with io.open("brand.json",encoding='utf-8') as js_file:
    d=json.load(js_file)

    for country in d:
        print(country["id"])