from vector import Vector2D

class LineSegment:

    def __init__(self, v1, v2):
        self.v1= v1
        self.v2= v2

    def __str__(self):
        return str(v1)+"-"+str(v2)


    def calculate_distance(self,vector):
        d1= (v1.get_substracted(vector)).mag()
        d2= (v2.get_substracted(vector)).mag()

        return d1+d2






v1= Vector2D(1,1)
v2= Vector2D(3,3)
v3= Vector2D(2,2)

print(v1)
print(v2)

l1= LineSegment(v1,v2)

print(l1)

print(l1.calculate_distance(v3))