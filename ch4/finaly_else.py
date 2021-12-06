import random



def finallyTest(choice):
    try:
        choice = random.choice(some_exceptions)
        print("raising {}".format(choice))
        if choice:
            raise choice("An error")
    except ValueError:
        print("Caught a ValueError")
    except TypeError:
        print("Caught a TypeError")
    except Exception as e:
        print("Caught some other error: %s" % (e.__class__.__name__))
    else:
        print("This code called if there is no exception")
    finally:
        print("This cleanup code is always called")


if __name__ == '__main__':
    some_exceptions = [ValueError, TypeError, IndexError, None]
    finallyTest(some_exceptions)
