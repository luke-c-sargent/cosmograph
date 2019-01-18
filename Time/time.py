"""
time has...a lot of shit. lets assume linear time and disregard einstein at first
no stop time == unknown amount of time in universe

"""

class Time(Base):
  def __init__(self):
    self.start = 0
    self.stop = None

class TimePoint():
