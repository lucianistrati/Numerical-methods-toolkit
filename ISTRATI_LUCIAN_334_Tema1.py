#1
import matplotlib.pyplot as plt
import numpy as np
import random
import math
EPS = 1e-5

def func_1(x:float):
    return x**2 - 3

def metoda_bisectiei(a:float, b:float, callback_function):
    
    if callback_function(a) * callback_function(b) >= 0:
        print("Valorile {} si {} nu indeplinesc conditia de semn distinct ".format(a,b))
        return
    numar_iteratii = 0
    while (b - a) >= EPS:
        numar_iteratii+=1
        c = (a + b) / 2
        if callback_function(c) == 0.0:
            break
        if callback_function(c) * callback_function(a) < 0:
            b = c
        else:
            a = c
    print("Valoarea gasita dupa un numar de {} iteratii este {}".format(numar_iteratii, round(c,7)))
    return c

# pentru a afla zecimalele lui radical din 3 este echivalent cu a rezolva ecuatia x^2-3=0
def one():
    rezultat = metoda_bisectiei(0,10, func_1) # 1-START

#2
def g(x:float):
    return math.e**(x-2)

def h(x:float):
    return math.cos(math.e**(x-2))+1

def ec_g_h(x:float):
    return (g(x)-h(x))

def two():
    xvalues = np.linspace(0,5,10000)
    gvalues = list(map(g, xvalues))
    hvalues = list(map(h,xvalues))
    plt.plot(xvalues, gvalues, color="red")
    plt.plot(xvalues, hvalues, color="green")
    plt.xlabel('x')
    plt.ylabel('y')
    rezultat_ec_g_h = metoda_bisectiei(0, 50, ec_g_h)
    y_g = g(rezultat_ec_g_h)
    plt.plot(rezultat_ec_g_h, y_g, 'ro', color="blue")
    print("Punctul de intersectie are coordonatele ({},{}) ".format(rezultat_ec_g_h, y_g))
    plt.axhline()
    plt.axvline()
    plt.show()



#3

def func_f(x:float):
    return x**3 + 5*x**2 +2*x - 8

def pozitie_falsa(f, a, b, my_eps):
    k = 0
    a0 = a
    b0 = b
    x0 = (a0 * f(b0) - b0 * f(a0) ) / (f(b0) - f(a0))
    N = 0
    x1, a1, b1 = None, None, None

    def run_step_2(N, k, a0, b0, x0, f):
        N+=1
        if f(x0)==0:
            x1 = x0
            x_aprox = x1
            return x1, None, None, None
        elif f(a0)*f(x0)<0:
            a1 = a0
            b1 = x0
            x1 = (a1 * f(b1) - b1 * f(a1))/(f(b1)-f(a1))
        elif f(a0)*f(x0)>0:
            a1 = x0
            b1 = b0
            x1 = (a1 * f(b1) - b1 * f(a1))/(f(b1)-f(a1))
        ret_val = abs(x1-x0)/abs(x0)
        return ret_val, a1, b1, x1, N

    ret_val, a1, b1, x1, N = run_step_2(N, k, a0, b0, x0, f)

    if a1==None:
        return x1

    while ret_val>= my_eps:
        k+=1
        ret_val, a1, b1, x1, N = run_step_2(N, k, a0, b0, x0, f)
        a0 = a1
        b0 = b1
        x0 = x1

    x_aprox = x1
    return x_aprox, N

def create_plot_context(rezultate, iteratii):
    xvalues = np.linspace(-5,5,1000)
    yvalues = list(map(func_f,xvalues))
    plt.plot(xvalues,yvalues,color='red')
    plt.axhline()
    plt.axvline()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Metoda secantei dupa " + str(iteratii[0]) + "," + str(iteratii[1]) + ", respectiv " + str(iteratii[2]) + " iteratii pentru solutiile: " + str(round(rezultate[0], 2)) + "," + str(round(rezultate[1], 2)) + ", respectiv " + str(round(rezultate[2], 2)))
    colors = ['magenta', 'yellow', 'orange']
    for i in range(len(rezultate)):
        plt.plot(rezultate[i], 0, marker='o', color=colors[i])  # plotam punctul daca exista


def iterate_intervals():
    intervals = [(-5,-3.5),(-2.5,-1.9),(0,5)]
    """
    Pentru a aplica metoda pozitiei false este necesar ca:
    f(a)*f(b)<0
    f' si f'' nu se anuleaza pe a,b
    functia f este X**3 + 5*X**2 +2*X - 8
    functia f' este 3*X**2 + 10*X + 2 cu solutiile -3.11 si -0.22
    functia f'' este 6*X + 10 cu solutia -1.67
    
    Primul interval:
    f(-5) = -18
    f(-3.5) = 3.375
    Produsul f(-5)*f(-3.5) este negativ
    f' este descrescatoare 
    f'' este crescatoare
    
    Al doilea interval interval:
    f(-2.5) = 12.625
    f(-0.2) = -7.4
    Produsul f(-5)*f(-3.5) este negativ
    f' este crescatoare 
    f'' este crescatoare
    
    Primul interval:
    f(0) = -8
    f(5) = 252
    Produsul f(0)*f(5) este negativ
    f' este crescatoare 
    f'' este crescatoare
    """
    rezultate = []
    iteratii = []
    for i in range(len(intervals)): # iteram prin intervalele date
        a,b = intervals[i][0], intervals[i][1]
        rezultat, N = pozitie_falsa(func_f,a,b,1e-5)# cautam acel c din intervalul (a,b) astfel incat f(c) sa fie egal cu 0, la o marja de eroara mai mica de 1e-5
        if rezultat!=None:
            rezultate.append(rezultat)
            iteratii.append(N)
        else:
            print("Din pacate, nu exista o solutie in intervalul dat :(")
    create_plot_context(rezultate, iteratii)

def three():
    iterate_intervals()
    plt.show()

#4
def f_(x:float):
    """ Functia data. """
    return x**3 + x**2 - 6*x

def df_(x:float):
    """ Derivata functiei date. """
    return 3*x**2 + 2*x - 6

def secanta(f, a:float, b:float, x0:float, x1:float, eps:float):
    k = 1
    x0 = random.uniform(a, b)
    x1 = random.uniform(a, b)
    x2 = None
    N = 0

    def run_step_2(N, a, b, x0, x1, eps):
        N+=1
        if abs(f_(x1) - f_(x0)) < eps:
            return x1, N
        x2 = (x0 * f_(x1) - x1 * f_(x0)) / (f_(x1) - f_(x0))
        if x2 < a or x2 > b:
            x0 = random.uniform(a, b)
            x1 = random.uniform(a, b)
            x0, x1 = min(x0, x1), max(x0, x1)
            if abs(f_(x1) - f_(x0)) < eps:
                return x1, N
            x2 = (x0 * f_(x1) - x1 * f_(x0)) / (f_(x1) - f_(x0))
        return x2, N

    while abs(x1 - x0) >= eps * abs(x0):
        x2, N = run_step_2(N, a, b, x0, x1, eps)
        x0 = x1
        x1 = x2

    x_aprox = x2
    return x_aprox, N

def plot_function(callback_function, a, b, rezultate, iteratii):
    x_ = np.linspace(a, b, 100)  # Discretizare interval [a, b]
    y_ = callback_function(x_)  # Valorile functiei pe discretizarea intervalului

    plt.figure(0)
    plt.plot(x_, y_, linestyle='-', linewidth=3,
             c='orange')  # Plotarea functiei
    plt.axvline(0, c='black')  # Adauga axa OY
    plt.axhline(0, c='black')  # Adauga axa OX
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(b=True)
    plt.axis('scaled')
    plt.title("Metoda secantei dupa " + str(iteratii[0]) + "," + str(iteratii[1])+ ", respectiv "+ str(iteratii[2]) + " iteratii pentru solutiile: "+ str(round(rezultate[0],2)) + "," + str(round(rezultate[1],2)) + ", respectiv "+ str(round(rezultate[2],2)))
    colors = ['magenta', 'yellow', 'orange']
    for i in range(len(rezultate)):
        plt.plot(rezultate[i], 0, marker='o',color=colors[i])  # plotam punctul daca exista
    plt.show()


def iterate_intervals_secant():
    intervals = [(-5, -2), (-0.1, 1), (1.5, 5)]
    """
    Pentru a aplica metoda pozitiei false este necesar ca:
    f(a)*f(b)<0
    f' si f'' nu se anuleaza pe a,b
    functia f este X**3 + X**2 - 6*X
    functia f' este 3*X**2 + 2*X - 6 cu solutiile -1.78, 1.11
    functia f'' este 6*X + 2 cu solutia -0.33

    Primul interval:
    f(-5) = -70
    f(-2) = 8
    Produsul f(-5)*f(-3.5) este negativ
    f' este descrescatoare 
    f'' este crescatoare

    Al doilea interval interval:
    f(-1) = 6
    f(1) = -4
    Produsul f(-1)*f(1) este negativ
    f' este crescatoare 
    f'' este crescatoare

    Al treilea interval:
    f(-1.5) = -3.375
    f(5) = 120
    Produsul f(0)*f(5) este negativ
    f' este crescatoare 
    f'' este crescatoare
    """
    rezultate = []
    iteratii = []
    for i in range(len(intervals)):  # iteram prin intervalele date
        a, b = intervals[i][0], intervals[i][1]
        rezultat, N = secanta(f_, a, b,a , b, 1e-5)  # cautam acel c din intervalul (a,b) astfel incat f(c) sa fie egal cu 0, la o marja de eroara mai mica de 1e-5
        print("Rezultat pe intervalul ",a,b,rezultat)
        if rezultat != None:
            rezultate.append(rezultat)
            iteratii.append(N)
        else:
            print("Din pacate, nu exista o solutie in intervalul dat :(")
    plot_function(f_, -3, 3, rezultate, iteratii)

def four():
    iterate_intervals_secant()
    plt.show()

#one()
#two()
#three()
#four()