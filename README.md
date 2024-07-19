# Mandelbrot App
A simple Mandelbrot set viewer in Python using Pygame.

## Overview
This project demonstrates best practices for structuring a Python project, including proper use of virtual environments, dependencies, testing, and documentation.

## Project Structure

```
mandelbrot_app/
├── src/
│ └── mandelbrot/
│ ├── init.py # Initializes the mandelbrot package
│ ├── main.py # Main application entry point
│ ├── mandelbrot.py # Mandelbrot set calculation and rendering logic
├── tests/
│ ├── init.py # Initializes the tests package
│ ├── test_mandelbrot.py # Test cases for the Mandelbrot class
├── pyproject.toml # Project metadata and dependencies
├── README.md # Project documentation
└── run_app.py # Script to run the application
```

### File Descriptions

- **src/mandelbrot/\_\_init\_\_.py**: Initializes the `mandelbrot` package.
- **src/mandelbrot/main.py**: Contains the main application entry point that sets up the Pygame window and handles events.
- **src/mandelbrot/mandelbrot.py**: Contains the `Mandelbrot` class, which handles the calculation and rendering of the Mandelbrot set.
- **tests/\_\_init\_\_.py**: Initializes the `tests` package.
- **tests/test_mandelbrot.py**: Contains test cases for the `Mandelbrot` class using `pytest`.
- **pyproject.toml**: Specifies project metadata and dependencies.
- **README.md**: Provides project documentation and instructions.
- **run_app.py**: A simple script to run the application.


## Getting Started

### Fork the Repository

This allows you to have a copy of the Mandelbrot_app repository under your own GitHub account.  Both repositories can then be updated independently, and share their changes if necessary.

#### How to fork the repository:

Go to the original repository: https://github.com/khiron/mandelbrot_app.

Click the "Fork" button at the top right to create a copy of the repository under your own GitHub account.

### Clone Your Fork Locally

```bash
git clone https://github.com/YOUR_USERNAME/mandelbrot_app.git
cd mandelbrot_app
```

### Set Up a Virtual Environment

Create a virtual environment to manage your project's dependencies.

```python 
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

### Install the Project in Editable Mode

Install the mandelbrot package in editable mode.  Installing the project using `pip` means that you can then import the `mandelbrot` package from anywhere on your system.  Doing this in editable mode means that changes you make to the source code will be reflected immediately without needing to reinstall the package.

```bash
pip install -e .
```
Installing the package will also download and install the libraries `pytest`, `pygame`, and `numpy`as these dependencies are specified in the `pyproject.toml` file that pip looks at when it tries to install your project.

### Run the Application

Run the application to view the Mandelbrot set.

```bash
python run_app.py
```

Use the mouse scroll wheel to zoom in and out of the Mandelbrot set.

### Testing

Run the tests using pytest which will look for any .py file that begins with `test_`.  Tests are code snippets that check if the code you wrote is working as expected, and raises an exception if it is not.  

Pytest can run all your tests with a single command.  It will automatically find all the tests in your project and run them.  If all the tests pass, pytest will return a green success message.  If any tests fail, pytest will return a red error message. 

```bash
pytest
```

#### why testing is a good practice 

This is a good way to ensure that your code is working as expected.  But it also helps when you are making changes to your code.  If you make a change that breaks something, the tests will catch it and let you know.

#### test driven development 
It is good practice to write tests before you write the code that you are testing.  So you write a test that checks if your code is working as expected, then you write the code that makes the test pass.  This is called test driven development.
 
### Start Editing in VS Code

Open the project in VS Code to start editing.

```bash
code .
```
Make sure to use the virtual environment you set up earlier. VS Code should automatically detect it, but you can select it manually if needed by pressing `F1` and typing "Python: Select Interpreter".

You can also run all tests in VS Code by installing the testing extension and clicking the "Run All Tests" button.

## Additional Resources
These packages should be loaded automatically when you install the project in editable mode.  But if you want to learn more about them, you can find their documentation here:

Pygame Documentation: https://www.pygame.org/docs/
NumPy Documentation: https://numpy.org/doc/
pytest Documentation: https://docs.pytest.org/en/stable/

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the BSD 3 clause License - see the LICENSE file for details.