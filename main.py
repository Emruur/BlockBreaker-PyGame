import pygame
from mover import Mover
from vector import Vector2D
from line_segment import LineSegment

WIDTH,HEIGHT= 800,800;
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

balls= []

def main():
    
    running= True
    ready_to_shoot= False
    shooting_direction= None

    
    ball_count= 3


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
            shoot_balls(shooting_direction,ball_count)
            shooting_direction= None
            ready_to_shoot= False

        elif not pygame.mouse.get_pressed()[0] and not ready_to_shoot:
            ready_to_shoot= False
        
        
        handle_ball_movement()
        draw(shooting_direction)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
   


def draw(shooting_direction):
    WIN.fill(GREY)
    pygame.draw.rect(WIN, RED, base)

    if not shooting_direction== None:
        pygame.draw.line(WIN, BLACK, (WIDTH/2,base.y), shooting_direction.getNumbers(), 3)

    if not balls== []:
        for ball in balls:
            pygame.draw.circle(WIN, WHITE,ball.location.getNumbers(),ball.radius)

def handle_ball_movement():
    if not balls==[]:
        for b in balls:
            b.update()
            if b.location.x<= 0 :
                b.location.x= 0
                b.velocity.x *= -1

            elif b.location.x>= WIDTH:
                b.location.x= WIDTH
                b.velocity.x *= -1

            if b.location.y <= 0:
                b.location.y = 0
                b.velocity.y *= -1
            
def shoot_balls(shooting_direction, ball_count):

    base_vector= Vector2D(WIDTH/2,base.y)

    dir_vector= shooting_direction.get_substracted(base_vector)
    dir_vector.mult(-1)
    dir_vector.normalize()


    velocity= dir_vector.get_multiplied(-15)


    for i in range(0, ball_count):

        location= base_vector.get_added(dir_vector.get_multiplied(i*100))
        
        balls.append(Mover(location,velocity.copy()))
        
    




if __name__=="__main__":
    main()