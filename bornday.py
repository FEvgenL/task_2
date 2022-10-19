bornyear = input('Введите год рождения А.С.Пушкина: ')
bornday_lst = ['6 июня', '6.06', '06.06']

if bornyear == '1799':
    bornday = input('День рождения А.С.Пушкина: ')
    if bornday in bornday_lst:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')
