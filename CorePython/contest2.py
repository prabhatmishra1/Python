def prime_generator(n):
  a=0   
  for i in range(2,n+1):
    for j in range(2,(i//2)+1):
         if(i%j==0):
             break
    else:
        try:
          yield i
        except StopIteration:
            print("0")
it=prime_generator(10)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("0")
        break

