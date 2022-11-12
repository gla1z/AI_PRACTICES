import os

def copy_file():
    name = input("Введите имя файла: ")
    f = open(name, 'r')
    copy = "copy_"+name
    f_copy = open(copy, 'w')
    string = f.readline()
    f_copy.writelines(string)
    f.close()
    f_copy.close()
    if os.path.isfile(name):
        print("[-] Файл удалён")
    else:
        print("Файл не найден")

copy_file()