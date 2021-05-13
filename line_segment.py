from vector import Vector2D

class LineSegment:

    def __init__(self, v1, v2):
        self.v1= v1
        self.v2= v2

    def __str__(self):
        return str(self.v1)+"-"+str(self.v2)


    def calculate_distance(self,vector):
        d1= (self.v1.get_substracted(vector)).mag()
        d2= (self.v2.get_substracted(vector)).mag()

        return d1+d2






