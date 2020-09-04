def add(n1, n2):
    summ = round((n1 + n2), 4)
    print(f'The sum of {n1} and {n2} is {summ}.')
    return str(n1) + '+' + str(n2) + '=' + str(summ)


def subtract(n1, n2):
    diff = round((n1 - n2), 4)
    print(f'The difference of {n1} and {n2} is {diff}.')
    return str(n1) + '-' + str(n2) + '=' + str(diff)


def multiply(n1, n2):
    prod = round((n1 * n2), 4)
    print(f'The product of {n1} and {n2} is {prod}.')
    return str(n1) + '*' + str(n2) + '=' + str(prod)


def divide(n1, n2):
    if n2 != 0:
        quot = round((n1 / n2), 4)
        print(f'The product of {n1} and {n2} is {quot}.')
        return str(n1) + '/' + str(n2) + '=' + str(quot)
    else:
        print('You cannot divide by zero.!!')
        return 'DIV ERROR'


def exponent(n1, n2):
    power = round((n1 ** n2), 4)
    print(f'The result of {n1} to the power of {n2} is {power}.')
    return str(n1) + '**' + str(n2) + '=' + str(power)


print('Welcome to Python Calculator App')
repeat = True
calc = []
while repeat:
    print('Enter two numbers and an operation to be performed on them.')

    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    operation = input('Enter an operation (Addition,Subtraction,Multiplication, Division,'
                      'or exponentiation): ').lower().strip()

    if operation.startswith('a'):
        result = add(num1, num2)
    elif operation.startswith('s'):
        result = subtract(num1, num2)
    elif operation.startswith('m'):
        result = multiply(num1, num2)
    elif operation.startswith('d'):
        result = divide(num1, num2)
    elif operation.startswith('e'):
        result = exponent(num1, num2)
    else:
        print('Not a valid calculation option.')
        result = "OPERATION ERROR"
    calc.append(result)
    choice = input('Do you like to calculate again?(Yes/No): ').lower().strip()
    if choice.startswith('n'):
        print('Calculation Summary: ')
        for cal in calc:
            print(cal)
        print('Thank you for using the Calculator App')
        repeat = False
