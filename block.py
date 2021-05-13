import pygame

class Block:
    def __init__(self, location,side_length):
        self.location= location
        self.side_length= side_length
        self.model= pygame.Rect(location.x,location.y,side_length,side_length)