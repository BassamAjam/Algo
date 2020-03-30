from algorithms import Algorithm
from glouton import Glouton
from dp import Dynamic_programming
from heuristique import Heuristique
import sys

def main():
  opt1, opt2, opt3 = "", "", ""
  l = len(sys.argv)

  if l >= 2:
    path = sys.argv[2]

  if l == 6:
    opt1 = sys.argv[5]
  elif l == 7:
    opt1 = sys.argv[5]
    opt2 = sys.argv[6]
  elif l == 8:
    opt1 = sys.argv[5]
    opt2 = sys.argv[6]
    opt3 = sys.argv[7]

  if l >= 5:
    if sys.argv[4] == "glouton":
      display_answer(Glouton(path), "glouton", opt1, opt2, opt3)
    elif sys.argv[4] == "dp":
      display_answer(Dynamic_programming(path), "dp", opt1, opt2, opt3)
    elif sys.argv[4] == "heuristique":
      display_answer(Heuristique(path), "heuristique", opt1, opt2, opt3)
    else:
      print("Algorithme inconnu")
  else:
    print("Manque des arguments.")

def display_answer(algo, type, opt1, opt2, opt3):
  if opt1 == "" and opt2 == "" and opt3 == "":
    print("Veuillez ajouter des argumentss")
    # g.get_averages()
  elif opt2 == "" and opt3 == "":
    if opt1 == "-c":
      algo.display_solution(type)
    elif opt1 == "-p":
      algo.display_total_cost()
    elif opt1 == "-t":
      algo.display_time_execution()
  elif opt3 == "":
    if opt1 == "-c" and opt2 == "-p":
      algo.display_solution(type)
      algo.display_total_cost()
    elif opt1 == "-c" and opt2 == "-t":
      algo.display_solution(type)
      algo.display_time_execution()
    elif opt1 == "-p" and opt2 == "-t":
      algo.display_total_cost()
      algo.display_time_execution()
    else:
      print("Veuillez entrer les arguments en ordre (-c -p OU -c -t OU -p -t)")
  else:
    if opt1 == "-c" and opt2 == "-p" and opt3 == "-t":
      algo.display_solution(type)
      algo.display_total_cost()
      algo.display_time_execution()
    else:
      print("Veuillez entrer les arguments en ordre (-c -p -t)")

if __name__ == '__main__':
    main()
