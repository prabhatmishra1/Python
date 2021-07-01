def display(n):
    s=0
    if n==0:
        return  0           
    s= n+display(n-1)
    print(" %d + "%(n),end='')
    return s


if __name__ =="__main__":
    print("= %d"%display(10))
