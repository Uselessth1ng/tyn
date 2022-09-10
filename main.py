import re
import string
import sys
import numpy as np

file = open("txt.txt", 'r')  # Считываем текст
text = file.read().lower()
print("Введите исходное слово (слова)")
inp = input().lower().split(' ')  # Получаем слова на вход
print("Введите количество слов, которые хотите получить")
postfix = int(input())
print("Введите количество слов, которые будут учитываться как префикс (не более количества введенных слов)")
prefix = int(input())

if prefix>len(inp):
    print ("Неверный ввод")
    sys.exit()
res = re.sub('[' + string.punctuation + '0123456789—«»"]', '', text).split()  # Разделяем на слова+удаляем лишние знаки
lul = list()  # Конечный список слов
lol = list()  # Список слов на одну позицию
ch = True

for dd in range(postfix):
    o = 0
    while len(inp) > prefix:
        del inp[o]
        o+1
    for i in range(len(res) - len(inp)):  # -len(prefix) для того чтобы не искать после последнего слова
        if res[i] == inp[0]:  # находим совпадение первого слова с текстом
            for p in range(len(inp)):  # в этом цикле проверяем по очереди все слова вместе с первым совпавшим
                if res[i+p] != inp[p]:
                    ch = False
            if ch:
                lol.append(res[i+len(inp)])  # в случае если все слова совпали добавляем слово в вывод
            ch = True
    try:
        s = np.random.choice(lol)
        inp.append(s)
        lul.append(s)
    except ValueError:
        if dd == 0:
            print("Нет подходящего продолжения")
        else:
            print("Удалось вывести только ", dd, "слов(-о), подходящее продолжение отсутствует")
        sys.exit()
    lol.clear()

print("Добавленные слова ", lul)
