# Скачайте файл по ссылке (referat.txt)
# Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def length_of_file(content):
    return len(content)


def words_if_file(content):
    content_split_by_words = content.split()
    return len(content_split_by_words)


def replace_dot_on_question_mark(content, file):
    content_with_replace = content.replace('.', '?')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content_with_replace)


def main():
    content = read_file('referat.txt')
    print(f'len of line in file: {length_of_file(content)}')
    print(f'number of words in file: {words_if_file(content)}')
    replace_dot_on_question_mark(content, 'referat.txt')


if __name__ == '__main__':
    main()
