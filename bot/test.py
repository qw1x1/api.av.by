lst = ['Volkswagen', 'Sharan', 'I', '·', '2-й', 'рестайлнг,']




print(lst)

def get_car_name(self, lst):
    lst.reverse()
    if lst[0] == 'Рестайлнг' and len(lst) == 5:
        gen = f'Рестайлинг {lst[1]} {lst[2]}'
        mod = f'{lst[3]}'
        brand = f'{lst[4]}'
    elif len(lst) == 3:
        gen = f'{lst[0]}'
        mod = f'{lst[1]}'
        brand = f'{lst[2]}'
    elif len(lst) == 6 and lst[0] == 'рестайлнг,':
        gen = f'{lst[3]} {lst[2]} {lst[1]} рестайлинг'
        mod = f'{lst[4]}'
        brand = f'{lst[5]}'
    else:
        gen = 0
        mod = 0
        brand = 0
    return brand, mod, gen

print(get_car_name(1, lst))