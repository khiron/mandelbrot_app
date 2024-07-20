# the existence of an __init__.py file in a directory makes it a package 
# Then we can `import mandelbrot` and call it's main() function from any other python app
# including a python script like run_app.py

from .main import main
from .mandelbrot import Mandelbrot
from .mandelbrot_buffer import MandelbrotBuffer
from .mandelbrot_view import MandelbrotView