import pygame
from mover import Mover
from vector import Vector2D

WIDTH,HEIGHT= 1000,1000;
WIN= pygame.display.set_mode((WIDTH,HEIGHT))

GREY= (100,100,100)
WHITE= (255,255,255)
RED= (255,0,0)
YELLOW= (155,155 ,0)

FPS= 100
clock= pygame.time.Clock()

mover1= Mover(100,100,30,10)



def main():
    force= Vector2D(0,5)
    running= True

    while running:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False


        mover1.applyForce(force)
        edgeDetect(mover1)
        mover1.update()
        draw()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
   


def draw():
    WIN.fill(GREY)

    pygame.draw.circle(WIN, RED,mover1.location.getNumbers(),mover1.radius)

def edgeDetect(mover):
    if(mover.location.y+mover.radius>=HEIGHT):
        mover1.location.y= HEIGHT-mover1.radius
        mover.velocity.mult(-1)

if __name__=="__main__":
    main()