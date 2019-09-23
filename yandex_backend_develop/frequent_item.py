def main(numbers, elements):
    calculate = {}
    for one_element in range(numbers):
        if calculate.__contains__(elements[one_element]):
            calculate[elements[one_element]] = calculate[elements[one_element]] + 1
        else:
            calculate[elements[one_element]] = 1
    max_number = max(list(calculate.values()))
    result = 0
    for one_element in list(calculate.keys()):
        if max_number == calculate[one_element]:
            if result < int(one_element):
                result = int(one_element)
    return result


if __name__ == '__main__':
    numbers = int(input())
    elements = list(input().split(" "))
    print(main(numbers, elements))
