class CollisionOccure(ZeroDivisionError):
    def __init__(self,arg):
        self.msg=arg
class HashTable:
    def __init__(self):
        self.Size=10
        self.Table=[None]*self.Size

    def get_hash_value(self, key):
        hash_vlaue=0
        for value in key:
            hash_vlaue+=ord(value)
        return hash_vlaue%self.Size   
    def __setitem__(self,key,value): #For example, operator.add(x, y) is equivalent to the expression Table[key]=value .
        hash_value=self.get_hash_value(key)
        if self.Table[hash_value]:
            index=hash_value
            if index==self.Size-1:
                index=0
            while index<self.Size-1:
                if not self.Table[index]:
                    self.Table[index]=value
                    return
                index+=1
        else:            
            self.Table[hash_value]=value

    def __getitem__(self,key):
        hash_value=self.get_hash_value(key) #For example, operator.get(key) is equivalent to the expression Table[key] .
        return self.Table[hash_value]    

    def delete(self,key):
        temp=self.Table[self.get_hash_value(key)]
        self.Table[self.get_hash_value(key)]=None
        return temp
        



ref=HashTable()
ref['march 6']="prabhat"
ref['march 17']="Stuti"
ref['march 26']="Sarita"
ref['march 23']="aadad"
print(ref.Table)
#print(ref.get_hash_value('march 26'))
