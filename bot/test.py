import json, io


with io.open("brand.json",encoding='utf-8') as js_file:
    d=json.load(js_file)
    i=0

    a={1:"qwe",2:"asd"}
    a.items()
    print(a[1])
   # for key, value in d.items():
    #    print(key, value)