import numpy as np
import matplotlib.pyplot as plt

def variant1():
    print(1)

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