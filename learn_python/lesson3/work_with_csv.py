import csv


def work_in_csv(list_people, file_csv):
    with open(file_csv, "w", newline="") as file:
        column = []
        for one_line_info_about_people in list_people:
            for one_title_from_list in one_line_info_about_people:
                column.append(one_title_from_list)
            break
        writer = csv.DictWriter(file, column, delimiter=';')
        writer.writerows(list_people)


def main():
    list_people = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
    file_csv = "users.csv"
    work_in_csv(list_people, file_csv)


if __name__ == '__main__':
    main()
