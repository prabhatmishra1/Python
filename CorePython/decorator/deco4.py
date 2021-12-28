def addextra(func):
    def wrapper(*args, **kwargs):
        print("add extra has benn callled")
        func()
        print("ended")
    return wrapper
@addextra
def display():
    print("This is display")

if __name__ == "__main__":
    display()