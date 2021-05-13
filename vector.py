from numpy import sqrt
class Vector2D:
    def __init__(self,x:float,y:float):
        self.x= x
        self.y= y

    def add(self,vector):
        if(isinstance(vector, Vector2D)):

            self.x += vector.x
            self.y += vector.y
            return True

        else:
            return False

    def get_added(self,vector):

        x= self.x + vector.x
        y= self.y + vector.y

        return Vector2D(x,y)

    def mult(self,integer:float):
        
        self.x *= integer
        self.y *= integer

    def get_multiplied(self, integer:float):

        x= self.x * integer
        y= self.y * integer

        return Vector2D(x,y)

        
    def div(self, integer: float):
     
        self.x /= integer
        self.y /= integer
    

    def substract(self, vector):
        if(isinstance(vector, Vector2D)):

            self.x -= vector.x
            self.y -= vector.y
            return True

        else:
            return False

    def get_substracted(self,vector):
        x= self.x - vector.x
        y= self.y - vector.y

        return Vector2D(x,y)



    def get_substracted(self,vector):
        x= self.x - vector.x
        y= self.y - vector.y

        return Vector2D(x, y)


    def mag(self):
        temp= (self.x**2)+(self.y**2)
        return sqrt(temp)

    def normalize(self):
        magnitude= self.mag()
        self.x /= magnitude
        self.y /= magnitude

    def get_normalized(self,vector):
        magnitude= self.mag()
        x=self.x / magnitude
        y=self.y / magnitude

        return Vector2D(x,y)


    def dot(self, vector):
        return (self.x*vector.x)+(vector.y*self.y)


    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
    def getNumbers(self):
        return (self.x,self.y)

    def copy(self):
        return Vector2D(self.x,self.y)

    
