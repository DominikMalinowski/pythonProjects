
class Car(object):
    wheels = 4 

    def __init__(self, make, model = '550i'):
        self.make = make
        self.model = model
    
    def info(self):
        print('Make of the car: '+ self.make)
        print('Model of the car: '+ self.model)
        print('Number of wheels: '+ str(self.wheels))

c1 = Car('bmw')
print(c1.make)
c1.wheels = 3 
print(c1.model)
c1.info()

c2 = Car('reno')
print(c2.make)
print(c2.model)
c2.info()
# %% 
class Car(object):
    def __init__(self):
        print('You create car instance')
        
    def drive(self):
        print('Car started')

    def stop(self):
        print('Car stopped')
class BMW(Car):
    def __init__(self):
        Car.__init__(self)
        print('BMW instance')

    def drive(self):
        super().drive()
        print('You are driving BMW')
    
    def heads_up_display(self):
        print('This is a unique feature')

# c = Car()
# c.drive()
# c.stop()

b = BMW()
b.drive()
b.stop()
b.heads_up_display()