
# create a function that will turn a string into a parsed list

def equationparser(equation):

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
            pequation.append(num)

            # clear the num
            num = ''

            # add the symbal to the parsed equation
            pequation.append(equation[0])

        # if the first char is a parenthethes
        if equation[0] == '(':

            # add the num to the parsed equation
            if not num == '':

                pequation.append(num)

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

            pequation.append(equationparser(equation[1:x]))
            equation = equation[x:]

        equation = equation[1:]

    if not num == '':

        pequation.append(num)
        
    return pequation

if __name__ == '__main__':

    print(equationparser(input()))
