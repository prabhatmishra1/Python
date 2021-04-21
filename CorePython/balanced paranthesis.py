open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def matched(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return False
    if len(stack) == 0: 
        return True
  
# Driver code

string ="((jkl)78(A)&l(8(dd(FJI:),):)?)" 
print(string,"-", matched(string)) 
   
