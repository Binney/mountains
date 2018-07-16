import sys
from .theme import Theme

class Screen:
  def __init__(self, dimensions):
    self._theme = Theme()
    self._height = dimensions.height
    self._screen = [[self._theme.get_sky_colour() for i in range(dimensions.width)] for j in range(dimensions.height)]

  def render(self, map):
    self._screen = [self._theme.get_sky_colour() * len(row) for row in self._screen]

    trees = map.render()
    for i in range(len(trees)):
        for j in range(trees[i], self._height):
            self._screen[j][i] = self._theme.get_tree_colour()

    rendered = "".join("".join("".join(cell) for cell in row) for row in self._screen)
    sys.stdout.write(rendered)
    sys.stdout.flush()
