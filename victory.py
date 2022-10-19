'''
Годы рождения Русских писателей:
А.С.Пушкин - 1799
М.Ю.Лермонтов - 1814
Ф.М.Достоевский - 1821
Л.Н.Толстой - 1828
М.А.Булгаков - 1891
'''
writers = {'А.С.Пушкина': '1799',
           'М.Ю.Лермонтова': '1814',
           'Ф.М.Достоевскова': '1821',
           'Л.Н.Толстова': '1828',
           'М.А.Булгакова': '1891'}
answers = len(writers)
yes = ['Да', 'да', 'Yes', 'yes', 'y']

while True:
    right_answer = 0
    for writer in list(iter(writers)):
        answer = input(f'Год рождения {writer}?  ')
        if answer == writers[writer]:
            right_answer += 1
        right_answer_pct = right_answer * 100 / answers
    print('-' * 30)
    print(f'Количество правильных ответов: {right_answer}')
    print(f'Количество неправлиьных ответов: {answers - right_answer}')
    print(f'Процент правильных ответов: {right_answer_pct}')
    print(f'Процент неправильных ответов: {100 - right_answer_pct}')
    yes_or_no = input('\nХотите повторить игру? ')
    print()
    if yes_or_no in yes:
        continue
    else:
        break
