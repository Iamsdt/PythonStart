def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("You can not divide by zero")
    except TypeError:
        print("Data type not supported")
    else:
        print("no error")
    finally:
        print("Thank you")


div(1.0, 2)
div(2, 0)
div(2, "4")
