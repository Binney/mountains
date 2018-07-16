import sys
from random import randint

class Map:
  def __init__(self, dimensions):
    self._width = dimensions.width
    self._height = dimensions.height
    self._map = self.setup(dimensions.width, dimensions.height)

  def setup(self, width, height):
    newmap = [0 for i in range(width)]
    newmap[0] = height - 5
    for i in range(1, width - 1):
      newmap[i] = newmap[i - 1] + randint(-2, 2)
    return newmap

  def advance(self):
    for x in range(self._width - 2):
      self._map[x] = self._map[x + 1]

    self._map[self._width - 1] = self._map[self._width - 2] + randint(-2, 2)
    if self._map[self._width - 1] > self._height:
      self._map[self._width - 1] = self._height
    elif self._map[self._width - 1] < self._height - 20:
      self._map[self._width - 1] = self._height - 20

  def render(self):
    return self._map