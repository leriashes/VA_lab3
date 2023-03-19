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

    n = len(table)
    a = table[0][0]
    b = table[n - 1][0]

    while(True):
        print('Введите значение x для точки: ', end='')
        xzn = float(input())

        if xzn >= a and xzn <= b:
            break

    result = 0

    for i in range(n):
        chisl = table[i][1]
        znam = 1
        for j in range(n):
                if (i != j):
                    chisl *= xzn - table[j][0]
                    znam *= table[i][0] - table[j][0]
        result += chisl / znam

    print('Результат: ', result)

    coef_Lagrange = []

    for i in range(n):
        coef1 = []
        coef = []

        znam = 1

        if i == 0:
            coef.append(table[1][0] * (-1))
        else:
            coef.append(table[0][0] * (-1))

        coef.append(1)

        for k in range(n):
            if k != i and k != abs(bool(i) - 1):

                coef1 = coef.copy()

                coef.insert(0, 0)

                for j in range(len(coef1)):
                    coef[j] += coef1[j] * table[k][0] * (-1)

            if k != i:
                znam *= (table[i][0] - table[k][0])

        for j in range(len(coef)):
            coef[j] /= znam
            coef[j] *= table[i][1]

        if i == 0:
            for j in range(len(coef)):
                coef_Lagrange.append(coef[j])
        else:
            for j in range(len(coef)):
                coef_Lagrange[j] += coef[j]

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