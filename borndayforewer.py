while True:
    bornyear = input('Введите год рождения А.С.Пушкина: ')

    if bornyear == '1799':
        while True:
            bornday = input('День рождения А.С.Пушкина: ')
            if bornday == '6 июня' or bornday == '6.06' or bornday == '06.06':
                print('Верно')
                break
            else:
                print('Неверны день рождения')
        break
    else:
        print('Неверный год рождения')
