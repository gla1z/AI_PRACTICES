class RealString:
    def __init__(self, word):
        self.word = word

    def __len__(self):
        return len(self.word)

    def same_string(self, word2):
        if isinstance(word2, RealString):
            print("Слова: '{}', '{}'".format(self.word, word2.word))
        else:
            print("Слова: '{}', '{}'".format(self.word, word2))

        if len(self.word) == len(word2):
            print("Результат: Слова равны!\n")
        if len(self.word) > len(word2):
            print("Результат: Первое слово больше!\n")
        if len(self.word) < len(word2):
            print("Результат: Второе слово больше!\n")

que1 = input("Введите первое слово: ")
que2 = input("Введите второе слово: ")
print('\n')

string1 = RealString(que1)
string1.same_string(que2)