# coding: utf-8

# Комментарии

import os
import psutil  #стороний
import shutil
import sys

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)  # Копируй
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
            return True
        else:
            print("Возникла проблема копирования")
            return False

def sys_info():
    print("Вот что я знаю о системе:")
    print("Количество процессоров: ", psutil.cpu_count())
    print("Платформа: ", sys.platform)
    print("Кодировка файловой системы: ", sys.getfilesystemencoding())
    print("Текущая директория: ", os.getcwd())
    print("Текущий пользователь: ", os.getlogin())

def del_duplicate(dirname):
    file_list = os.listdir(dirname)
    doupl_count = 0

    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                doupl_count += 1
            print("Файл", fullname, "  был удалён")
    return doupl_count

print("SUPER PROGRAMM!!!")
print("Привет программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = ''

# PEP-8

while answer != 'q':
    answer = input("Давай поработаем? (Y/N/Q)")
    if answer == 'Y' or answer == 'y':
        print("Чем бы ты хотел заняться?")
        print("Вот что я умею:")
        print("[1] - вывести список файлов")
        print("[2] - выведу информацию о системе")
        print("[3] - выведу список процессов")
        print("[4] - продублировать файлы в текущей директории")
        print("[5] - продублировать указаный файл")
        print("[6] - удалить дубликаты файлов")
        do = int(input("Укажите номер действия: "))

        if do == 1:
            print(os.listdir())
        elif do == 2:
           sys_info()
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("=Дублирование файлов в текущей директории=")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i += 1
        elif do == 5:
            print("=Дублирование указанного файла=")
            filename = input("Укажите название файла: ")
            duplicate_file(filename)
        elif do == 6:
            print("=Удаление дубликатов в директории=")
            dirname = input("Укажите имя директории: ")
            file_list = os.listdir(dirname)
            count = del_duplicate(dirname)
            print("Файлов удалено: ", count)
        else:
            input("Ты придумал что то ещё?")

    elif answer == 'N' or answer == 'n':
        print(name, ", ну ты и лентяй!")
    elif answer == 'Q' or answer == 'q':
        print(name, ", досвидания!")
    else:
        print("В следующий раз выбирай ответ из предложенных вариантов.")
# pass - пустышка.
