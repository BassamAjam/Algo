class Pattern:
  def __init__(self, length_exemplary, elapsed_time, transition_cost):
    self.length_exemplary = length_exemplary
    self.elapsed_time = elapsed_time
    self.transition_cost = transition_cost

class Finger_cost:
  def __init__(self, finger, cost):
    self.finger = finger
    self.cost = cost

class Two_fingers:
  def __init__(self, finger_one, finger_two, cost):
    self.finger_one = finger_one
    self.finger_two = finger_two
    self.cost = cost