class Circle:
    Id = 0
    radius = 0
    color = ""
    display = True

    def __init__(self,id,r,c,d):
        self.Id = id
        self.radius = r
        self.color = c
        self.display = d
    
    def circumfrence(self):
        return 3.141 * 2 * self.radius

circle1 = Circle(1,10,"Blue",True)

circle2 = Circle(2,8,"Yellow",True)

circle3 = Circle(3,17,"Red",False)

print("Circle 1 circumfence is: " + circle1.circumfrence())
print("Circle 2 circumfence is: " + circle2.circumfrence())
print("Circle 3 circumfence is: " + circle3.circumfrence())
