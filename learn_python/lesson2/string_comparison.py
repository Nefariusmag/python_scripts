# Написать функцию, которая принимает на вход две строки
# Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
# Если строки одинаковые, вернуть 1
# Если строки разные и первая длиннее, вернуть 2
# Если строки разные и вторая строка 'learn', возвращает 3
# Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты


def string_comparsion(first_line, second_line):
    if type(first_line) is not str or type(second_line) is not str:
        return '0'
    elif first_line == second_line:
        return '1'
    elif len(first_line) >= len(second_line) and second_line != 'learn':
        return '2'
    elif first_line != second_line and second_line == 'learn':
        return '3'


def main():
    first_line = 'test_test_test'
    # second_line = 'test_test_test'
    # second_line = "2"
    # second_line = 2
    second_line = 'learn'
    # second_line = 'learn_learn_learn'
    print(string_comparsion(first_line, second_line))


if __name__ == '__main__':
    main()