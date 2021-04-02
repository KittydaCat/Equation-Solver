def equation_solver(equation):

    # loop thru the equation and solve all the parentheses
    for item in equation:

        if type(item) == 'list':

            # if there is an implied multiplication
            if type(equation[equation.index(item)-1]) == 'str':

                # add the * sign
                equation.insert(equation.index(item)-1, '*')

            # insert the solved expression from the parens
            equation.insert(equation_solver(item)[0], equation.pop(equation.index(item)))

    while '^' in equation:

        x = equation.index('^')
        equation[x-1:x+2] = equation[x-1] ^ equation[x+1]

    while '/' in equation:

        x = equation.index('/')
        equation[x-1:x+2] = equation[x-1] / equation[x+1]

    while '*' in equation:

        x = equation.index('*')
        equation[x-1:x+2] = equation[x-1] * equation[x+1]

    while '-' in equation:

        x = equation.index('-')
        equation[x-1:x+2] = equation[x-1] - equation[x+1]

    while '+' in equation:

        x = equation.index('+')
        equation[x-1:x+2] = equation[x-1] + equation[x+1]

    return equation

if __name__ == '__main__':
    import Expressionsparser
    print(equation_solver(Expressionsparser.equationparser(input())))
