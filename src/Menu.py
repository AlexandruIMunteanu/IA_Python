import Regine_backtracking_recursiv as rbk
import Regine_alg_alpinistului as raa
import Regine_alg_calirii_simulate as rcs
import Regine_alg_genetic as rag
import Comis_voiajorului_alg_celui_mai_apropiat_vecin as cvcmav
import Comis_voiajorului_backtracking_recursiv as cvbr
import matplotlib.pyplot as plt
import time

def frbkr():
    times = []
    for i in range(4, 11, 2):
        start_time = time.time()
        solution = rbk.solve_n_queens(i)
        end_time = time.time()
        final_time = end_time - start_time
        times.append(final_time)
        
        with open(f"Regine_bkt_output_{i}.txt", "w") as file:
            for row in solution:
                file.write("|")
                for cell in row:
                    if cell == 1:
                        file.write(" Q |")
                    else:
                        file.write(" - |")
                file.write("\n")

    with open("rbk_time_output.txt", "w") as file:
        for t in times:
            file.write(f"{t}\n")

def fraa():
    times = []
    for i in range(4, 11, 2):
        start_time = time.time()
        solution = raa.hill_climbing(i)
        end_time = time.time()
        final_time = end_time - start_time
        times.append(final_time)
      
        with open(f"Regine_hill_climbing_output_{i}.txt", "w") as file:
            for row in solution:
                file.write("|")
                for col in range(i):
                    if row == col:
                        file.write(" Q |")
                    else:
                        file.write(" - |")
                file.write("\n")

    with open("raa_time_output.txt", "w") as file:
        for t in times:
            file.write(f"{t}\n")

def frcs():
    k = 0
    times = []

    with open("rcs_input.txt", "r") as file:
        linii = file.readlines()
  
    date = []
    for linie in linii:
        date_linie = linie.strip().split(', ')
        date.append((int(date_linie[0]), float(date_linie[1]), float(date_linie[2])))

    for data in date:
        n, temp_initiala, rata_racire = data
        start_time = time.time()
        stare, cost = rcs.calire_simulata(n, temp_initiala, rata_racire)
        end_time = time.time()
        final_time = end_time - start_time
        times.append(final_time)
  
        k += 1
        with open(f"Calire_simulata_output_{k}.txt", "w") as file:
            file.write("Starea finala a calirii simulata:\n")
            file.write(str(stare) + "\n")
            file.write("Costul starii finale: " + str(cost) + "\n")

    with open("rcs_time_output.txt", "w") as file:
        for t in times:
            file.write(f"{t}\n")

def frag():
    k = 1
    times = []

    with open("rag_input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split()
        n_regine = int(data[0])
        dimensiune_populatie = int(data[1])
        rata_mutatie = float(data[2])
        num_generatii = int(data[3])

        start_time = time.time()
        cel_mai_bun_individ = rag.algoritm_genetic(n_regine, dimensiune_populatie, rata_mutatie, num_generatii)
        end_time = time.time()
        final_time = end_time - start_time
        times.append(final_time)

        
        with open(f"Algoritm_genetic_output_{k}.txt", "w") as file:
            file.write("Cel mai bun individ:\n")
            file.write(" ".join(map(str, cel_mai_bun_individ)) + "\n")
            file.write("Fitness: {}\n".format(rag.calculeaza_fitness(cel_mai_bun_individ)))
        k += 1

    with open("rag_time_output.txt", "w") as file:
        for t in times:
            file.write(f"{t}\n")


def plot_data(file_paths, labels):
    colors = ['r', 'b', 'g', 'm']  # Culorile pentru fiecare algoritm
    markers = ['o', 's', '^', 'd']  # Simbolurile pentru fiecare algoritm
    for i, file_path in enumerate(file_paths):
        with open(file_path, 'r') as file:
            data = [float(line.strip()) for line in file]
        plt.plot(data, color=colors[i], marker=markers[i], label=labels[i])

    plt.xticks(range(len(data)), ['4', '6', '8', '10'])  # Setăm etichetele pentru axa x
    plt.xlabel('N')  # Eticheta pentru axa x
    plt.ylabel('t (s)')  # Eticheta pentru axa y
    plt.title('Reginele')  # Titlul graficului
    plt.legend()  # Adăugăm legenda
    plt.show()

def afisare_meniu():
    print("\nMENIU PRINCIPAL")
    print("1. Problema celor N regine (backtracking recursiv)")
    print("2. Problema celor N regine (alg. alpinistului)")
    print("3. Problema celor N regine (alg. calirii simulate)")
    print("4. Problema celor N regine (alg. genetic)")
    print("5. Plotare grafice problema celor N regine")
    print("6. Problema comis-voiajorului (backtrgacking recursiv)")
    print("7. Problema comis-voiajorului (alg. celui mai apropiat vecin)")
    print("8. Plotare grafice problema comis-voiajorului")
    print("9. Info")
    print("0. Exit")

def main():
    while True:
        afisare_meniu()
        optiune = input("Alegeti o optiune: ")

        if optiune == "1":
            frbkr()     
        elif optiune == "2":
            fraa()
        elif optiune == "3":
            frcs()
        elif optiune == "4":
            frag()
        elif optiune == "5":
            # Definim calea către fiecare fișier și etichetele corespunzătoare pentru legenda
            file_paths = ['rbk_time_output.txt', 'rcs_time_output.txt', 'raa_time_output.txt', 'rag_time_output.txt']
            labels = ['rbk', 'rcs', 'raa', 'rag']

            # Apelăm funcția pentru a plota datele
            plot_data(file_paths, labels)

            pass
        elif optiune == "6":
            pass
        elif optiune == "7":
            pass
        elif optiune == "8":
            pass
        elif optiune == "9":
            print("DavDev 3111a - Artificial Intelligence")
        elif optiune == "0":
            break
        else:
            print("Optiune invalida. Te rog alege o optiune din meniu.")

if __name__ == "__main__":
    main()
