import pygame
from vector import Vector2D
from line_segment import LineSegment

class Block:
    def __init__(self, location,side_length):
        self.location= location
        self.side_length= side_length
        self.model= pygame.Rect(location.x,location.y,side_length,side_length)
        self.health= 2

    def shift_location(self,length):
        shift_vector= Vector2D(0,length)
        self.location.add(shift_vector)
        self.model.x= self.location.x
        self.model.y= self.location.y

    def ball_hit_on(self,ball):
        e1= self.location
        e2= self.location.get_added(Vector2D(self.side_length,0))
        e3= self.location.get_added(Vector2D(0,self.side_length))
        e4= self.location.get_added(Vector2D(self.side_length,self.side_length))

        l1= LineSegment(e1,e2)
        l2= LineSegment(e3,e4)
        l3= LineSegment(e1,e3)
        l4= LineSegment(e2,e4)

        max= 0
        arr= [l1,l2,l3,l4]

        min = 10000;
        count= 1
        
        for l in arr:
            distance= l.calculate_distance(ball.location)
            if distance< min:
                min= distance
                min_index= count

            count+=1
                
            
        if min_index==1 or min_index==2:
            return 1
        else:
            return 2




        
