import pygame
from vector import Vector2D

class Block:
    def __init__(self, location,side_length):
        self.location= location
        self.side_length= side_length
        self.model= pygame.Rect(location.x,location.y,side_length,side_length)


    def shift_location(self,length):
        shift_vector= Vector2D(0,length)
        self.location.add(shift_vector)
        self.model.x= self.location.x
        self.model.y= self.location.y