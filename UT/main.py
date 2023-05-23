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

player_icon = "player_icon.png" # "N:\\My Pictures\\Shalom.jpg"
dash_icon = "player_icon_dash.png"
chara = classes.Character(player_icon, width=50, height=50, position_x=screen.get_width() / 2, position_y=screen.get_height() / 2)

buffer = 22
score = 0

dead = False
first_movement = False
dash_cooldown = False
dash_time = 0
last_dash = 0

angreifers = []
angreifers.append(classes.Angreifer("red", position_x = -50, position_y = -50, width=30, height=30, direction="vertical"))
angreifers.append(classes.Angreifer("green", position_x = -50, position_y = -50, width=30, height=30, direction="vertical"))
angreifers.append(classes.Angreifer("red", position_x = -50, position_y = -50, width=30, height=30, direction="horizontal"))


def has_time_passed(time_1, seconds_l=None, seconds_u=None):
    time_passed = time() - time_1
    if seconds_l and seconds_u:
        if time_passed >= seconds_l and time_passed < seconds_u:
            return True
    elif seconds_l:
        if time_passed >= seconds_l:
            return True
    elif seconds_u:
        if time_passed < seconds_u:
            return True
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
        my_font = pygame.font.SysFont('Comic Sans MS', 20)
        text_surface = my_font.render(str(round(score / _FPS, 3))  + "s", False, (255, 255, 255))
        screen.blit(text_surface, (buffer, buffer))

        keys = pygame.key.get_pressed()
        keysinput.wasdinput(keys, buffer, chara, screen, dt) # movement / freeze program

        # DASH ----------------------->

        if keys[pygame.K_RSHIFT]:
            if has_time_passed(dash_time, 4):
                dash_time = time()
        if has_time_passed(dash_time, 0, 1):
            chara.speed = 500
            chara.change_image(dash_icon)
        else:
            chara.speed = 300
            chara.change_image(player_icon)
            last_dash = time()

        # ---------------------------->

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
                    _.time_1 = float(time())
                    _.position[_.not_direction] = random.uniform(chara.position[_.not_direction] - _.spawn_distance, chara.position[_.not_direction] + _.spawn_distance)
                    _.position[_.direction] = 0
                    _.start = False
                    _.start0 = True
                    _.wait_time = random.uniform(0.1, 0.5)

                if has_time_passed(_.time_1, _.wait_time):
                    if _.start0:
                        _.time = time()
                        _.start0 = False
                    _.position[_.direction] = ( time() - _.time ) * 400
                    _.display_angreifer(screen)
                    if _.check_collision(chara):
                        dead = True
                if _.position[_.direction] > _.screen_size:
                    _.start = True
                    #_.position = pygame.Vector2(0, 0)

        if first_movement == True:
            score += 1

    # flip() the display to put your work on screen
    pygame.display.flip()
    #print(player_pos)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(_FPS) / 1000

pygame.quit()
