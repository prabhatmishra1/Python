arr=[1,"2",1,"Ramna","Raman", 3,4,1,2,4]
result=[]

#Method-1:

"""for index,value in enumerate(arr):
    if value:
      result.append(value)
    print("i=",value)    
    for j in range(len(arr)):
        print("j=",j,end=" ")
        if arr[j]==value:
            arr[j]=None

print(result)
"""

#Method-2

"""for value in arr:
    if value not in result:
      result.append(value)
arr=result      
print(arr)      
"""
#Method-3

"""
[result.append(value) for value in arr if value not in result]
print(result)
"""

#count the frequency of elements
#method-1

"""key=[]
[key.append(value) for value in arr if value not in key]

d=dict()
for value in key:
  cnt=0
  print(value)
  for j in arr:
    if value==j:
      cnt+=1
  d[value]=cnt  
print(d)
"""
#method-2
'''d={}
for value in arr:
  if value not in d:
    cnt=0
    for j in arr:
        if j==value:
          cnt+=1
    d[value]=cnt      
print(d)  
'''

#method-3

d={}

for value in arr:
  if value in d:
    d[value]=d[value]+1
  else:
    d[value]=1
      
print(d)    