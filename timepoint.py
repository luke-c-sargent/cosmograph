"""
Time: like location, contains a reference to a plane which has its own time management system
"""

class Timepoint:
  BASE_CLASS=None

  def __init__(self, baseclass):
    self.BASE_CLASS = baseclass
