import pygame
from mover import Mover
from vector import Vector2D
from line_segment import LineSegment

WIDTH,HEIGHT= 1000,1000;
WIN= pygame.display.set_mode((WIDTH,HEIGHT))

GREY= (100,100,100)
WHITE= (255,255,255)
RED= (255,0,0)
YELLOW= (155,155 ,0)
BLACK= (0,0,0)

FPS= 60
clock= pygame.time.Clock()

base_width, base_height= 100,40
base= pygame.Rect((WIDTH-base_width)/2,HEIGHT-base_height,base_width,base_height)



def main():
    
    running= True
    ready_to_shoot= False
    shooting_direction= None

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False

           
        if pygame.mouse.get_pressed()[0]:
            location= pygame.mouse.get_pos()
            shooting_direction= Vector2D(location[0],location[1])
            ready_to_shoot= True

        elif not pygame.mouse.get_pressed()[0] and ready_to_shoot:
            print("BOOM!")
            shooting_direction= None
            ready_to_shoot= False

        elif not pygame.mouse.get_pressed()[0] and not ready_to_shoot:
            ready_to_shoot= False
        
      
        draw(shooting_direction)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
   


def draw(shooting_direction):
    WIN.fill(GREY)
    pygame.draw.rect(WIN, RED, base)
    if not shooting_direction== None:
        pygame.draw.line(WIN, BLACK, (WIDTH/2,base.y), shooting_direction.getNumbers(), 3)

   
if __name__=="__main__":
    main()