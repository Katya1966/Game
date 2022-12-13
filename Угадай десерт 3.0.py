import random
desserts = {'чизкейк':['мой любимый десерт', 'тортик', 'нежная, кремовая текстура'],
        'тирамису':['десерт родом из Италии', 'что-то на кофейном', 'в этой вкусняшке много слоев'],
        'морковный торт':['хорош в Вольчека', 'оранжевенький', 'один ингредиент в нем очень полезный'],
        'синнабон':['что-то вкусненькое с корицей', 'последние три буквы на французский манер', 'в Цехе 85 есть своя версия этой вкусняшки']}


def play():
    random_dessert = (random.choice(list(desserts.keys())))
    print('Загадан очень вкусный десерт. Угадай его. Если угадаешь с первого раза, получишь этот десерт в подарок :)\n')
    for i in desserts:
        print(i)
    print('\n')

    def help(n):
        for i in desserts.keys():
            if i == random_dessert:
                print(desserts.get(i)[n])
    help(0)
        

    
    answer = input("Введи десерт: ")
    count_try = 1

    while answer != random_dessert:
        count_try = count_try + 1
        if count_try == 4:
            break
        print(f"\nПопытка: {count_try}. Ещё раз попробуй: \n")

        if count_try == 2:
            help(1)
        if count_try == 3:
            help(2)

        answer = input("Введи блюдо: ")


    if answer == random_dessert and count_try == 1:
        print("\nМолодец! Угощаю тебя этой вкусняшкой при нашей следующей встрече :)")
    elif answer == random_dessert:
        print("\nМолодец!")
    else:
        print("\nЖаль, что не угадал(a) :(")

play()



