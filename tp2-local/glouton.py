from algorithms import Algorithm
from interfaces import Pattern, Finger_cost
import time

class Glouton(Algorithm):
  def __init__(self, path):
    super().__init__(path)
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
    self.apply_glouton()

  def get_first_fingers(self):
    costs_possibilities = []
    min_cost = 0
    finger = 0

    for d_one in range(5):
      for d_two in range(5):
        f_c = Finger_cost(d_one, int(self.transitions_costs[int(self.notes[0])][d_one][int(self.notes[1])][d_two]))
        costs_possibilities.append(f_c)

    min_cost = min([i.cost for i in costs_possibilities])

    for c_p in costs_possibilities:
      if min_cost == c_p.cost:
        finger = c_p.finger
        break

    return finger

  def apply_glouton(self):
    start_time = time.time()

    costs_possibilities = []
    d_first = self.get_first_fingers()
    min_cost = 0
    total_cost = 0
    i = 0

    self.fingers_transitions.clear()
    self.fingers_transitions.append(d_first)

    while i < self.length_exemplary-1:
      for d_second in range(5):
        f_c = Finger_cost(d_second, int(self.transitions_costs[int(self.notes[i])][d_first][int(self.notes[i+1])][d_second]))
        costs_possibilities.append(f_c)

      min_cost = min([i.cost for i in costs_possibilities])
      total_cost += min_cost

      # choisir le doigt
      for c_p in costs_possibilities:
        if min_cost == c_p.cost:
          self.fingers_transitions.append(c_p.finger)
          d_first = c_p.finger
          break

      costs_possibilities.clear()

      i += 1

    elapsed_time = (time.time() - start_time) * 1000

    # Pour les calculs des moyennes
    # 1 <= len(array_patterns) <= 100
    self.array_patterns.append(Pattern(self.length_exemplary, round(elapsed_time, 4), total_cost))
