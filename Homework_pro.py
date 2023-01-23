# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого
# списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию
# random);
import random


def F(list_name, N):
    random_name = []
    for i in range(N):
        name = random_name.append(random.choice(list_name))
    return random_name

random_list_name = F(
    ('Dima', 'Ivan', 'Glen', 'Marina', 'Max', 'Tolya', 'Luda', 'Rita', 'Kristina', 'Larisa', 'Denis', 'Galina',
     'Inna', 'Nina', 'Elena', 'Edik', 'Bob', 'Olga', 'Mary', 'Jessica', 'Marat'), 100)

print(random_list_name)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
#def frequent_name():



# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
