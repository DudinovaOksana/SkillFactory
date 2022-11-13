#импорт библиотеки для регулярных выражений
import re
#запрашиваем имя файла для считывания у пользователя
a = input("Введите имя файла")
#открываем файл для чтения
myfile = open(a, 'rt', encoding='utf8')
#считываем построчно текст из файла
file = myfile.readlines()
#разбиваем строки файла на слова
spisok_slov = []
for string in file:
    spisok_slov += string.split()
# с помощью list comprehension отбираем из списка слова с количеством букв больше 3-х
more_3_words = [x for x in spisok_slov if len(x)>3]
#делаем словарь, в котором ключ - это слово, а значение - это количество повторений этого слова
common_word_dict = {x:more_3_words.count(x) for x in more_3_words}
#выбираем из словаря наиболее часто встречающееся слово с помощью функции max()
common_word = max(common_word_dict, key = common_word_dict.get)
#содаем регулярное выражение для поиска только английских слов
r = re.compile('[a-zA-Z]+')
#c помощью list comprehension в отдельный список записываем только английские слова
output = [w for w in filter(r.match, spisok_slov)]
#при помощи функции max() отбираем самое длинное английское слово
english_longest_word = max(output, key=len)
#вывод полученных результатов на экран
print(f'Наиболее часто встречающееся слово из 3-х символов: {common_word}')
print(f'Самое длинное слово на английском языке: {english_longest_word}')
#закрываем открытый для чтения файл
myfile.close()

