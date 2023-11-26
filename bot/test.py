from api.controls import get_location_user, change_location_user, get_user_id_on_procent

import requests, json, math
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs

def pars_page():
    user = User().random
    respons_page = requests.get('https://cars.av.by/jetour/dashing/106399677', headers={'user-agent': f'{user}'})
    if respons_page.status_code == 200:
        data_soup = bs(respons_page.text, 'lxml')
        return data_soup
    return 0

def mid_price(data_soup):       
        total = ''
        try:
            mid_price = data_soup.find(class_='featured__price-value').text
        except AttributeError:
            mid_price = data_soup.find(class_='card__price-secondary').text
        
        for item in mid_price:
            if item in '1234567890':
                total += item
        return int(total)
    
gg = pars_page()
price = mid_price(gg)
print(price)
    
    # for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
    #     link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
    #     price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
        
    #     car_list.append({'link':link_car,'price': price_car})
    # self.car.append(car_list)
    # return  respons_list
        

