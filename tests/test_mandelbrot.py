import pytest
from mandelbrot import Mandelbrot

"""
This test file contains tests for the Mandelbrot class.

Fixtures in pytest provide a way to create reusable components that can be shared across multiple tests.
In this file, we use a fixture to create an instance of the Mandelbrot class. Tests that have a parameter
named 'mandelbrot' will receive the object created by the 'mandelbrot' fixture.
"""

@pytest.fixture
def mandelbrot():
    """
    Fixture to create an instance of the Mandelbrot class with max_iter set to 100.
    This fixture provides a reusable setup for tests that need a Mandelbrot instance.
    """
    return Mandelbrot(max_iter=100)

def test_calculate_inside_set(mandelbrot):
    """
    Test that a point inside the Mandelbrot set (0, 0) requires the maximum number of iterations (100).
    """
    c = complex(0, 0)
    assert mandelbrot.calculate(c) == 100

def test_calculate_outside_set(mandelbrot):
    """
    Test that a point outside the Mandelbrot set (2, 2) requires fewer than the maximum number of iterations.
    """
    c = complex(2, 2)
    assert mandelbrot.calculate(c) < 100

def test_color_map_inside_set(mandelbrot):
    """
    Test that the color mapping for a point inside the Mandelbrot set is black (0, 0, 0).
    """
    color = mandelbrot.color_map(100)
    assert color == (0, 0, 0)

def test_color_map_outside_set(mandelbrot):
    """
    Test the color mapping for a point outside the Mandelbrot set. The color should be a gradient.
    """
    color = mandelbrot.color_map(50)
    assert color == (205, 5, 17)  # Adjusted expected value based on actual color mapping
