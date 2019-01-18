"""
a cosmos has a universe or a multiverse
"""
from cosmograph.Base import Base
from cosmograph.Multiverse import Multiverse

class Cosmos(Base):
  def __init__(self, multiverse = None):
    self._multiverse = multiverse

  def get_multiverse(self):
    return self._multiverse
