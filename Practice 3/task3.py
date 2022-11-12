try:
    f = open("File.txt", 'r')
    string = f.read()
    print(string)
    f.close()
except FileNotFoundError:
    print("Файл не найден")