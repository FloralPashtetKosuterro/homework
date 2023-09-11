
#Моя попытка в перебор "букаф"

stroka = input('Введите строку: ')
print({letter: stroka.count(letter) for letter in set(stroka)})