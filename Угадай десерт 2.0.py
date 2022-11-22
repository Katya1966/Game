import random
desserts = ['чизкейк', 'тирамису', 'морковный торт', 'синнабон']

def play(random_dessert = (random.choice(desserts))):           
    print('Загадан очень вкусный десерт. Угадай его. Если уагадаешь с первого раза, получишь этот десерт в подарок :)\n')
    for i in desserts:
        print(i)
    print('\n')

    if random_dessert == 'чизкейк':
        print('мой любимый десерт\n')
    if random_dessert == 'тирамису':
        print('десерт родом из Италии\n')
    if random_dessert == 'морковный торт':
        print('хорош в Вольчека\n')
    if random_dessert == 'синнабон':
        print('что-то вкусненькое с корицей\n')

    
    answer = input("Введи десерт: ")
    count_try = 1

    while answer != random_dessert:
        count_try = count_try + 1
        if count_try == 4:
            break
        print(f"\nПопытка: {count_try}. Ещё раз попробуй: \n")

    

        if random_dessert == 'чизкейк':
            print('тортик\n')
        if random_dessert == 'тирамису':
            print('что-то на кофейном\n')
        if random_dessert == 'морковный торт':
            print('оранжевенький\n')
        if random_dessert == 'синнабон':
            print('последние три буквы на французский манер\n')
    
        answer = input("Введи блюдо: ")

    if answer == random_dessert:
        print("\nМолодец!")
    else:
        print("\nЖаль, что не угадал :(")

play()

