def int_func(wrd):
    return wrd.capitalize()

oneword = input ("Введите слово из маленьких латинских букв: ")
print(f"Итоговый вариант: {int_func(oneword)}")
s=""
many_words = [i for i in input('Введите строку из слов, разделенных пробелами: ').split()]
for i, el in enumerate (many_words):
    s = s+" " + int_func(el)
print (f"Итоговый вариант: {s}")