import numpy as np

# Aufgabe 2 - Hello World
print("----------------------------------------")
print("## Aufgabe 2 - Hello World")
print("Hello world")

# Aufgabe 3 -  Taschnenrechner
from math import sqrt, exp, log
print("----------------------------------------")
print("## Aufgabe 3 -  Taschnenrechner")
print("Nun kommen die Rechenaufgaben")
Taschenrechner = [5+5, 5.0 + 5.0, 5.0+4, 10/3, 10.0/3.0, sqrt(2), sqrt(2.0), \
                   exp(log(10)), (0.3-0.2-0.1), 2**3, not(4>3 and 100>6), \
                       True or False, "a" + "bc", 3*"bc"]
for eintrag in Taschenrechner:
    print(eintrag)

# Aufgabe 4  - Schleifen und Fallunterscheidungen
print("----------------------------------------")
print("## Aufgabe 4 - Schleifen und Fallunterscheidungen")

# Summe aller ganzer Zahlen zwischen 1 und 100
k = 0
for i in range(1,100+1): # oder sum(range(0,101))
    k += i
print("Summe aller ganzer Zahlen von 1 bis 100 =", k)

# Summe aller ungeraden ganzen Zahlen zwischen 1 und 100
k=0
for i in range(1,100+1,2): # oder sum(range(0,101,2))
    k += i
print("Summe aller ungeraden ganzen Zahlen zwischen 1 und 100 =",k)

# Summe aller Primzahlen zwischen 1 und 100
def Primes(Nmax):
    primzahlen = [2,3,5,7]
    for i in range(2,Nmax+1):
        if (i%2 != 0 and i%3!=0 and i%5!=0 and i%7!=0):
            # primzahlen = np.append(primzahlen, i)
            primzahlen.append(i)
    return primzahlen
            
print("Summe aller Primzahlen zwischen 1 und 100 ergibt:", sum(Primes(100))) 

# Primzahlen, aehnlich nur besser
def primeList(Nmax):
    """returns a list of prime numbers lower or equal Nmax."""
    primes = [2]
    for n in range(3,Nmax,2):
        for p in primes:
            if (n % p == 0):
                break
        else:
            primes.append(n)
    return primes
print(primeList(2))

# Berechnung der Fibonacci Zahlen < 1000
fibonacci = np.array([1,1])
while(fibonacci[-1]<=1000):
    fibonacci = np.append(fibonacci,fibonacci[-1]+fibonacci[-2])
print("Fibonacci Zahlen bis 1000: \n", fibonacci)

# Berechnung der Fibonacci Zahlen < 1000
fibonacci = [1,1]
fibo1 = fibonacci[-1]
while(fibo1<=1000):
    fibonacci.append(fibo1)
    fibo1 = fibonacci[-1]+fibonacci[-2]
print("Fibonacci Zahlen bis 1000: \n", fibonacci)

# äehnliche Variante
# Berechnung der Fibonacci Zahlen < 1000
def fiboless(N):
    fibonacci = [1]
    fibo0, fibo1 = (1,1)
    while(fibo1<=N):
        fibonacci.append(fibo1)
        fibo0, fibo1 = (fibo1,fibo0+fibo1)
    return fibonacci
print("Fibonacci Zahlen bis 1000: \n", fiboless(1000))

# print("Nun wird herausgefunden, ob eine Jahreszahl ein Schaltjahr war oder sein wird")
# while True:
#     Jahreszahl = int(input("Eingabe einer Jahreszahl:"))
#     if Jahreszahl%400==0:
#         print(Jahreszahl, "ist ein Schaltjahr!")
#     elif Jahreszahl%100==0:
#         print(Jahreszahl, "ist kein Schaltjahr!")
#     elif Jahreszahl%4==0:
#         print(Jahreszahl, " ist ein Schaltjahr!")
#     else:
#         print(Jahreszahl, " ist kein Schaltjahr!")

#
def checkLeapYear(year):
    """Evaluates if a given year is a leap year or not."""
    if (not(year % 4 == 0)):
        leapYear = False
    elif (not(year % 100 == 0)):
        leapYear = True
    elif (not(year % 400 == 0)):
        leapYear = False
    else:
        leapYear = True
    return leapYear

Jahr = 1900
print("Is %d a LeapYear?"%(Jahr))
print(checkLeapYear(Jahr))

# Aufgabe 5 (2018) - Satellit
print("-----------------------------")
print("# Aufgabe 5 (2018) - Satellit")

def heightSat(time):
    """
    Returns height of a satellite depending on its orbital period t around the earth
    """
    from math import pi
    # Konstanten
    G = 6.67E-11 # m^3/(kg*s^2) Gravitationskonstante
    M_earth = 5.97E+24  # kg          Erdmasse
    R_earth = 6371.E+3   # m          Erdradius
    
    height = ( (G*M_earth*time**2)/(4*pi**2) )**(1/3) - R_earth
    
    return height

def getInput(request):
    inputValue = input(request)
    return inputValue

sRequest = "Bitte geben Sie die Umlaufzeit des Satelliten in Sekunden ein: "
#time = float(getInput(sRequest))
time = 86400.
#time = float(input(sRequest))

# confirm the input
print("Die Umlaufzeit ist {t:.1f} s.".format(t=time))

# perform calculation
height = heightSat(time)
answer = "Die Höhe des Satelliten ist {h:.2E} m."
print(answer.format(h=height))

# Aufgabe 5  - Wurf
print("----------------------------------------")
g = 9.81 # m/(s^2) - Erdbeschleunigung
#h_turm = int(input("Eingabe der Turmhoehe: ")) # m - Turmhoehe
h_turm = 100.
t = sqrt(2*g*h_turm) # s - Zeit
print("Der Ball trifft den Boden nach ", t, "Sekunden")
print("----------------------------------------")

# Aufgabe 6 (2018) - Binomialkoeffizient
def binomial(n,k):
    """Diese Funktion berechnet den Binomialkoeffizienten
    """
    result = 1
    for i in range(1,k+1):
        #print((result*(n-i+1)), i, (result*(n-i+1))//i)
        result = (result*(n-i+1))//i
    return result

print("Binomialkoeffizient")
print(binomial(4,2))

# koeff = []
# n = 4
# for i in range(0,n+1):
#     for j in range(0,i+1):
#         koeff.append(binomial(i, j))
        
# for i in range(0,n+1):
#     for j in range(0,i+1):
#         print(koeff[i 
#         #print(binomial(i,j))
        
# Aufgabenteil b)
koeff = []
n = 10
for i in range(0,n+1):
    row = []
    for j in range(0,i+1):
        row.append(binomial(i, j))
    koeff.append(row)

for i in range(0,n+1):
    for j in range(0,i+1):
        print(koeff[i][j],end=" ",sep=" ")
    print() # new line
    
for i in range(i+1):
    print(koeff[i][0:i+1])

# Aufgabe 6  - Rekursion
print("----------------------------------------")
def fakultaet(n):
    """
    Diese Funktion berechnet die Fakultaet einer natuerlichen Zahl.
    """
    if n == 1:
        return 1
    else:
        return n*fakultaet(n-1)

print(fakultaet(4))

def ggT(m,n):
    """ Diese Funktion berechnet den groessten gemeinsamen Teiler zweier Zahlen.
    """
    if n == 0:
        return m
    else: 
        print("m =", m, "n =", n, "m mod n =", m%n)
        return ggT(n, m%n)
    
print("ggT von 108 und 192 ist: ", ggT(108,192))

def fibonacci(n):
    """Diese Funktion berechnet die ersten n Fibonacci Zahlen.
    """
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

import time
tt = time.time()       
a,b = [1,1]
N = 1000   
# Zwischenspeichern der Werte
for i in range(2,1000):
    a,b = [b, a+b]
print(b)
print ((time.time()-tt)*1000, "ms")
    

      

    

    
    


    



