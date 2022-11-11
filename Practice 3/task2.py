def add_string():
    f = open('File.txt', "a")
    string = input("Введите строку: ")
    f.write(f"{string}\n")
    f.close()

add_string()
print("[+] Строка добавлена")