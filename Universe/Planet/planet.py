"""
a planet has certain characteristics (that may change over time?)
"""

class BasePlanet(Base):
  def __init__(self, properties, map):
    self.properties = properties
    self.map = map
    self.time = Time()
    
  def get_map(self, timepoint = None):
    if not timepoint:
      timepoint = self.NOW
    return self.map
