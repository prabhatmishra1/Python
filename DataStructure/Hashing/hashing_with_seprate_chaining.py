class HashTable:
    def __init__(self):
        self.Size=10
        self.Table=[[] for _ in range(self.Size)]

    def get_hash_value(self, key):
        hash_vlaue=0
        for value in key:
            hash_vlaue+=ord(value)
        return hash_vlaue%self.Size   
    def __setitem__(self,key,value): #For example, operator.add(x, y) is equivalent to the expression Table[key]=value .
        hash_value=self.get_hash_value(key)
        found=False
        for index,data in enumerate(self.Table[hash_value]):
            if data[0]==key:
                self.Table[hash_value][index]=(key,value)
                found=True
                break
        if not found:            
            self.Table[hash_value].append((key,value))

    def __getitem__(self,key):
        hash_value=self.get_hash_value(key) #For example, operator.get(key) is equivalent to the expression Table[key] .
        if not self.Table[hash_value]:
            return 
        for index, data in enumerate(self.Table[hash_value]):
            if data[0]==key:
                return data[1]
        else:
            return                  

    def delete(self,key):
        hash_value=self.get_hash_value(key)
        if not self.Table[hash_value]:
            return None
        else:
            for index,data in enumerate(self.Table[hash_value]):
                if data[0]==key:
                    temp=data[1]
                    del(self.Table[hash_value][index])
                    return temp    
        
ref=HashTable()
ref['march 6']="prabhat"
ref['march 17']="Stuti"
print(ref.delete('march 17'))
print(ref.Table)
