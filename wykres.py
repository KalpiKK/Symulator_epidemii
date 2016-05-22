import numpy as nu
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# WYKRES
# Funkcja rysujaca wykres, na podstawie wprowadzonych danych -  beta, gamma, ilosc populacji, ilosci zainfekowanych, czas.
# Zalozenia:
# - liczebnosc populacji jest stala
# - beta > gamma, w innym przypadku nie jest to przypadek epidemii,
# - kazdy typ osobnika ma rowne szanse spotkania osobnika innego typu.

def wykres():

    q = 0;
    p = 0;

    while q == 0:
        beta = float(raw_input("Podaj wartosc bety (predkosc rozprzestrzenania sie epidemii, beta > gamma): "))
        gamma = float(raw_input("Podaj wartosc gamma (predkosc zdrowienia populacji, beta > gamma): "))
        if beta > gamma:
            q = 1
        else:
            print 'Nieprawidlowe dane! (beta > gamma; liczby zmiennoprzecinkowe)'
            q = 0

    while p == 0:
        N = int(raw_input("Podaj liczebnosc populacji: "))
        x = int(raw_input("Podaj poczatkowa ilosc zaifekowanych: "))
        if N > x:
            p = 1
        else:
            print 'Nieprawidlowe dane! (N > x; liczby calkowite)'
            p = 0

    czas = int(raw_input("Podaj czas trwania obserwacji epidemii: "))

    def funkcja(u, t):

    # u = [S(t), I(t), R(t)]

        z = nu.zeros((3,)) #stworzenie listy wypelnionej 3 zerami

        # rozwiazanie rownania modelu SIR
        z[0] = -beta * u[0] * u[1]/ N
        z[1] = beta * u[0] * u[1]/ N - gamma * u[1]
        z[2] = gamma * u[1]
        return z

    # poczatkowe wartosci [S0,I0,R0]
    u0 = nu.array([N-x, x, 0.0])

    # krok czasu
    t = nu.linspace(0, czas, czas * 0.05)

    #ODE dy/dt = func(y, t0, ...) -> odeint(func,y0,t), rozwiazuje rownanie rozniczkowe modelu SIR
    u = odeint(funkcja, u0, t)

    # plot

    fig = plt.figure()
    plt.plot(t, u[:,0], label='S(t) - zdrowe', color='grey')
    plt.plot(t, u[:,1], label='I(t) - zainfekowane', color='red')
    plt.plot(t, u[:,2], label='R(t) - ozdrowiale', color='blue')
    plt.xlabel('Czas [t]')
    plt.ylabel('S/I/R')
    plt.legend(loc='center right')
    plt.grid()
    plt.savefig('sir.png', format='png')
    plt.show()

