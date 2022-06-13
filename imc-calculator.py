import string
import os

class User:
    def __init__(user, height, weight):
        user.height = (float(height)*float(height))
        user.weight = float(weight)

    def calculate(user):
        print("Your IMC is " + ("{0:.2f}".format(user.weight/user.height)))
        user.imc = user.weight/user.height

    def classificate(user):
        if(user.imc < 18.5): print('Underweight')
        elif(user.imc >= 18.5 and user.imc <= 24.9): print('Normal weight')
        elif(user.imc >= 25 and user.imc <= 29.9): print('Overweight')
        elif(user.imc >= 30 and user.imc <= 34.9): print('Obesity I')
        elif(user.imc >= 35 and user.imc <= 39.9): print('Obesity II')
        elif(user.imc >= 40): print('Obesity III')


def validate(height, weight):
    try:
        float(height)
        float(weight)
    except ValueError:
        return bool(False)
    
    return bool(True)


def main(height, weight):
    if(validate(height, weight)):
        test = User(height, weight)
        test.calculate()
        test.classificate()
        return 'Valid'
    else:
        return 'Invalid'

def test_answer():
    assert main('1.70', '80') == 'Valid'
    assert main('aaa', 'bbb') == 'Invalid'
    assert main('1,70', '80') == 'Invalid'
