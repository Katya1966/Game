import random
desserts = ['чизкейк', 'тирамису', 'морковный торт', 'синнабон']
random_index = random.randint(0, len(desserts) -1)
print(random_index)
char = desserts[random_index]
print('Загадан очень вкусный десерт. Угадай его. Если уагадаешь с первого раза, получишь этот десерт в подарок :)')
answer = input("Введи десерт: ")
count_try = 3

while answer != char:
    count_try = count_try - 1
    if count_try == 0:
        break
    print(f"Попытка: {count_try}. Ещё раз попробуй: ")
    answer = input("Введи блюдо: ")

if answer == char:
    print("Молодец!")
else:
    print("Жаль, что не угадал :(")