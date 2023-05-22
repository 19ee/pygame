import pygame, random
import keysinput, classes
from time import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.font.init()
running = True
dt = 0
_FPS = 120
width = screen.get_width()
height = screen.get_height()

player_icon = "pygame\\UT\\player_icon.png" # "N:\\My Pictures\\Shalom.jpg"
chara = classes.Character(pygame.image.load(player_icon), width=50, height=50, position_x=screen.get_width() / 2, position_y=screen.get_height() / 2)

buffer = 22
score = 0

dead = False
first_movement = False

angreifers = []
angreifers.append(classes.Angreifer("red", position_x = -50, position_y = -50, width=30, height=30, direction="vertical"))
angreifers.append(classes.Angreifer("green", position_x = -50, position_y = -50, width=30, height=30, direction="vertical"))
angreifers.append(classes.Angreifer("red", position_x = -50, position_y = -50, width=30, height=30, direction="horizontal"))


def has_time_passed(time_1, seconds_l, seconds_u):
    time_passed = time() - time_1
    if time_passed >= seconds_l and time_passed < seconds_u:
        return True
    else:
        return False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if dead:
        screen.fill("red")
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render('You died', False, (255, 255, 255))
        screen.blit(text_surface, (0,0))
    else:
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        pygame.draw.rect(screen, "white", pygame.Rect((10, 10), (width-20, height-20)))
        pygame.draw.rect(screen, "black", pygame.Rect((20, 20), (width-40, height-40)))

        screen.blit(chara.image, chara.position)

        #score
        my_font = pygame.font.SysFont('Comic Sans MS', 50)
        text_surface = my_font.render(str(score), False, (255, 255, 255))
        screen.blit(text_surface, (width/2 - 25 ,height/2 - 25))

        keys = pygame.key.get_pressed()
        keysinput.wasdinput(keys, buffer, chara, screen, dt) # movement / freeze program

        if first_movement == False:
            if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
                first_movement = True
                print("mogus")
                aktueller_angreifer = 0
                
        elif aktueller_angreifer == 0:                  
            for _ in angreifers:
                if _.direction == "vertical":
                    _.direction = 1
                    _.not_direction = 0
                    _.screen_size = screen.get_height()
                if _.direction == "horizontal":
                    _.direction = 0
                    _.not_direction = 1
                    _.screen_size = screen.get_width()
                if _.start:
                    time_1 = float(time())
                    _.position[_.not_direction] = random.uniform(0, screen.get_width())
                    _.position[_.direction] = 0
                    _.start = False
                    _.start0 = True
                    _.wait_time = random.uniform(0.1, 2)
                if has_time_passed(time_1, _.wait_time, 30):
                    if _.start0:
                        _.time = time()
                        _.start0 = False
                    _.position[_.direction] = ( time() - _.time ) * 200
                    _.display_angreifer(screen)
                    if _.check_collision(chara):
                        dead = True
                if _.position[_.direction] > _.screen_size:
                    _.start = True
                    _.position = (0, 0)

    # flip() the display to put your work on screen
    pygame.display.flip()
    #print(player_pos)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(_FPS) / 1000

pygame.quit()