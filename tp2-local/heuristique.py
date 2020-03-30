from algorithms import Algorithm
from glouton import Glouton
from interfaces import Pattern, Finger_cost
import time
import random

class Heuristique(Algorithm):
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
    self.apply_heur()

  def apply_heur(self):
    start_time = time.time()

    Glouton(self.path)
    array_current_costs = []
    # le cout final de la solution gloutonne
    # final_cost = g.cost_cost
    final_cost = self.get_total_cost()
    t = int((self.length_exemplary * 10) / 100)
    i = 1
    while i < t:
      r = random.randint(1, t)
      old_finger = self.fingers_transitions[r]
      before_old_finger = self.fingers_transitions[r - 1]
      after_old_finger = self.fingers_transitions[r + 1]

      first_old_cost= int(self.transitions_costs[int(self.notes[r-1])][before_old_finger][int(self.notes[r])][old_finger])
      second_old_cost= int(self.transitions_costs[int(self.notes[r])][old_finger][int(self.notes[r+1])][after_old_finger])
      old_current_total_cost = first_old_cost + second_old_cost

      for j in range(5):
        if j != old_finger:
          first_new_cost = int(self.transitions_costs[int(self.notes[r-1])][before_old_finger][int(self.notes[r])][j])
          second_new_cost = int(self.transitions_costs[int(self.notes[r-1])][j][int(self.notes[r])][after_old_finger])
          new_current_total_cost = first_new_cost + second_new_cost
          f_c = Finger_cost(j, new_current_total_cost)
          array_current_costs.append(f_c)

      new_min = min([k.cost for k in array_current_costs])
      if(new_min < old_current_total_cost):
        for l in array_current_costs:
          if l.cost == new_min:
            self.fingers_transitions[r] = l.finger
            final_cost = final_cost - old_current_total_cost + l.cost
            break

      array_current_costs.clear()
      i += 1

    elapsed_time = (time.time() - start_time) * 1000
    self.array_patterns[0] = Pattern(self.length_exemplary, round(elapsed_time, 4), final_cost)
    # self.array_patterns.append(Pattern(self.length_exemplary, round(elapsed_time, 4), final_cost))

