"""
A location contains a reference to the base class of the plane type;
this enables the lookup of places via plane-specific syntax
"""

class Location:
  BASE_CLASS=None

  def __init__(self, baseclass):
    self.BASE_CLASS=baseclass

  def resolve(self):
    pass
