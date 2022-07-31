"""
class Cab:
    
   drivar_name = "Talha Aftab"
   Noofkm = 30
   pickup = "nazimabad"
   drop =   "North karachi"
   cap_fare = 3000
   Noofpassenger = 100
   
   
   def rateperkm(self):
       
             return  self.Noofkm / self.cap_fare
       
       
   
   def noofcabs(cls):
   
             return cls.Noofpassenger
        
    
   def avgnoofpassenger(cls, noofcabs):
        
              return noofcabs / cls.Noofpassenger
        
        
      

cab1 = Cab()
print(cab1.rateperkm())
print(cab1.noofcabs())
print(cab1.avgnoofpassenger(30))
"""

class shape:
    
    length = 0.0
    hieght = 0.0
        
    def Getdata(self, length , hieght):
        
        self.length = length
        self.hieght = hieght
        
    def DisplayArea():
            pass
        
class triangle(shape):
    
    def Getdata(self, length, hieght):
        self.length = length
        self.hieght = hieght
    
    def DisplayArea(self):
        return 1/2*self.length*self.hieght
    
class rectangle(shape):
    
    def Getdata(self, length, hieght):
        self.length = length
        self.hieght = hieght
        
    def DisplayArea(self):
        return self.length*self.hieght
    
    
t = triangle()
t.Getdata(4, 9)
print("Area of triangle :",t.DisplayArea())
r = rectangle()
r.Getdata(5, 10)
print("Area of Rectangle :",r.DisplayArea())
        
        




























