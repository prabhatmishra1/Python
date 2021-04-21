class std:
    def __init__(self,a):
        num=a
        s=0
        while a!=0:
            w=a%10
            s=s+w*w*w
            a=a//10
        if(num==s):
            print(num,"Is armstrong number:")
        else:    
            print(num,"Is not armstrong number:")
            
        

obj=std(152)        
