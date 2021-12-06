def funny_division(divider):
    try:
        return 100 / divider
    except ZeroDivisionError:
        return "Zero is not a good idea!"
    except BaseException:
        return "General Exception"
def funny_divisions2(divider):
    try:
        if divider==13:
            raise ValueError("13 is un luck number")
        return 100/divider

    except(ZeroDivisionError , TypeError):
        """ to catch more than one error """
        return "Enter number other than Zero"

def funny_division3(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError as e:
        print("No, No, not 13!")
        print("The exception arguments were ", e.args)
        #raise




if __name__ == '__main__':
    """ test funny_division function """
    print(funny_division(2))
    print(funny_division(0))
    print(funny_division("Ali"))


    print("************************************")
    """ test funny_division2 function """
    for val in (0,"hello",50.0,13):
        """ end just turn new line to space """
        print("Test {}".format(val),end=" ")
        #print(funny_divisions2(val))

    print("************************************")
    """ test funny_division3 function """
    for val in (0, "hello", 50.0, 13):
        print("Test {}".format(val), end=" ")
        print(funny_division3(val))






