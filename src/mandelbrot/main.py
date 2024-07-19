import pygame
from .mandelbrot import Mandelbrot

# Constants
WIDTH, HEIGHT = 800, 600
MAX_ITER = 100
ZOOM_FACTOR = 1.1

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mandelbrot Set')
    clock = pygame.time.Clock()
    
    mandelbrot = Mandelbrot(WIDTH, HEIGHT, MAX_ITER)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    mandelbrot.zoom_in(event.pos, ZOOM_FACTOR)
                elif event.button == 5:  # Scroll down
                    mandelbrot.zoom_in(event.pos, 1 / ZOOM_FACTOR)

        screen.fill((0, 0, 0))
        mandelbrot.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
