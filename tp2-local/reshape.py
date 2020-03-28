import numpy as np
import os
import sys

def reshape():
  load_file = np.loadtxt('cout_transition.txt', dtype=int)
  cout_transition = load_file.reshape((24, 5, 24, 5))
  print(cout_transition)


if __name__ == '__main__':
    reshape()
