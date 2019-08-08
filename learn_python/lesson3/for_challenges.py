# Задание 1
print('Необходимо вывести имена всех учеников из списка с новой строки')
names = ['Оля', 'Петя', 'Вася', 'Маша']
# for one_name in names:
#     print(one_name)
print('\n'.join(names))


# Задание 2
print('Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.')
names = ['Оля', 'Петя', 'Вася', 'Маша']
for one_name in names:
    print(f'{one_name}: {len(one_name)}')

# Задание 3
print('Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика')
is_male = {
    'Оля': False,  # если True, то пол мужской
    'Петя': True,
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for one_name in names:
    if is_male[one_name] == False:
        sex = 'F'
    else:
        sex = 'M'
    print(f'{one_name}: {sex}')


# Задание 4
# Даны группу учеников.
print('Нужно вывести количество групп и для каждой группы – количество учеников в ней')
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.
groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
]
print(f'Всего групп: {len(groups)}')
for one_group in groups:
    print(f'В группе {len(one_group)} ученика.')


# Задание 5
print('Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.')
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша
groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
]
number_group = 0
for one_group in groups:
    # names_in_group = ''
    number_group += 1
    # for names in one_group:
    #     names_in_group += names + ' '
    names_in_group = ' '.join(one_group)
    print(f'Группа {number_group}: {names_in_group}')



