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
        z = np.zeros(c.shape, dtype=np.complex128)
        div_time = np.full(c.shape, self.max_iter, dtype=int)
        mask = np.full(c.shape, True, dtype=bool)

        for i in range(self.max_iter):
            z[mask] = z[mask] * z[mask] + c[mask]
            mask[np.abs(z) > 2] = False
            div_time[mask & (div_time == self.max_iter)] = i

        return div_time

    def update_image(self):
        re = np.linspace(-2.0, 1.0, self.width) / self.zoom + self.offset[0]
        im = np.linspace(-1.5, 1.5, self.height) / self.zoom + self.offset[1]
        re, im = np.meshgrid(re, im)
        c = re + 1j * im
        div_time = self.mandelbrot(c)
        color = 255 - (div_time * 255 // self.max_iter)
        self.image = np.stack([color]*3, axis=2).astype(np.uint8)

    def zoom_in(self, pos, factor):
        x, y = pos
        re = 3.0 * (x / self.width - 0.5) / self.zoom + self.offset[0]
        im = 3.0 * (y / self.height - 0.5) / self.zoom + self.offset[1]
        self.offset = (re, im)
        self.zoom *= factor
        self.update_image()

    def draw(self, surface):
        pygame.surfarray.blit_array(surface, self.image)
