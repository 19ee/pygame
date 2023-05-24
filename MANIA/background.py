import pygame

def draw_background(screen, num_of_keys):
    screen.fill("black")
    #pygame.draw.rect(screen, "white", pygame.Rect((10, 10), (screen.get_width()-20, screen.get_height()-20)))
    #pygame.draw.rect(screen, "black", pygame.Rect((20, 20), (screen.get_width()-40, screen.get_height()-40)))

    keys_buffer = 10
    key_width = screen.get_width() / num_of_keys
    key_height = 150
    for i in range(num_of_keys):
        pygame.draw.rect(screen, "white", pygame.Rect((( key_width*i ), screen.get_height() - key_height), (key_width, key_height)))
        
        position = (key_width*i + keys_buffer/2, screen.get_height() - key_height + keys_buffer/2)
        dimensions = (key_width - keys_buffer, key_height - keys_buffer)
        pygame.draw.rect(screen, "black", pygame.Rect(position, dimensions))

def draw_keys(screen, keys):
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('You died', False, "white")
    screen.blit(text_surface, (0,0))
