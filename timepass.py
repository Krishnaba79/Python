class car():
   def fuel(self):
        print("Fuel")
def ride(self):

         print("Ride")
    
def __init__(self,name,speed,color,model):
    self.name=name
    self.speed=speed
    self.color=color
    self.model=model
c1=car("Mercedes",250,"Red","G360")
c2=car("Kia",120,"Blue","Seltos")
c3=car("Supra",200,"Red","Sports")
c4=car("Mustang",190,"Blue","GT")
cars=[c1,c2,c3,c4]
for i in cars:
     print(i.name)


