# Design a simple calculator.  Allows the user to define an operator and numbers to add.

num1 = 0
num2 = 0
operator = ""
outPut = 0.0
finish = True

while finish:
    operator = input("What operation do you want to perform? ")

    if operator.lower() == 'done':
        finish = False
        break
    else:
        num1 = input("What is the first number? ")
        num2 = input("What is the second number? ")
        num1 = float(num1)
        num2 = float(num2)
        if operator == '+':
            outPut = num1 + num2
        elif operator == '-':
            outPut = num1 - num2
        elif operator == '*':
            outPut = num1 * num2
        elif operator == '/':
            outPut = num1 / num2
        print(outPut)
#finish = False
#break