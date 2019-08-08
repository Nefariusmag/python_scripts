# Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
# Оба аргумента нужно приводить к целому числу при помощи int() и перехватывать исключение ValueError если приведение типов не сработало


def get_sum(num_one, num_two):
    try:
        return sum([int(num_one), int(num_two)])
    except ValueError:
        return 'Переданы не целые числа'


def main():
    print(get_sum(1, 2))


if __name__ == '__main__':
    main()