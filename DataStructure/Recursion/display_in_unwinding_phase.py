def display(n):
    if n==0:
        return         
    display(n-1)
    print(n)


if __name__ =="__main__":
    display(10)
