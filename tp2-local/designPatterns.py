from algorithms import Algorithm
from glouton import Glouton
from dp import Dynamic_programming
from heuristique import Heuristique
import sys, time

def main():

  path = sys.argv[2]
  algo = sys.argv[4]
  # path = "./exemplairess"
  # path = "./exemplaires"
  # path = "./exemplaires/ex_8000000_1.txt"
  # path = "./fur_elise.txt"
  # path = "./twinkle_twinkle.txt"
  # path = "./exemplaires/ex_300000_1.txt"
  print(algo)

  if algo == "glouton":
    g = Glouton(path)
    # g.get_averages("glouton")
    g.display_path()
    g.display_total_cost()
    g.display_time_execution()
    # g.display_solution()
  elif algo == "dp":
    dp = Dynamic_programming(path)
    # dp.get_averages("dp")
    # dp.display_path()
    # dp.display_total_cost()
    # dp.display_time_execution()
    # dp.display_solution_dp()
  elif algo == "heuristique":
    heur = Heuristique(path)
    heur.get_averages("heuristique")
    # heur.display_path()
    # heur.display_total_cost()
    # heur.display_time_execution()
    # heur.display_solution()

if __name__ == '__main__':
    main()
