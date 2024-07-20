import pygame
from mandelbrot import Mandelbrot

# Constants
WIDTH, HEIGHT = 800, 600
MAX_ITER = 100
ZOOM_FACTOR = 1.5

def draw_buttons(screen):
    font = pygame.font.Font(None, 36)
    zoom_in_button = font.render('Zoom In', True, (255, 255, 255))
    zoom_out_button = font.render('Zoom Out', True, (255, 255, 255))
    
    screen.blit(zoom_in_button, (10, 10))
    screen.blit(zoom_out_button, (10, 50))
    
    return zoom_in_button.get_rect(topleft=(10, 10)), zoom_out_button.get_rect(topleft=(10, 50))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mandelbrot Set')
    clock = pygame.time.Clock()
    
    mandelbrot = Mandelbrot(WIDTH, HEIGHT, MAX_ITER)
    running = True

    while running:
        screen.fill((0, 0, 0))
        mandelbrot.draw(screen)
        zoom_in_rect, zoom_out_rect = draw_buttons(screen)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if zoom_in_rect.collidepoint(event.pos):
                    mandelbrot.zoom_in((WIDTH // 2, HEIGHT // 2), ZOOM_FACTOR)
                elif zoom_out_rect.collidepoint(event.pos):
                    mandelbrot.zoom_in((WIDTH // 2, HEIGHT // 2), 1 / ZOOM_FACTOR)
                elif event.button == 1:  # Left mouse button
                    mandelbrot.center_on(event.pos)

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
