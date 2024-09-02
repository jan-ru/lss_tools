# script.py
from pyscript import Element

def init_app():
    class_value = Element('class-input').value
    email_value = Element('email-input').value
    
    if class_value and email_value:
        Element('init-form').element.style.display = "none"
        Element('main-nav').element.style.display = "block"
        Element('result').write(f"Initialized for class: {class_value}, email: {email_value}")
    else:
        Element('result').write("Please fill in both class and email")

def show_console():
    Element("console").element.style.display = "block"
    Element("calculator").element.style.display = "none"

def show_calculator():
    Element("console").element.style.display = "none"
    Element("calculator").element.style.display = "block"
    
    # Clear input fields
    Element('num1').element.value = ""
    Element('num2').element.value = ""
    
    # Clear result
    Element('result').write("Result will appear here")

def calculate_sum():
    try:
        num1 = float(Element('num1').value)
        num2 = float(Element('num2').value)
        result = num1 + num2
        Element('result').write(f"The sum is: {result}")
    except ValueError:
        Element('result').write("Please enter valid numbers")

# Initialize the app
Element('main-nav').element.style.display = "none"
Element('console').element.style.display = "none"
Element('calculator').element.style.display = "none"
Element('result').write("Please initialize the app")