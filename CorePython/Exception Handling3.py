try:
    print("Line1")

    print("Line2")
    try:
        print("Line3")
        3+"x"
        print("Line4")
    except ZeroDivisionError:
        print("Except1")
    finally:
        print("Finally1")
    print("Line5")
except TypeError:
    print("Line5")
finally:
    print("finally2")
