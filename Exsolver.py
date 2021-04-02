import Fraction as frac

# create a function that will turn a string into a parsed list

def exparser(equation):

    # create an empty list for the result
    pequation = []

    # create a str to hold a num untill it is pushed to the list
    num = ''

    # while the the string isn't entirely parsed
    while not equation == '':

        print(equation)


        # if the first char is a num
        if equation[0] in '0123456789.':

            # add the first item of the list to num
            num += equation[0]

        # if the first char is a symbal
        elif equation[0] in '*/+-^':

            # add the num to the parsed equation
            pequation.append(frac.tofraction(num))

            # clear the num
            num = ''

            # add the symbal to the parsed equation
            pequation.append(equation[0])

        # if the first char is a parenthethes
        if equation[0] == '(':

            # add the num to the parsed equation
            if not num == '':

                pequation.append(frac.tofraction(num))

            # clear the num
            num = ''

            #parse the equation in the parentheses
            parennum = 1
            x=1

            # loop thru the equation until we find the end the paren grouping
            while parennum > 0:

                if equation[x] == '(':  parennum += 1
                if equation[x] == ')':  parennum -= 1

                x += 1

            pequation.append(exparser(equation[1:x]))
            equation = equation[x:]

        equation = equation[1:]

    if not num == '':

        pequation.append(num)
        
    return pequation


def equation_solver(equation):

    # loop thru the equation and solve all the parentheses
    for item in equation:

        if type(item) == 'list':

            # if there is an implied multiplication
            if equation[equation.index(item)-1].__name__ == 'Fraction':

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

    print(equation_solver(exparser('1+1')))
