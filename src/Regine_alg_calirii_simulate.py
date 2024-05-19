import random
import math

def stare_initiala(n):
    """Genereaza o stare initiala aleatoare."""
    stare = list(range(n))
    random.shuffle(stare)  # Amesteca pozitiile reginelor initial
    return stare

def calculeaza_cost(stare):
    """Calculeaza costul unei stari."""
    cost = 0
    n = len(stare)
    for i in range(n):
        for j in range(i+1, n):
            # Verifica daca doua regine sunt pe aceeasi linie orizontala sau pe diagonala
            if stare[i] == stare[j] or abs(stare[i] - stare[j]) == j - i:
                cost += 1
    return cost

def obtine_vecin(stare):
    """Obtine un vecin al starii curente."""
    vecin = stare.copy()
    i = random.randint(0, len(stare)-1)
    j = random.randint(0, len(stare)-1)
    vecin[i], vecin[j] = vecin[j], vecin[i]  # Schimba aleator doua pozitii ale reginelor
    return vecin

def calire_simulata(n, temp_initiala, rata_racire):
    """Aplica algoritmul de calire simulata."""
    stare_curenta = stare_initiala(n)  # Starea initiala cu pozitiile reginelor
    cost_curent = calculeaza_cost(stare_curenta)  # Costul starii initiale
    cea_mai_buna_stare = stare_curenta.copy()  # Cel mai bun aranjament de regine gasit
    cea_mai_bun_cost = cost_curent  # Cel mai mic cost gasit

    temperatura = temp_initiala  # Temperatura initiala
    while temperatura > 0.1:  # Continua pana la o temperatura suficient de scazuta
        vecin = obtine_vecin(stare_curenta)  # Genereaza un vecin al starii curente
        cost_vecin = calculeaza_cost(vecin)  # Calculeaza costul vecinului

        delta = cost_vecin - cost_curent  # Diferenta de cost intre vecin si starea curenta
        probabilitate = math.exp(-delta / temperatura)  # Probabilitatea de acceptare a vecinului

        if delta < 0 or random.random() < probabilitate:
            stare_curenta = vecin  # Accepta vecinul daca are un cost mai mic sau cu o anumita probabilitate
            cost_curent = cost_vecin

        if cost_curent < cea_mai_bun_cost:
            cea_mai_buna_stare = stare_curenta.copy()  # Actualizeaza cea mai buna stare daca se gaseste una mai buna
            cea_mai_bun_cost = cost_curent

        temperatura *= rata_racire  # Racirea treptata a temperaturii

    return cea_mai_buna_stare, cea_mai_bun_cost  # Returneaza cea mai buna stare si costul asociat