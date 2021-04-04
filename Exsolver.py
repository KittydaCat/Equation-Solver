import Fraction as frac
import random as rand

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

        pequation.append(frac.tofraction(num))

    print(pequation)
    return pequation


def equation_solver(equation):

    # loop thru the equation and solve all the parentheses
    for item in equation:

        if type(item) == type([]):

            # if there is an implied multiplication in front
            if type(equation[equation.index(item)-1]) == type(frac.Fraction(1,1)) and not equation.index(item) == 0:

                # add the * sign
                equation.insert(equation.index(item), '*')

            # if there is an implied multiplication in back
            if not equation.index(item) == len(equation)-1 and type(equation[equation.index(item)+1]) == type(frac.Fraction(1,1)):

                # add the * sign
                equation.insert(equation.index(item)+1, '*')

            # insert the solved expression from the parens
            equation.insert(equation.index(item), equation_solver(equation.pop(equation.index(item)))[0])
            print(equation)

    while '^' in equation:

        x = equation.index('^')
        equation[x-1:x+2] = [equation[x-1] ** equation[x+1]]
        print(equation)
    while '/' in equation:

        x = equation.index('/')
        equation[x-1:x+2] = [equation[x-1] / equation[x+1]]
        print(equation)
    while '*' in equation:

        x = equation.index('*')
        equation[x-1:x+2] = [equation[x-1] * equation[x+1]]
        print(equation)
    while '-' in equation:

        x = equation.index('-')
        equation[x-1:x+2] = [equation[x-1] - equation[x+1]]
        print(equation)
    while '+' in equation:

        x = equation.index('+')
        equation[x-1:x+2] = [equation[x-1] + equation[x+1]]
        print(equation)
    return equation

if __name__ == '__main__':

    equation = '3695(49*7+5*686481*857/992+8)*21-3/8+62085^7154'

    print(equation_solver(exparser(equation)))
