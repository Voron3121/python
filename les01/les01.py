# coding: utf-8

#Комментарии
print("SUPER PROGRAMM!!!")
print("Привет программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давай поработаем? (Y/N)")


#PEP-8
if answer == 'Y' or answer == 'y':
    print("Чем бы ты хотел заняться?")
    print("1. Программировать?")
    print("2. Почитать?")
    print("3. Просто подумать?")
    work = input("Что выбираешь? (1, 2 или 3)")
    if work == '1':
        print("Давай ", name, ", сделаем это.")
    elif work == '2':
        print("Очень много есть интересных книг, выбери сам.")
    elif work == '3':
        print("Погрузись в свои мысли.")
    else:
        input("Ты придумал что то ещё?")
elif answer == 'N' or answer == 'n':
    print(name, ", ну ты и лентяй!")
else:
    print("В следующий раз выбирай ответ из предложенных вариантов.")
#pass - пустышка.
