import random

def genereaza_populatie_initiala(dimensiune_populatie, n_regine):
    """Generează o populație inițială pentru algoritmul genetic."""
    populatie = []
    for _ in range(dimensiune_populatie):
        individ = list(range(n_regine))
        random.shuffle(individ)
        populatie.append(individ)
    return populatie

def calculeaza_fitness(individ):
    """Calculează fitnessul unui individ."""
    fitness = 0
    n = len(individ)
    for i in range(n):
        for j in range(i+1, n):
            # Verifică dacă două regine sunt pe aceeași linie orizontală sau pe aceeași diagonală
            if individ[i] == individ[j] or abs(individ[i] - individ[j]) == j - i:
                fitness += 1
    return 1 / (fitness + 1)

def selecteaza_parinti(populatie, scoruri_fitness):
    """Selectează părinții pentru crossover pe baza scorurilor de fitness."""
    selectati = random.choices(populatie, weights=scoruri_fitness, k=2)
    return selectati[0], selectati[1]

def crossover(parinte1, parinte2):
    """Realizează crossover între doi părinți."""
    n = len(parinte1)
    punct_crossover = random.randint(1, n-1)
    copil1 = parinte1[:punct_crossover] + parinte2[punct_crossover:]
    copil2 = parinte2[:punct_crossover] + parinte1[punct_crossover:]
    return copil1, copil2

def mutatie(individ, rata_mutatie):
    """Aplică mutația unui individ."""
    n = len(individ)
    for i in range(n):
        # Verifică dacă va avea loc mutația pentru gena curentă
        if random.random() < rata_mutatie:
            j = random.randint(0, n-1)
            individ[i], individ[j] = individ[j], individ[i]
    return individ

def algoritm_genetic(n_regine, dimensiune_populatie, rata_mutatie, num_generatii):
    """Rezolvă problema N-Regine folosind un algoritm genetic."""
    populatie = genereaza_populatie_initiala(dimensiune_populatie, n_regine)

    for _ in range(num_generatii):
        scoruri_fitness = [calculeaza_fitness(individ) for individ in populatie]
        noua_populatie = []

        for _ in range(dimensiune_populatie // 2):
            parinte1, parinte2 = selecteaza_parinti(populatie, scoruri_fitness)
            copil1, copil2 = crossover(parinte1, parinte2)
            copil1 = mutatie(copil1, rata_mutatie)
            copil2 = mutatie(copil2, rata_mutatie)
            noua_populatie.extend([copil1, copil2])

        populatie = noua_populatie

    cel_mai_bun_individ = max(populatie, key=calculeaza_fitness)
    return cel_mai_bun_individ
