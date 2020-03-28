import numpy as np
import os
import sys
from interfaces import Pattern
from os import path

class Algorithm:
  path = ""
  files = []
  array_length_exemplaries = []

  array_patterns = []
  average_costs = 0
  average_time_execution = 0

  fingers_transitions = []

  def __init__(self, p):
    if path.exists(p):
      self.path = p
      self.reshape()
    else:
      print("Repertoire n'existe pas")
      sys.exit(1)

  def read_first_line(self, path):
    exemplary = open(path, "r")
    self.length_exemplary = int(exemplary.readline())

    if self.length_exemplary not in self.array_length_exemplaries:
      self.array_length_exemplaries.append(self.length_exemplary)
    exemplary.close()

    return self.length_exemplary

  def read_notes(self, path):
    exemplary = open(path, "r")
    for i, line in enumerate(exemplary):
      if i == 0:
        notes = exemplary.readline().split()
    exemplary.close()

    return notes

  def reshape(self):
    p = "cout_transition.txt"
    if path.exists(p):
      load_file = np.loadtxt(p, dtype=int)
      self.transitions_costs = load_file.reshape((24, 5, 24, 5))

  def get_transitions_costs(self):
    return self.transitions_costs

  def get_total_cost(self):
    return self.array_patterns[0].transition_cost

  def display_path(self):
    print(self.path)

  def display_total_cost(self):
    print(self.get_total_cost())

  def display_time_execution(self):
    print(self.array_patterns[0].elapsed_time)

  def display_solution(self):
    for i in self.fingers_transitions:
      print(i, end = ' ')

  def display_solution_dp(self):
    for j in self.fingers_transitions[::-1]:
      print(j, end = ' ')

##########################################################

  def get_all_exemplaries(self):
    for r, d, f in os.walk(self.path):
      for file in f:
          if '.txt' in file:
              self.files.append(os.path.join(r, file))

    return self.files

  def get_averages(self, algo_type):
    p = "averages.txt"
    if path.exists(p):
      os.remove(p)

    for l in self.array_length_exemplaries:
      for p in self.array_patterns:
        if p.length_exemplary == l:
          self.average_costs += p.transition_cost
          self.average_time_execution += p.elapsed_time

      self.average_costs = self.average_costs/10
      self.average_time_execution = round(self.average_time_execution/10, 4)
      self.write_in_file(l, algo_type)
      self.average_costs = 0
      self.average_time_execution = 0

  def write_in_file(self, l, algo_type):
    print("Algorithm type: {}".format(algo_type))
    print("Exemplary size: {}".format(l))
    print("Average costs: {}".format(self.average_costs))
    print("Average time execution: {}".format(self.average_time_execution))
    print("********************")

    with open("averages.txt", "a") as myfile:
      myfile.write("Algorithm type: " + str(algo_type) + "\n")
      myfile.write("Exemplary size: " + str(l) + "\n")
      myfile.write("Average costs: " + str(self.average_costs) + "\n")
      myfile.write("Average time execution: " + str(self.average_time_execution) + "\n")
      myfile.write("\n")
