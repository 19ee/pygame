import pygame

def wasdinput(keys, buffer, chara, screen, dt):

    if keys[pygame.K_w]:
        if chara.position.y > buffer:
            chara.position.y -= 300 * dt
    if keys[pygame.K_s]:
        if chara.position.y < (screen.get_height() - (chara.height + buffer)):
            chara.position.y += 300 * dt
    if keys[pygame.K_a]:
        if chara.position.x > buffer:
            chara.position.x -= 300 * dt
    if keys[pygame.K_d]:
        if chara.position.x < (screen.get_width() - (chara.width + buffer)):
            chara.position.x += 300 * dt

    if keys[pygame.K_0]: # freeze program
        while True:
            pass

if __name__ == '__main__':
    pass