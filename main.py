import pygame
from mover import Mover
from vector import Vector2D
from line_segment import LineSegment
from block import Block

pygame.font.init()

WIDTH,HEIGHT= 700,700;
WIN= pygame.display.set_mode((WIDTH,HEIGHT))

font = pygame.font.Font('freesansbold.ttf', 32)

GREY= (100,100,100)
WHITE= (255,255,255)
RED= (255,0,0)
YELLOW= (155,155 ,0)
BLACK= (0,0,0)

FPS= 120
clock= pygame.time.Clock()

base_width, base_height= 100,40
base= pygame.Rect((WIDTH-base_width)/2,HEIGHT-base_height,base_width,base_height)

balls= []

BLOCK_NUMBER= 10
BLOCK_LENGTH= WIDTH/ BLOCK_NUMBER

blocks=  [[None]*BLOCK_NUMBER for _ in range(BLOCK_NUMBER)]

GAME_OVER= pygame.USEREVENT+1

def main(): 
    running= True
    ready_to_shoot= False
    shooting_direction= None

    
    ball_count= 4
    add_block_row()


    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False
            if event.type == GAME_OVER:
                pygame.time.delay(1000)
                pygame.quit()

        if balls== []:  

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
    
    if not shooting_direction== None:
        pygame.draw.line(WIN, BLACK, (WIDTH/2,base.y), shooting_direction.getNumbers(), 3)

    if not balls== []:
        for ball in balls:
            pygame.draw.circle(WIN, WHITE,ball.location.getNumbers(),ball.radius)

    for row in blocks:
        for block in row:
            if not block== None:
                text = font.render(str(block.health), True,YELLOW, BLACK)
                textRect = text.get_rect()
                textRect.center= (block.location.x+block.side_length/2,block.location.y+ block.side_length/2)

                pygame.draw.rect(WIN, BLACK, block.model)
                pygame.draw.rect(WIN, YELLOW, block.model,5)
                WIN.blit(text, textRect)
        


    pygame.draw.rect(WIN, RED, base)



def handle_ball_movement():
    if not balls==[]:
        for b in balls:
            b.update()

            for row in blocks:
                for block in row:
                    if not block== None:
                        if b.location.x>= (block.location.x)-b.radius and b.location.x<= block.location.x+ block.side_length+ b.radius:
                            if b.location.y >= block.location.y-b.radius and b.location.y<= block.location.y+ block.side_length+ b.radius:
                                index= row.index(block)
                                block.health -= 1
                                hit_type= block.ball_hit_on(b)
                                if hit_type==1:
                                    b.velocity.y *= -1
                                elif hit_type==2:
                                    b.velocity.x *= -1
                                if(block.health==0):
                                    row[index]= None
                                


            if b.location.y< HEIGHT and b.location.x > 0 and b.location.x<WIDTH:
                b.in_bounds= True

            if b.location.x<= 0 and b.in_bounds:
                b.location.x= 0
                b.velocity.x *= -1

            elif b.location.x>= WIDTH and b.in_bounds:
                b.location.x= WIDTH
                b.velocity.x *= -1

            if b.location.y <= 0 and b.in_bounds:
                b.location.y = 0
                b.velocity.y *= -1

            elif b.location.y >= HEIGHT and b.in_bounds:
                balls.remove(b)
                if(balls==[]):
                    shift_blocks()
                    add_block_row()
            
            
def shoot_balls(shooting_direction, ball_count):

    base_vector= Vector2D(WIDTH/2,base.y)

    dir_vector= shooting_direction.get_substracted(base_vector)
    dir_vector.mult(-1)
    dir_vector.normalize()


    velocity= dir_vector.get_multiplied(-12)


    for i in range(0, ball_count):

        location= base_vector.get_added(dir_vector.get_multiplied(i*100))
        
        balls.append(Mover(location,velocity.copy()))
        
    
def add_block_row():
    base_location= Vector2D(BLOCK_LENGTH,0)
    for i in range(0,BLOCK_NUMBER):
        block_location= base_location.get_multiplied(i)
        blocks[0][i]= Block(block_location,BLOCK_LENGTH)


def shift_blocks():
    
    for i in range(8,-1,-1):
        for e in range(9,-1,-1):
            block= blocks[i][e]
            if not block == None:

                block.shift_location(BLOCK_LENGTH)
                blocks[i+1][e]= block
                blocks[i][e]= None

                if(i==8):
                    pygame.event.post(pygame.event.Event(GAME_OVER))
    
                
    #for r in blocks:
        #for bl in r:
            #if(bl== None):
                #print(0,end="")
            #else:
                #print(1,end="")
        #print("")



if __name__=="__main__":
    main()