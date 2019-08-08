# Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

# Чтобы не потерять чужой клевый код
# from statistics import mean
# from itertools import chain
#
# def school_mean(raiting):
#     all_scores_of_one_class = [i['scores'] for i in raiting]
#     return mean(chain(*all_scores_of_one_class))
#
#
# def class_mean(raiting):
#     for data in raiting:
#         yield data['school_class'], mean(data['scores'])


def rating_class(raiting):
    sum_of_all_scores = 0
    number_of_all_students = 0
    for all_scores_of_one_class in raiting:
        sum_of_scores_in_class = 0
        number_of_student_in_class = 0
        for score in all_scores_of_one_class['scores']:
            sum_of_scores_in_class += score
            number_of_student_in_class += 1
        number_of_all_students += number_of_student_in_class
        sum_of_all_scores += sum_of_scores_in_class
        grade_point_average_in_class = sum_of_scores_in_class / number_of_student_in_class
        print(f'Средний балл по {all_scores_of_one_class["school_class"]}: {grade_point_average_in_class}')

    print(f'Учеников в школе: {number_of_all_students}')
    grade_point_average = sum_of_all_scores / number_of_all_students
    print(f'Средний балл по школе {grade_point_average}')


def main():
    raiting = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
               {'school_class': '5a', 'scores': [3, 5, 2, 5, 5]},
               {'school_class': '5b', 'scores': [3, 3, 4, 3, 3]},
               {'school_class': '6a', 'scores': [3, 3, 4, 3, 3]},
               {'school_class': '6b', 'scores': [2, 5, 3, 4, 3]},
               {'school_class': '7a', 'scores': [5, 2, 3, 3, 5]},
               {'school_class': '7b', 'scores': [4, 2, 2, 3, 3]}]
    rating_class(raiting)
    # Запуск чужего прикольного кода
    # print(school_mean(raiting))
    # print(*class_mean(raiting), sep='\n')


if __name__ == '__main__':
    main()