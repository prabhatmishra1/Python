def display(n):
    if n==0:
        return  
    print(n)       
    display(n-1)


if __name__ =="__main__":
    display(10)

