import numpy as np
import matplotlib.pyplot as plt
import math

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

def read_x():
    spisok = []
    xt = []

    with open('fx.csv', 'r') as file:
        i = 0
        for line in file.readlines():
            spisok.append(line[:line.find(';')])
            xt.append([])
            xt[i].append(float(spisok[i]))
            i += 1
        
    xt.sort()

    return xt

def Lagrange(table):

    n = len(table)
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

    print('\nПолином Лагранжа: ', end='')

    for i in range(n - 1):
        print(coef_Lagrange[len(coef_Lagrange) - 1 - i], ' * (x^', n - i - 1, ') + ', end='', sep='')

    print(coef_Lagrange[0])

    return coef_Lagrange

def Newton(table, f):
    #вычисление разностей
    n = len(table)
    
    f.append([])
    for i in range(n):
        f[0].append(table[i][1])
        

    for i in range(1, n):
        f.append([])
        k = i
        for j in range(n - i):
            f[i].append((f[i - 1][j + 1] - f[i - 1][j])/(table[k][0] - table[j][0]))
            k += 1

    print('\nПолином Ньютона: ', table[0][1], end='')

    for i in range(n - 1):
        print(' + ', end='')
        for j in range(i + 1):
            print('(x - ', end='')
            if table[j][0] < 0:
                print('(', table[j][0], ')', end='', sep='')
            else:
                print(table[j][0], end='')
            print(') * ', end='')

        if f[i + 1][0] < 0:
            print('(', f[i + 1][0], ')', end='', sep='')
        else:
            print(f[i + 1][0], end='')
    
    return

def count_Lagrange(xs, coefs):
    order = len(coefs)

    ys = np.zeros(len(xs))

    ys += coefs[order - 1]

    for i in range(order - 1):
        ys *= xs
        ys += coefs[order - 2 - i]

    return ys

def count_Newton(xs, f, table):

    ys = np.zeros(len(xs))
    ys += f[0][0]

    n = len(table)

    s = []

    for i in range(n - 1):
        s.append([])
        for j in range(len(ys)):
            s[i].append(f[i + 1][0])
   
    r = np.zeros(len(xs))

    for i in range(n - 1):
        r = xs - table[i]

        for j in range(n - 2, -1 + i, -1):
            s[j] *= r

    for i in range(n - 1):
        ys += s[i]

    return ys

def count_function(xs, func):
    ys = []

    for i in range(len(xs)):
        x = xs[i]
        ys.append(eval(func))
    return ys

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

    for i in range(n - 1):
        if xzn >= table[i][0]:
            if xzn <= table[i + 1][0]:
                a = (table[i + 1][1] - table[i][1]) / (table[i + 1][0] - table[i][0])
                result = a * xzn + table[i][1] - a * table[i][0]

    print('\nРезультат (линейная интерполяция): ', result)


    result = 0

    count = 0
    for i in range(n):
        chisl = table[i][1]
        znam = 1
        for j in range(n):
            count += 1
            if (i != j):
                chisl *= xzn - table[j][0]
                znam *= table[i][0] - table[j][0]
        result += chisl / znam

    print('\n\nРезультат (полином Лагранжа): ', result)


    coef_Lagrange = Lagrange(table)

    result1 = coef_Lagrange[len(coef_Lagrange) - 1]
    count = 0

    for i in range(n - 1):
        result1 *= xzn
        result1 += coef_Lagrange[len(coef_Lagrange) - 2 - i]
        count += 1

    print('\nРезультат (полином Лагранжа): ', result1)


    f = []
    Newton(table, f)

    result = table[0][1]
    s = []

    for i in range(1, n):
        s.append(f[i][0])

    for i in range(n - 1):
        r = xzn - table[i][0]

        for j in range(n - 2, -1 + i, -1):
            s[j] *= r

    for i in range(n - 1):
        result += s[i]

    print('\n\nРезультат (полином Ньютона): ', result)

    xt = []
    yt = []

    for i in range(len(table)):
        xt.append(table[i][0])
        yt.append(table[i][1])

    x = np.arange(table[0][0], table[len(table) - 1][0], 0.001)
    plt.plot(x, count_Lagrange(x, coef_Lagrange))
    plt.plot(x, count_Newton(x, f, xt))

    plt.plot(xzn, result, 'ro')
    plt.plot(xt, yt, 'bo')
    plt.grid(True)

    return

def variant2():
    print('Введите функцию: y = ', end='')
    func = input()

    table = read_x()

    for i in range(len(table)):
        x = table[i][0]
        table[i].append(eval(func))
        print('x = ', table[i][0], '   y = ', table[i][1], sep='')

    coef_Lagrange = Lagrange(table)

    f = []
    Newton(table, f)

    xt = []
    yt = []

    for i in range(len(table)):
        xt.append(table[i][0])
        yt.append(table[i][1])

    x = np.arange(table[0][0], table[len(table) - 1][0], 0.001)
    plt.plot(x, count_Lagrange(x, coef_Lagrange))
    plt.plot(x, count_Newton(x, f, xt))
    plt.plot(x, count_function(x, func))

    plt.plot(xt, yt, 'bo')
    plt.grid(True)

    

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

    

x = np.arange(-9, 74, 0.01)
"""plt.figure(figsize=(10, 5))
#plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
#plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
#plt.plot(x, -x, label=r'$f_3(x)=-x$')
c = np.poly1d([-10, 10, 15])


plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')"""
plt.show()