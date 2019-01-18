from exceptions import AbstractUnimplemented, abstr

"""
A calendar for measuring the passage of time in the weird ways we do
"""

class Calendar:
  def __init__(self):
    pass

# default calendar class
class Gregorian(Calendar):
  MONTHS = {
    "January" : 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December" : 31
  }

  WEEKDAYS = ["Mon", "Tues", "Wednes", "Thurs", "Fri", "Satur", "Sun"]

  def __init__(self):
    pass

  def is_leap(self, year):
    if year % 4: # if not divisible by 4
      return 0
    elif year % 100: # if not divisible by 100
      return 1
    elif year % 400: # if not divisible by 400
      return 0
    else:
      return 1
