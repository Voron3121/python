# coding: utf-8

# Комментарии

import os
import psutil  #стороний
import shutil
import sys

print("SUPER PROGRAMM!!!")
print("Привет программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = ''
# PEP-8
while answer != 'q' or 'Q':
    answer = input("Давай поработаем? (Y/N/Q)")
    if answer == 'Y' or answer == 'y':
        print("Чем бы ты хотел заняться?")
        print("Вот что я умею:")
        print("[1] - вывести список файлов")
        print("[2] - выведу информацию о системе")
        print("[3] - выведу список процессов")
        print("[4] - дублирование файлов")
        do = int(input("Укажите номер действия: "))

        if do == 1:
            print(os.listdir())
        elif do == 2:
            print("Вот что я знаю о системе:")
            print("Количество процессоров: ", psutil.cpu_count())
            print("Платформа: ", sys.platform)
            print("Кодировка файловой системы: ", sys.getfilesystemencoding())
            print("Текущая директория: ", os.getcwd())
            print("Текущий пользователь: ", os.getlogin())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("=Дублирование файлов в текущей директории=")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                newfile = file_list[i] + '.dupl'
                shutil.copy(file_list[i], newfile) #Копируй
                i += 1
        else:
            input("Ты придумал что то ещё?")

    elif answer == 'N' or answer == 'n':
        print(name, ", ну ты и лентяй!")
    elif answer == 'Q' or answer == 'q':
        print(name, ", досвидания!")
    else:
        print("В следующий раз выбирай ответ из предложенных вариантов.")
# pass - пустышка.
