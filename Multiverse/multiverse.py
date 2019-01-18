from cosmograph.Universe import Universe

class Multiverse:
  def __init__(self, universes = []):
    self._universes = universes

  def get_universes(self):
    return self._universes
