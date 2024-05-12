import Regine_backtracking_recursiv as rbk
import Regine_alg_alpinistului as raa
import Regine_alg_calirii_simulate as rcs
import Regine_alg_genetic as rg
import Comis_voiajorului_alg_celui_mai_apropiat_vecin as cvcmav
import Comis_voiajorului_backtracking_recursiv as cvbr

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
      # Implementați rezolvarea problemei N regine cu backtracking recursiv
      rbk.solve_n_queens(8)
      pass
    elif optiune == "2":
      # Implementați rezolvarea problemei N regine cu algoritmul alpinistului
      raa.hill_climbing(8)
      pass
    elif optiune == "3":
      # Implementați rezolvarea problemei N regine cu algoritmul calirii simulate
      rcs.calire_simulata(8)
      pass
    elif optiune == "4":
      # Implementați rezolvarea problemei N regine cu algoritmul genetic
      rg.algoritm_genetic(8)
      pass
    elif optiune == "5":
      # Implementați funcția de afișare a graficelor pentru problema N regine

      pass
    elif optiune == "6":
      # Implementați rezolvarea problemei comis-voiajorului cu backtracking recursiv
      pass
    elif optiune == "7":
      # Implementați rezolvarea problemei comis-voiajorului cu algoritmul celui mai apropiat vecin
      pass
    elif optiune == "8":
      # Implementați funcția de afișare a graficelor pentru problema comis-voiajorului
      pass
    elif optiune == "9":
      # Afișați informații despre program
      print("DavDev 3111a - Artificial Intelligence")
      pass
    elif optiune == "0":
      # Ieșiți din program
      break
    else:
      print("Opțiune invalidă. Te rog alege o opțiune din meniu.")

if __name__ == "__main__":
  main()
