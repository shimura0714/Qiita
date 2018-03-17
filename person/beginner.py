class Beginner ():

  @property
  def point(self):
    return self._point

  @point.setter
  def point(self, value):
    self._point = value

  def __init__(self, point):
    self.experience = point 
  
  def  getExperiencePoint(self):
    return self.experience
