# coding: utf-8

#Комментарии
print("SUPER PROGRAMM!!!")
print("Привет программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давай поработаем? (Y/N)")


#PEP-8
if answer == 'Y':
    print("Вам премия!")
elif answer == 'N':
    print("До свидания")
else:
    print("Неизвестный ответ")
#pass - пустышка.
