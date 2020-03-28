from algorithms import Algorithm
from glouton import Glouton
from dp import Dynamic_programming
from heuristique import Heuristique
import sys, time

def main():
  # AVERAGE : choose a folder
  # g = Glouton("./exemplaires")
  # g.get_averages()

  # f= open("solution.txt","w+")
  # f.write(g.path + "\n")
  # f.write("cost: " + str(g.array_patterns[0].transition_cost) + "\n")
  # f.write("time execution: " + str(g.array_patterns[0].elapsed_time) + "\n")
  # f.write("fingers solution: \n")
  # for i in g.fingers_transitions:
  #   f.write(str(i) + " ")
  # f.close

  ####################################################
  # start_time = time.time()

  algo = sys.argv[1]
  # path = "./exemplairess"
  # path = "./exemplaires"
  # path = "./exemplaires/ex_8000000_1.txt"
  # path = "./fur_elise.txt"
  path = "./twinkle_twinkle.txt"
  # path = "./exemplaires/ex_300000_1.txt"

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
