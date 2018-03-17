import beginner

class Intermediate(beginner.Beginner):

  def getExperiencePoint(self) :
    return self.experience * 2

my = Intermediate(100)
print (my.getExperiencePoint())  

my.point = 1000
print(my.point)