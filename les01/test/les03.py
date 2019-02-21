# coding: utf-8

# Комментарии

import os

import psutil  #стороний

print("SUPER PROGRAMM!!!")
print("Привет программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давай поработаем? (Y/N)")

# PEP-8
if answer == 'Y' or answer == 'y':
    print("Чем бы ты хотел заняться?")
    print("Вот что я умею:")
    print("[1] - вывести список файлов")
    print("[2] - выведу информацию о системе")
    print("[3] - выведу список процессов")
    do = int(input("Укажите номер действия: "))

    if do == 1:
        print(os.listdir())
    elif do == 2:
        pass
    elif do == 3:
        print(psutil.pids())
    else:
        input("Ты придумал что то ещё?")

elif answer == 'N' or answer == 'n':
    print(name, ", ну ты и лентяй!")
else:
    print("В следующий раз выбирай ответ из предложенных вариантов.")
# pass - пустышка.
