import pytest
from src.mandelbrot.mandelbrot import Mandelbrot

def test_mandelbrot_initialization():
    mandelbrot = Mandelbrot(800, 600, 100)
    assert mandelbrot.width == 800
    assert mandelbrot.height == 600
    assert mandelbrot.max_iter == 100

def test_mandelbrot_zoom_in():
    mandelbrot = Mandelbrot(800, 600, 100)
    initial_zoom = mandelbrot.zoom
    mandelbrot.zoom_in((400, 300), 1.1)
    assert mandelbrot.zoom != initial_zoom
