from exceptions import AbstractUnimplemented, abstr

"""
A Time System is a way of describing the passage of time; must accept timepoints with the same base class
"""

class TimeSystem:

  def __init__(self):
    abstr()

  def get_rate(self):
    pass

  def get_units(self):
    pass

class EarthTime(TimeSystem):
  UNITS = {
#    name    : seconds
    "minute" : 60,
    "hour"   : 60*60
    "day"    : 24*60*60
    "week"   : 7*24*60*60
}

  def __init__(self):
     pass

class Timeless(TimeSystem):
    pass
