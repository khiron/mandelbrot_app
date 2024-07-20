import pytest
import numpy as np
import pygame
from mandelbrot import MandelbrotBuffer

"""
This test file contains tests for the MandelbrotBuffer class.

Fixtures in pytest provide a way to create reusable components that can be shared across multiple tests.
In this file, we use a fixture to create an instance of the MandelbrotBuffer class. Tests that have a parameter
named 'buffer' will receive the object created by the 'buffer' fixture.
"""

@pytest.fixture(scope="module")
def pygame_init():
    """
    Fixture to initialize and quit Pygame for the test module.
    """
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def buffer(pygame_init):
    """
    Fixture to create an instance of the MandelbrotBuffer class with width and height set to 100,
    and max_iter set to 100. This fixture provides a reusable setup for tests that need a MandelbrotBuffer instance.
    """
    return MandelbrotBuffer(width=100, height=100, max_iter=100)

def test_initial_image_not_empty(buffer):
    """
    Test that the initial image buffer is not empty.
    """
    assert np.any(buffer.image != 0)

def test_zoom_in(buffer):
    """
    Test that zooming in updates the zoom level correctly.
    """
    initial_zoom = buffer.zoom
    buffer.zoom_in((50, 50), 1.1)
    assert buffer.zoom == initial_zoom * 1.1, "Zooming in should increase the zoom level"
    buffer.zoom_in((50, 50), 1/1.1)
    assert buffer.zoom == initial_zoom, "Zooming out should decrease the zoom level"

def test_center_on(buffer):
    """
    Test that centering on a new point updates the offset correctly.
    """
    initial_offset = buffer.offset
    buffer.center_on((50, 50)) # center on the center of the screen
    assert buffer.offset == initial_offset, "Centering on the center should not change the offset"
    buffer.center_on((75, 75)) # center on a different point
    assert buffer.offset != initial_offset, "Centering on a different point should change the offset" 
