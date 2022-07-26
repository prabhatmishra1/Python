class Vehicle:
    """This is Vehicle class """

    def __init__(self):
        self.name = "Ram"
        self.max_speed = 1200
        self.mileage = 55
        Vehicle.color = "white"
    
    def work(self):
        self.spin = "good"
    
    def seating_capacity(self, capacity):
        self.capacity = capacity

    def fare(self):
        print((self.capacity*100))
    

class Bus(Vehicle):
    "This is BUS class"

    def __init__(self):
        self.driver = "GK"
        self.route = "KV"
        super().__init__()
    
    def add_extra(self):
        return (self.capacity*100)*10/100
    
    def fare(self):
        print((self.capacity*100)+self.add_extra())
    
    def test(self):
        print(self.name)
        print(self.driver)

ref = Bus()
print(ref.test())


