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
      display_glouton_answer(Glouton(path), opt1, opt2, opt3)
    elif sys.argv[4] == "dp":
      display_dp_answer(Dynamic_programming(path), opt1, opt2, opt3)
    elif sys.argv[4] == "heuristique":
      display_heuristique_answer(Heuristique(path), opt1, opt2, opt3)
    else:
      print("Algorithme inconnu")
  else:
    print("Manque des arguments.")

def display_glouton_answer(g, opt1, opt2, opt3):
  if opt1 == "" and opt2 == "" and opt3 == "":
    print("Veuillez ajouter des arguments")
  elif opt2 == "" and opt3 == "":
    if opt1 == "-c":
      g.display_solution()
    elif opt1 == "-p":
      g.display_total_cost()
    elif opt1 == "-t":
      g.display_time_execution()
  elif opt3 == "":
    if opt1 == "-c" and opt2 == "-p":
      g.display_solution()
      g.display_total_cost()
    elif opt1 == "-c" and opt2 == "-t":
      g.display_solution()
      g.display_time_execution()
    elif opt1 == "-p" and opt2 == "-t":
      g.display_total_cost()
      g.display_time_execution()
    else:
      print("Veuillez entrer les arguments en ordre (-c -p OU -c -t OU -p -t)")
  else:
    if opt1 == "-c" and opt2 == "-p" and opt3 == "-t":
      g.display_solution()
      g.display_total_cost()
      g.display_time_execution()
    else:
      print("Veuillez entrer les arguments en ordre (-c -p -t)")

def display_dp_answer(dp, opt1, opt2, opt3):
  if opt1 == "" and opt2 == "" and opt3 == "":
    print("Veuillez ajouter des arguments")
  elif opt2 == "" and opt3 == "":
    if opt1 == "-c":
      dp.display_solution_dp()
    elif opt1 == "-p":
      dp.display_total_cost()
    elif opt1 == "-t":
      dp.display_time_execution()
  elif opt3 == "":
    if opt1 == "-c" and opt2 == "-p":
      dp.display_solution_dp()
      dp.display_total_cost()
    elif opt1 == "-c" and opt2 == "-t":
      dp.display_solution()
      dp.display_time_execution()
    elif opt1 == "-p" and opt2 == "-t":
      dp.display_total_cost()
      dp.display_time_execution()
    else:
      print("Veuillez entrer les arguments en ordre (-c -p OU -c -t OU -p -t)")
  else:
    if opt1 == "-c" and opt2 == "-p" and opt3 == "-t":
      dp.display_solution_dp()
      dp.display_total_cost()
      dp.display_time_execution()
    else:
      print("Veuillez entrer les arguments en ordre (-c -p -t)")

def display_heuristique_answer(heur, opt1, opt2, opt3):
  if opt1 == "" and opt2 == "" and opt3 == "":
    print("Veuillez ajouter des arguments")
  elif opt2 == "" and opt3 == "":
    if opt1 == "-c":
      heur.display_solution()
    elif opt1 == "-p":
      heur.display_total_cost()
    elif opt1 == "-t":
      heur.display_time_execution()
  elif opt3 == "":
    if opt1 == "-c" and opt2 == "-p":
      heur.display_solution()
      heur.display_total_cost()
    elif opt1 == "-c" and opt2 == "-t":
      heur.display_solution()
      heur.display_time_execution()
    elif opt1 == "-p" and opt2 == "-t":
      heur.display_total_cost()
      heur.display_time_execution()
    else:
      print("Veuillez entrer les arguments en ordre (-c -p OU -c -t OU -p -t)")
  else:
    if opt1 == "-c" and opt2 == "-p" and opt3 == "-t":
      heur.display_solution()
      heur.display_total_cost()
      heur.display_time_execution()
    else:
      print("Veuillez entrer les arguments en ordre (-c -p -t)")
if __name__ == '__main__':
    main()
