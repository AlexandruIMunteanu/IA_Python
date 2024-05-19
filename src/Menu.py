import Regine_backtracking_recursiv as rbk
import Regine_alg_alpinistului as raa
import Regine_alg_calirii_simulate as rcs
import Regine_alg_genetic as rag
import Comis_voiajorului_alg_celui_mai_apropiat_vecin as cvacmav
import Comis_voiajorului_backtracking_recursiv as cvbr
import matplotlib.pyplot as plt
import time

def frbkr():
    # Lista pentru stocarea timpilor de rezolvare
    times = []
    
    # Pentru fiecare dimensiune de la 10 la 22, cu pasul 2
    for i in range(10, 23, 2):
        # Înregistrarea timpului de început
        start_time = time.time()
        
        # Rezolvarea problemei reginelor folosind backtracking
        solution = rbk.solve_n_queens(i)
        
        # Înregistrarea timpului de sfârșit și calculul timpului total
        end_time = time.time()
        final_time = end_time - start_time
        
        # Adăugarea timpului la lista de timpi
        times.append(final_time)
        
        # Salvarea soluției într-un fișier txt
        with open(f"Regine_bkt_output_{i}.txt", "w") as file:
            for row in solution:
                file.write("|")
                for cell in row:
                    if cell == 1:
                        file.write(" Q |")  # Înlocuiește 1 cu "Q" în fișier
                    else:
                        file.write(" - |")  # Înlocuiește 0 cu "-" în fișier
                file.write("\n")
    
    # Salvarea timpilor de rezolvare într-un fișier txt
    with open("rbk_time_output.txt", "w") as file:
        for t in times:
            file.write(f"{t}\n")


def fraa():
    # Lista pentru stocarea timpilor de rezolvare
    times = []
    
    # Pentru fiecare dimensiune de la 10 la 22, cu pasul 2
    for i in range(10, 23, 2):
        # Înregistrarea timpului de început
        start_time = time.time()
        
        # Rezolvarea problemei reginelor folosind hill climbing
        solution = raa.hill_climbing(i)
        
        # Înregistrarea timpului de sfârșit și calculul timpului total
        end_time = time.time()
        final_time = end_time - start_time
        
        # Adăugarea timpului la lista de timpi
        times.append(final_time)
        
        # Salvarea soluției într-un fișier txt
        with open(f"Regine_hill_climbing_output_{i}.txt", "w") as file:
            for row in solution:
                file.write("|")
                for col in range(i):
                    if row == col:
                        file.write(" Q |")  # Plasează o regină pe poziția corectă
                    else:
                        file.write(" - |")  # Adaugă spațiu gol
                file.write("\n")
    
    # Salvarea timpilor de rezolvare într-un fișier txt
    with open("raa_time_output.txt", "w") as file:
        for t in times:
            file.write(f"{t}\n")


def frcs():
    # Inițializare contor pentru numărul de instanțe procesate
    k = 0
    # Lista pentru stocarea timpilor de rezolvare
    times = []

    # Deschiderea fișierului de intrare și citirea liniilor
    with open("rcs_input.txt", "r") as file:
        linii = file.readlines()

    # Procesarea datelor din fișierul de intrare
    date = []
    for linie in linii:
        date_linie = linie.strip().split(', ')
        date.append((int(date_linie[0]), float(date_linie[1]), float(date_linie[2])))

    # Pentru fiecare set de date
    for data in date:
        n, temp_initiala, rata_racire = data
        # Înregistrarea timpului de început
        start_time = time.time()
        # Aplicarea algoritmului de căutare locală (recalibrare simulată)
        stare, cost = rcs.calire_simulata(n, temp_initiala, rata_racire)
        # Înregistrarea timpului de sfârșit și calculul timpului total
        end_time = time.time()
        final_time = end_time - start_time
        # Adăugarea timpului la lista de timpi
        times.append(final_time)

        # Incrementarea contorului
        k += 1
        # Salvarea rezultatelor într-un fișier txt
        with open(f"Calire_simulata_output_{k}.txt", "w") as file:
            file.write("Starea finala a calirii simulata:\n")
            file.write(str(stare) + "\n")
            file.write("Costul starii finale: " + str(cost) + "\n")

    # Salvarea timpilor de rezolvare într-un fișier txt
    with open("rcs_time_output.txt", "w") as file:
        for t in times:
            file.write(f"{t}\n")

def frag():
    # Inițializare contor pentru numărul de instanțe procesate
    k = 1
    # Lista pentru stocarea timpilor de rezolvare
    times = []

    # Deschiderea fișierului de intrare și citirea liniilor
    with open("rag_input.txt", "r") as file:
        lines = file.readlines()

    # Pentru fiecare linie din fișierul de intrare
    for line in lines:
        data = line.strip().split()
        n_regine = int(data[0])
        dimensiune_populatie = int(data[1])
        rata_mutatie = float(data[2])
        num_generatii = int(data[3])

        # Înregistrarea timpului de început
        start_time = time.time()
        # Aplicarea algoritmului genetic
        cel_mai_bun_individ = rag.algoritm_genetic(n_regine, dimensiune_populatie, rata_mutatie, num_generatii)
        # Înregistrarea timpului de sfârșit și calculul timpului total
        end_time = time.time()
        final_time = end_time - start_time
        # Adăugarea timpului la lista de timpi
        times.append(final_time)

        # Salvarea rezultatelor într-un fișier txt
        with open(f"Algoritm_genetic_output_{k}.txt", "w") as file:
            file.write("Cel mai bun individ:\n")
            file.write(" ".join(map(str, cel_mai_bun_individ)) + "\n")
            file.write("Fitness: {}\n".format(rag.calculeaza_fitness(cel_mai_bun_individ)))
        # Incrementarea contorului
        k += 1

    # Salvarea timpilor de rezolvare într-un fișier txt
    with open("rag_time_output.txt", "w") as file:
        for t in times:
            file.write(f"{t}\n")



def plot_data_regine(file_paths, labels):
    # Culorile pentru fiecare algoritm
    colors = ['r', 'b', 'g', 'm']
    # Simbolurile pentru fiecare algoritm
    markers = ['o', 's', '^', 'd']
    
    # Pentru fiecare fișier și etichetă din listele date
    for i, file_path in enumerate(file_paths):
        with open(file_path, 'r') as file:
            # Extragem datele din fișier
            data = [float(line.strip()) for line in file]
        
        # Plasăm punctele pe grafic, cu culorile și simbolurile corespunzătoare
        plt.plot(data, color=colors[i], marker=markers[i], label=labels[i])

    # Setăm etichetele pe axa x
    plt.xticks(range(len(data)), ['10', '12', '14', '16', '18', '20', '22'])
    # Eticheta pentru axa x
    plt.xlabel('N')
    # Eticheta pentru axa y
    plt.ylabel('t (s)')
    # Titlul graficului
    plt.title('Reginele')
    # Adăugăm legenda
    plt.legend()
    # Afișăm graficul
    plt.show()

def fcvbr():
    # Inițializăm listele pentru grafuri și timpi
    graphs = []
    times = []
    
    # Citim datele din fișierul de intrare
    with open("cvbr_input.txt", 'r') as file:
        lines = file.readlines()
        index = 0
        while index < len(lines):
            line = lines[index].strip()
            # Trecem peste liniile goale
            if not line:
                index += 1
                continue
            try:
                num_cities = int(line)
            except ValueError as e:
                print(f"Error converting line to integer: {line}")
                index += 1
                continue
            index += 1
            # Construim matricea de adiacență pentru graful curent
            graph = []
            for _ in range(num_cities):
                line = lines[index].strip()
                if not line:
                    continue
                graph.append(list(map(int, line.split())))
                index += 1
            graphs.append(graph)
    
    # Scriem rezultatele în fișierul de ieșire
    with open("cvbr_output.txt", 'w') as file:
        for i, graph in enumerate(graphs):
            file.write(f"Procesarea grafului {i + 1}:\n")
            # Măsurăm timpul de început
            start_time = time.time()
            # Aplicăm algoritmul pentru problema comis-voiajorului
            min_cost, min_path = cvbr.tsp(graph)
            # Măsurăm timpul de sfârșit și calculăm durata totală
            end_time = time.time()
            final_time = end_time - start_time
            # Adăugăm timpul la lista de timpi
            times.append(final_time)
            # Scriem rezultatele în fișier
            file.write(f"Rezultate pentru graful {i + 1}:\n")
            file.write("Costul minim: " + str(min_cost) + "\n")
            file.write("Traseul minim: " + str(min_path) + "\n\n")

    # Scriem timpul de execuție în fișierul de ieșire
    with open("cvbr_time_output.txt", "w") as file:
        for t in times:
            file.write(f"{t}\n")


def fcvacmav():
    # Inițializăm listele pentru grafuri și timpi
    graphs = []
    times = []
    
    # Citim datele din fișierul de intrare
    with open("cvacmav_input.txt", 'r') as file:
        lines = file.readlines()
        index = 0
        while index < len(lines):
            line = lines[index].strip()
            # Trecem peste liniile goale
            if not line:
                index += 1
                continue
            try:
                num_cities = int(line)
            except ValueError as e:
                print(f"Error converting line to integer: {line}")
                index += 1
                continue
            index += 1
            # Construim matricea de adiacență pentru graful curent
            graph = []
            for _ in range(num_cities):
                line = lines[index].strip()
                if not line:
                    continue
                graph.append(list(map(int, line.split())))
                index += 1
            graphs.append(graph)
    
    # Scriem rezultatele în fișierul de ieșire
    with open("cvacmav_output.txt", 'w') as file:
        for i, graph in enumerate(graphs):
            start = 0
            file.write(f"Procesarea grafului {i + 1}:\n")
            # Măsurăm timpul de început
            start_time = time.time()
            # Aplicăm algoritmul vecinului cel mai apropiat pentru problema comis-voiajorului
            min_path = cvacmav.nearest_neighbor(graph, start)
            # Măsurăm timpul de sfârșit și calculăm durata totală
            end_time = time.time()
            final_time = end_time - start_time
            # Adăugăm timpul la lista de timpi
            times.append(final_time)
            # Scriem rezultatele în fișier
            file.write(f"Rezultate pentru graful {i + 1}:\n")
            file.write("Traseul minim: " + str(min_path) + "\n\n")

    # Scriem timpul de execuție în fișierul de ieșire
    with open("cvacmav_time_output.txt", "w") as file:
        for t in times:
            file.write(f"{t}\n")


def plot_data_comis_voiajor(file_paths, labels):
    # Culorile pentru fiecare algoritm
    colors = ['r', 'g' ]
    # Simbolurile pentru fiecare algoritm
    markers = ['o', 's']
    
    # Pentru fiecare fișier și etichetă din listele date
    for i, file_path in enumerate(file_paths):
        with open(file_path, 'r') as file:
            data = [float(line.strip()) for line in file]
        # Plasăm punctele pe grafic, cu culorile și simbolurile corespunzătoare
        plt.plot(data, color=colors[i], marker=markers[i], label=labels[i])

    # Setăm etichetele pe axa x
    plt.xticks(range(len(data)), ['1','2','3','4','5'])
    # Eticheta pentru axa x
    plt.xlabel('Nr. Teste')
    # Eticheta pentru axa y
    plt.ylabel('t (s)')
    # Titlul graficului
    plt.title('Comis-voiajorul')
    # Adăugăm legenda
    plt.legend()
    # Afișăm graficul
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
            plot_data_regine(file_paths, labels)

            pass
        elif optiune == "6":
            fcvbr()
            pass
        elif optiune == "7":
            fcvacmav()
            pass
        elif optiune == "8":
            # Definim calea către fiecare fișier și etichetele corespunzătoare pentru legenda
            file_paths_cv = ['cvbr_time_output.txt', 'cvacmav_time_output.txt']  # Adaugă căile pentru fișierele comis-voiajorului
            labels_cv = ['cvbr', 'cvacmav']  # Adaugă etichetele pentru graficul comis-voiajorului

            # Apelăm funcția pentru a plota datele pentru problema comis-voiajorului
            plot_data_comis_voiajor(file_paths_cv, labels_cv)
            pass
        elif optiune == "9":
            print("DavDev 3111a - Artificial Intelligence")
            pass
        elif optiune == "0":
            break
        else:
            print("Optiune invalida. Te rog alege o optiune din meniu.")

if __name__ == "__main__":
    main()
