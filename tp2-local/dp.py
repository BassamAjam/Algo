from algorithms import Algorithm
from interfaces import Pattern, Finger_cost, Two_fingers
import time

class Dynamic_programming(Algorithm):

  min_min = 0
  J = []

  def __init__(self, path):
    super().__init__(path)
    self.transitions_costs = super().get_transitions_costs()
    if ".txt" in path:
      self.run(path)
    else:
      self.read_files(super().get_all_exemplaries())

  def read_files(self,files):
    if len(files) != 0:
      for p in files:
        self.path = p
        self.run(p)

  def run(self, p):
    self.length_exemplary = super().read_first_line(p)
    self.notes = super().read_notes(p)
    self.apply_dynamic_programming()

  def initialize(self):
    # costs_possibilities =[int(self.transitions_costs[int(self.notes[i])][d_one][int(self.notes[i+1])][d_two]) + self.J[i+1][d_two] for d_two in range(5)]
    self.J.clear()
    self.fingers_transitions.clear()
    self.min_min = 0
    w , h = 5, self.length_exemplary
    self.J = [[0 for x in range(w)] for y in range(h)]
    self.fingers_transitions.append(0)

  def apply_dynamic_programming(self):
    start_time = time.time()
    self.initialize()
    costs_possibilities = []
    i = self.length_exemplary - 2
    while i >= 0:
      for d_one in range(5):
        for d_two in range(5):
          cost = int(self.transitions_costs[int(self.notes[i])][d_one][int(self.notes[i+1])][d_two]) + self.J[i+1][d_two]
          costs_possibilities.append(cost)

        min_cost = min(costs_possibilities)
        self.J[i][d_one] = min_cost
        costs_possibilities.clear()

      self.min_min = min(self.J[i])
      self.fingers_transitions.append(self.J[i].index(self.min_min))
      print("i:{}".format(i))
      i -= 1

    elapsed_time = (time.time() - start_time) * 1000
    self.array_patterns.append(Pattern(self.length_exemplary, round(elapsed_time, 4), self.min_min))