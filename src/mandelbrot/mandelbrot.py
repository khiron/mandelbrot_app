import numpy as np
import pygame

class Mandelbrot:
    def __init__(self, width, height, max_iter):
        self.width = width
        self.height = height
        self.max_iter = max_iter
        self.zoom = 1.0
        self.offset = (-0.5, 0.0)
        self.image = None
        self.update_image()

    def mandelbrot(self, c):
        z = 0
        n = 0
        while abs(z) <= 2 and n < self.max_iter:
            z = z*z + c
            n += 1
        return n

    def update_image(self):
        self.image = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for x in range(self.width):
            for y in range(self.height):
                re = 3.5 * (x / self.width - 0.5) / self.zoom + self.offset[0]
                im = 2.0 * (y / self.height - 0.5) / self.zoom + self.offset[1]
                c = complex(re, im)
                m = self.mandelbrot(c)
                color = self.color_map(m)
                self.image[y, x] = color

    def color_map(self, n):
        if n == self.max_iter:
            return (0, 0, 0)
        else:
            return (n % 256, (n * 5) % 256, (n * 15) % 256)

    def zoom_in(self, pos, factor):
        x, y = pos
        re = 3.5 * (x / self.width - 0.5) / self.zoom + self.offset[0]
        im = 2.0 * (y / self.height - 0.5) / self.zoom + self.offset[1]
        self.offset = (re, im)
        self.zoom *= factor
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)
        self.update_image()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def center_on(self, pos):
        x, y = pos
        re = 3.5 * (x / self.width - 0.5) / self.zoom + self.offset[0]
        im = 2.0 * (y / self.height - 0.5) / self.zoom + self.offset[1]
        self.offset = (re, im)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)
        self.update_image()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, surface):
        transposed_image = np.transpose(self.image, (1, 0, 2))
        pygame.surfarray.blit_array(surface, transposed_image)
