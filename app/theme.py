class Theme:
  def __init__(self):
    self._sky_colour = ['\x00', '\xaa', '\xff']
    self._tree_colour = ['\x00', '\x00', '\x00']
  
  def get_sky_colour(self):
    return self._sky_colour
  
  def get_tree_colour(self):
    return self._tree_colour