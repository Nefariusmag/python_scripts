def main(t1, t2, operation):
    list1 = list(t1.keys())
    list2 = list(t2.keys())

    def inner(t1, t2):
        list_keys_for_list3 = []
        list3 = {}
        for element_of_list3 in list1:
            if element_of_list3 in list2:
                list_keys_for_list3.append(element_of_list3)
        for one_key_of_list3 in list_keys_for_list3:
            value1 = t1[one_key_of_list3]
            value2 = t2[one_key_of_list3]
            list3[one_key_of_list3] = f'{value1} {value2}'
        return list3

    def left(t1, t2):
        list_keys_for_list3 = list1
        list3 = {}
        for one_key_of_list3 in list_keys_for_list3:
            value1 = t1[one_key_of_list3]
            if t2.__contains__(one_key_of_list3):
                value2 = t2[one_key_of_list3]
            else:
                value2 = 'NULL'
            list3[one_key_of_list3] = f'{value1} {value2}'
        return list3

    def right(t1, t2):
        list_keys_for_list3 = list2
        list3 = {}
        for one_key_of_list3 in list_keys_for_list3:
            if t1.__contains__(one_key_of_list3):
                value1 = t1[one_key_of_list3]
            else:
                value1 = 'NULL'
            value2 = t2[one_key_of_list3]
            list3[one_key_of_list3] = f'{value1} {value2}'
        return list3

    def full(t1, t2):
        list_keys_for_list3 = []
        list3 = {}
        list_keys_for_list3 = list1 + list2
        for one_key_of_list3 in list_keys_for_list3:
            if t1.__contains__(one_key_of_list3):
                value1 = t1[one_key_of_list3]
            else:
                value1 = 'NULL'
            if t2.__contains__(one_key_of_list3):
                value2 = t2[one_key_of_list3]
            else:
                value2 = 'NULL'
            list3[one_key_of_list3] = f'{value1} {value2}'
        return list3

    if operation == 'INNER':
        list3 = inner(t1, t2)
    elif operation == 'LEFT':
        list3 = left(t1, t2)
    elif operation == 'RIGHT':
        list3 = right(t1, t2)
    elif operation == 'FULL':
        list3 = full(t1, t2)

    return list3


if __name__ == '__main__':
    n1 = int(input())
    t1 = {}
    for number_line in range(n1):
        value = input().split(" ")
        t1[value[0]] = value[1]
    n2 = int(input())
    t2 = {}
    for number_line in range(n2):
        value = input().split(" ")
        t2[value[0]] = value[1]
    operation = input()

    main(t1, t2, operation)
