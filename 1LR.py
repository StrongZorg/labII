
from scipy.integrate import quad
import math

"""
Левые и правые прфмоугольники p = 1
Средние прямоугольники и трапеции p = 2
Парабола p = 4
"""

#### Проверка точности
def check (mean_1, mean_2, p):
    return abs( (mean_1 - mean_2) / (2**p - 1) )

#### Левые прямоугольники
def left_p (fun, edge, acc):
    
    a = edge[0]
    b = edge[1]
    b_a = b - a
    eps = acc + 1
    n = 1
    
    p = 1

    res = fun(a) * b_a
    
    while eps > acc:

        n *= 2
        int_2 = 0.0
        h = b_a / n
            
        for i in range(n):
            x_left = a + i * h
            int_2 += fun(x_left)
            
        int_2 *= h

        eps = check(res, int_2, p)

        res = int_2
        
    return res, eps, n

#### Правые прямоугольники
def right_p (fun, edge, acc):
    
    a = edge[0]
    b = edge[1]
    b_a = b - a
    eps = acc + 1
    n = 1
    
    p = 1

    res = fun(b) * b_a
    
    while eps > acc:

        n *= 2
        int_2 = 0.0
        h = b_a / n
            
        for i in range(1, n):
            x_right = a + i * h
            int_2 += fun(x_right)
            
        int_2 *= h

        eps = check(res, int_2, p)

        res = int_2
        
    return res, eps, n

#### Средние прямоугольники
def middle_p (fun, edge, acc):
    
    a = edge[0]
    b = edge[1]
    b_a = b - a
    eps = acc + 1
    n = 1
    
    p = 2

    res = fun(b_a/2) * b_a
    
    while eps > acc:

        n *= 2
        int_2 = 0.0
        h = b_a / n
            
        for i in range(n):
            x_middle = (a + h/2) + i * h
            int_2 += fun(x_middle)
            
        int_2 *= h

        eps = check(res, int_2, p)

        res = int_2
        
    return res, eps, n

#### Трапеции
def trap (fun, edge, acc):
    
    a = edge[0]
    b = edge[1]
    b_a = b - a
    eps = acc + 1
    n = 1
    
    p = 2

    n_k = (fun(a) + fun(b)) / 2

    res = n_k * b_a
    
    while eps > acc:

        n *= 2
        int_2 = n_k
        h = b_a / n
            
        for i in range(n):
            x = a + i * h
            int_2 += fun(x)
            
        int_2 *= h

        eps = check(res, int_2, p)

        res = int_2
        
    return res, eps, n

#### Симпсон
def simp (fun, edge, acc):
    
    a = edge[0]
    b = edge[1]
    b_a = b - a
    eps = acc + 1
    n = 2
    
    p = 2

    n_k = fun(a) + fun(b)

    res = ( n_k + 4*fun((a+b) / 2) ) * b_a / 6
    
    while eps > acc:

        n *= 2
        int_2 = n_k
        h = b_a / n

        for i in range(1, n):
            x = a + i * h
            if i % 2 == 0:
                int_2 += 2 * fun(x)
            else:
                int_2 += 4 * fun(x)
            
        int_2 *= h / 3

        eps = check(res, int_2, p)

        res = int_2
        
    return res, eps, n

#################################################################
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")
#################################################################
"""
fun = lambda x: math.exp(-x -1/x)
accur = 0.001
"""
edge = [0, 1]

fun_str = str(input("Введите подынтегральную функцию(формате python): "))
fun = lambda x: eval(fun_str)

edge[0] = float(input("Введите нижний предел: "))
edge[1] = float(input("Введите верхний предел: "))

accur = float(input("Введите желаемую точность: "))

#################################################################
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")
#################################################################

resault, accurate = quad(fun, edge[0], edge[1])
print(f"Результат quad - {resault:.4f}\nОшибка quad - {accurate}\n")

resault, accurate, n = left_p(fun, edge, accur)
print(f"Результат м. левых прямоугольников- {resault:.4f}\n\
        Ошибка м. левых прямоугольников - {accurate}\n\
        Количество разбиений - {n}\n")


resault, accurate, n = right_p(fun, edge, accur)
print(f"Результат м. правых прямоугольников - {resault:.4f}\n\
        Ошибка м. правых прямоугольников - {accurate}\n\
        Количество разбиений - {n}\n")

resault, accurate, n = middle_p(fun, edge, accur)
print(f"Результат м. средних прямоугольников - {resault:.4f}\n\
        Ошибка м. средних прямоугольников - {accurate}\n\
        Количество разбиений - {n}\n")

resault, accurate, n = trap(fun, edge, accur)
print(f"Результат м. трапеций - {resault:.4f}\n\
        Ошибка м. трапеций - {accurate}\n\
        Количество разбиений - {n}\n")

resault, accurate, n = simp(fun, edge, accur)
print(f"Результат м. парабол - {resault:.4f}\n\
        Ошибка м. парабол - {accurate}\n\
        Количество разбиений - {n}\n")

#################################################################
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")
#################################################################
