import numpy as np
import matplotlib.pyplot as plt

def read_table():
    spisok = []
    table = []

    with open('znacheniya.csv', 'r') as file:
        i = 0
        print('ТАБЛИЦА ЗНАЧЕНИЙ (x и y)')
        for line in file.readlines():
            spisok.append([])
            table.append([])
            spisok[i].append(line[:line.find(';')])
            line = line[line.find(';') + 1:]
            spisok[i].append(line[:-1])

            for j in range(2):
                table[i].append(float(spisok[i][j]))
                j += 1
            i += 1
        

    table.sort()

    for strok in table:
        print(strok[0], end='   ')
        print(strok[1])

    print()

    return table

def variant1():
    table = read_table()

    while(True):
        print('Введите значение x для точки: ', end='')
        xzn = float(input())

        if xzn >= table[0][0] and xzn <= table[len(table) - 1][0]:
            break

    return

def variant2():
    print(2)

while True:
    print('Режимы работы:\n1 - по заданной таблице значений определить \n    приближённое значение функции в точке\n2 - по заданной аналитически функции y = f(x) и массиву значений аргумента \n    вычислить таблицу значений функции\n\nВыберите режим работы программы: ', end='')
    variant = input()

    print('\n')
    if len(variant) == 1 and (variant[0] == '1' or variant[0] == '2'):
        if variant == '1':
            variant1()
        else:
            variant2()
        break


x = np.arange(-10, 10.01, 0.01)
plt.figure(figsize=(10, 5))
plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
plt.plot(x, -x, label=r'$f_3(x)=-x$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')
plt.show()