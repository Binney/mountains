import argparse
import sys
import time
from .screen import Screen
from .map import Map

class Game:
  def __init__(self, dimensions):
    self.map = Map(dimensions)
    self.screen = Screen(dimensions)

  def run(self):
    sys.stdout.write('READY\n')
    sys.stdout.flush()

    last_tick = time.time()
    while True:
      line = sys.stdin.readline()
      if line.strip() == 'SKILL':
        exit()
      elif line.strip() == 'STICK':
        if (time.time() - last_tick > 0.2):
          self.map.advance()
        self.screen.render(self.map)
      elif line[0] == 'P':
        # TODO more user input?
        if line[2:5] == 'FB1':
          exit()
