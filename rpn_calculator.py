import cProfile
import operator

def rpn_compute(tokens):        
    '''
    Returns the result of a reverse polish notation calculation.

            Parameters:
                    tokens (str): A rpn calculation
            Returns:
                    result (int): Integer result of the calculation
    '''
    # To augment the performance and reduce code we will use this "OPERATORS" dict()
    OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow
    }

    stack = []
    # Get rid of spaces by making tokens into an array
    tokens = tokens.split(" ")

    # Loop through tokens
    for token in tokens:
        # If token is an operator, compute this part of the calculation
        if token in OPERATORS:
            operand2, operand1= stack.pop(), stack.pop()
            result = OPERATORS[token](operand1, operand2)
            stack.append(int(result))
        # Else, add number to stack
        else:
            stack.append(int(token))
    # Return result
    return stack.pop()

def rpn_to_infix(tokens):
    '''
    Returns the reverse polish notation calculation in infix notation.

            Parameters:
                    tokens (str): A rpn calculation
            Returns:
                    result (str): String representing the infix equivalent of the rpn
    '''
    stack = []

    # Get rid of spaces by making tokens into an array
    tokens = tokens.split(" ")

    # Loop through tokens
    for token in tokens:
        # If token is an operator, pop the 2 last numbers in stack 
        if token not in {'^', '/', '-', '+', '*'}:
            stack.append(token)
        else:
            second_to_last, last = stack.pop(), stack.pop()
            stack.append("({} {} {})".format(last, token, second_to_last))
    # Return result
    return stack.pop()

if __name__ == '__main__':
    # Here we assume the user will enter a proper rpn equation

    tokens = input("Please enter a reverse polish notation equation using spaces: ")

    cProfile.run("rpn_compute(tokens)") # This is to test the speed of the function
    print("The result of {} is {}.".format(rpn_to_infix(tokens),rpn_compute(tokens)))
