from vector import Vector2D


class Mover:

    def __init__(self,x:float,y:float,radius:int,mass:float):

        self.location= Vector2D(x,y)
        self.velocity= Vector2D(0,0)
        self.accelaration= Vector2D(0,0)
        self.radius= radius
        self.mass= mass
    
    def __init__(self, vector,velocity):
        self.location= vector
        self.radius= 7
        self.velocity= velocity
        self.accelaration= Vector2D(0,0)
        self.mass= 1
        self.in_bounds= False



        
    def applyForce(self,force:Vector2D):
        force_copy= force.copy()

        force_copy.div(self.mass)
        self.accelaration.add(force_copy)
        
       


    def update(self):
        self.velocity.add(self.accelaration)
        self.location.add(self.velocity)
        self.accelaration.mult(0)
        
        
    
    

    