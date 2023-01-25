# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого
# списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию
# random);
import random
from collections import Counter


def F(list_names, N):
    random_name = []
    for i in range(N):
        name = random_name.append(random.choice(list_names))
    return random_name


names = (
'Dima', 'Ivan', 'Glen', 'Marina', 'Max', 'Tolya', 'Luda', 'Rita', 'Kristina', 'Larisa', 'Denis', 'Galina', 'Inna',
'Nina', 'Elena', 'Edik', 'Bob', 'Olga', 'Mary', 'Jessica', 'Marat')

random_list_names = F(names, 100)

print(random_list_names)


# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
def frequent_name_F():
    most_common_name = Counter(random_list_names).most_common()[0][0]
    return most_common_name


print('Самое часто встречающееся имя в списке:', frequent_name_F())


# Альтернативный вариант решения.
# Лично мне первый вариант нравится больше!
# def frequent_name_1_F():
#   spisok = str(random_list_names).split()
#    return max(spisok, key = spisok.count)

# print('Самое часто встречающееся имя в списке:', frequent_name_1_F())

# 3. Напишите функцию вывода самой редкой буквы, с которой начинаются имена в списке на выходе функции F.
def rarest_letter():
    letters_list = []
    random_list_names.sort()
    for i in random_list_names:
        letters_list.append(i[0])
    #    print(letters_list)

    letters_dict = dict()
    for i in letters_list:
        if i in letters_dict:
            letters_dict[i] += 1
        else:
            letters_dict[i] = 1
    #    print(letters_dict)

    sorted_letters_dict = sorted(letters_dict, key=letters_dict.get)
    #    print(sorted_letters_dict)

    letters = []
    for key in sorted_letters_dict:
        letters.append(key)

    result = "Самая редкая буква с которой начинаются имена в списке: " + letters[0]

    return result


print(rarest_letter())
