import random

def genereaza_populatie_initiala(dimensiune_populatie, n_regine):
    """Genereaza o populatie initiala pentru algoritmul genetic."""
    populatie = []
    for _ in range(dimensiune_populatie):
        individ = list(range(n_regine))
        random.shuffle(individ)  # Amesteca pozitiile reginelor pentru a obtine un individ aleator
        populatie.append(individ)
    return populatie

def calculeaza_fitness(individ):
    """Calculeaza fitnessul unui individ."""
    fitness = 0
    n = len(individ)
    for i in range(n):
        for j in range(i+1, n):
            # Verifica daca doua regine sunt pe aceeasi linie orizontala sau pe aceeasi diagonala
            if individ[i] == individ[j] or abs(individ[i] - individ[j]) == j - i:
                fitness += 1
    return 1 / (fitness + 1)  # Returneaza inversul sumei conflictelor, cu 1 adaugat pentru a evita impartirea la 0

def selecteaza_parinti(populatie, scoruri_fitness):
    """Selecteaza parintii pentru crossover pe baza scorurilor de fitness."""
    selectati = random.choices(populatie, weights=scoruri_fitness, k=2)  # Alege 2 parinti cu probabilitatea data de scorurile de fitness
    return selectati[0], selectati[1]

def crossover(parinte1, parinte2):
    """Realizeaza crossover intre doi parinti."""
    n = len(parinte1)
    punct_crossover = random.randint(1, n-1)  # Alege un punct de crossover intre 1 si lungimea individului - 1
    copil1 = parinte1[:punct_crossover] + parinte2[punct_crossover:]  # Creeaza primul copil combinand parti din cei doi parinti
    copil2 = parinte2[:punct_crossover] + parinte1[punct_crossover:]  # Creeaza al doilea copil combinand parti din cei doi parinti
    return copil1, copil2

def mutatie(individ, rata_mutatie):
    """Aplica mutatia unui individ."""
    n = len(individ)
    for i in range(n):
        # Verifica daca va avea loc mutatia pentru gena curenta
        if random.random() < rata_mutatie:
            j = random.randint(0, n-1)
            individ[i], individ[j] = individ[j], individ[i]  # Schimba pozitia a doua gene aleator din individ
    return individ

def algoritm_genetic(n_regine, dimensiune_populatie, rata_mutatie, num_generatii):
    """Rezolva problema N-Regine folosind un algoritm genetic."""
    populatie = genereaza_populatie_initiala(dimensiune_populatie, n_regine)

    with open("Algoritm_genetic_output.txt", "w") as file:
        for i in range(num_generatii):
            scoruri_fitness = [calculeaza_fitness(individ) for individ in populatie]  # Calculeaza scorurile de fitness pentru fiecare individ din populatie
            noua_populatie = []

            for _ in range(dimensiune_populatie // 2):
                parinte1, parinte2 = selecteaza_parinti(populatie, scoruri_fitness)  # Selecteaza doi parinti pentru crossover
                copil1, copil2 = crossover(parinte1, parinte2)  # Realizeaza crossover intre cei doi parinti
                copil1 = mutatie(copil1, rata_mutatie)  # Aplica mutatia primului copil
                copil2 = mutatie(copil2, rata_mutatie)  # Aplica mutatia celui de-al doilea copil
                noua_populatie.extend([copil1, copil2])  # Adauga cei doi copii in noua populatie

            populatie = noua_populatie  # Actualizeaza populatia

            cel_mai_bun_individ = max(populatie, key=calculeaza_fitness)  # Alege cel mai bun individ din populatie

            file.write(f"Generatia {i+1}: {cel_mai_bun_individ}, Fitness: {calculeaza_fitness(cel_mai_bun_individ)}\n")

    cel_mai_bun_individ = max(populatie, key=calculeaza_fitness)  # Alege cel mai bun individ din ultima populatie
    return cel_mai_bun_individ  # Returneaza cel mai bun individ gasit