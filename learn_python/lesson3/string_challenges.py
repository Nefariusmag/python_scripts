print("Вывести последнюю букву в слове")
word = 'Архангельск'
print(word[-1])


print("Вывести количество букв а в слове")
word = 'Архангельск'
print(len(word))


print("Вывести количество гласных букв в слове")
vowels = ["а", "о", "и", "е", "ё", "э", "ы", "у", "ю", "я"]
word = 'Архангельск'
q = 0
for i in word:
    if i.lower() in vowels:
        q += 1
print(q)
# q  = len([i for i in word if i in vowels])


print('Вывести количество слов в предложении')
sentence = 'Мы приехали в гости'
tests = sentence.split()
print(len(tests))


print('Вывести первую букву каждого слова на отдельной строке')
sentence = 'Мы приехали в гости'
tests = sentence.split()
for i in tests:
    print(i[0])


print('Вывести усреднённую длину слова.')
sentence = 'Мы приехали в гости'
len_words = 0
tests = sentence.split()
for i in tests:
    len_words += len(i)

print(len_words/len(tests))
