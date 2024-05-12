import random
import math

def stare_initiala(n):
    """Generează o stare inițială aleatoare."""
    stare = list(range(n))
    random.shuffle(stare)
    return stare

def calculeaza_cost(stare):
    """Calculează costul unei stări."""
    cost = 0
    n = len(stare)
    for i in range(n):
        for j in range(i+1, n):
            if stare[i] == stare[j] or abs(stare[i] - stare[j]) == j - i:
                cost += 1
    return cost

def obtine_vecin(stare):
    """Obține un vecin al stării curente."""
    vecin = stare.copy()
    i = random.randint(0, len(stare)-1)
    j = random.randint(0, len(stare)-1)
    vecin[i], vecin[j] = vecin[j], vecin[i]
    return vecin

def calire_simulata(n, temp_initiala, rata_racire):
    """Aplică algoritmul de recăldire simulată."""
    stare_curenta = stare_initiala(n)
    cost_curent = calculeaza_cost(stare_curenta)
    cea_mai_buna_stare = stare_curenta.copy()
    cea_mai_bun_cost = cost_curent

    temperatura = temp_initiala
    while temperatura > 0.1:
        vecin = obtine_vecin(stare_curenta)
        cost_vecin = calculeaza_cost(vecin)

        delta = cost_vecin - cost_curent
        probabilitate = math.exp(-delta / temperatura)

        if delta < 0 or random.random() < probabilitate:
            stare_curenta = vecin
            cost_curent = cost_vecin

        if cost_curent < cea_mai_bun_cost:
            cea_mai_buna_stare = stare_curenta.copy()
            cea_mai_bun_cost = cost_curent

        temperatura *= rata_racire

    return cea_mai_buna_stare
