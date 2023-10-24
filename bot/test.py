import requests, json, math

# https://web.telegram.org/a/#2139630052

respons_page = requests.get('https://web.telegram.org/a/#faribybot')
print(respons_page)