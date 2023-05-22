import pygame

class Character:
    def __init__(self, image, width, height, position_x, position_y):
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.width = width
        self.height = height
        self.position = pygame.Vector2(position_x, position_y)
        self.speed = 300

    def change_image(self, image):
        self.image = pygame.transform.scale(pygame.image.load(image), (self.width, self.height))
       
class Angreifer:
    def __init__(self, color, position_x, position_y, width, height, direction):
        self.color = color
        self.width = width
        self.height = height
        self.position = pygame.Vector2(position_x, position_y)
        #self.position_Rect((position_x, position_y), (width, height))
        self.start = True
        self.direction = direction
        self.spawn_distance = 300
   
    def check_collision(self, chara):
        if (chara.position.x + chara.width) > self.position.x:
            if chara.position.x < (self.position.x + self.width):
                if (chara.position.y + chara.height) > self.position.y:
                    if chara.position.y < (self.position.y + self.height):
                        return True

    def display_angreifer(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position, (self.width, self.height)))