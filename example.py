a = 10
b = 5
c = a -b
print("Substraction of two numbers:",c)

def add(a, b, c):
    print(a)
    print(b)
    print(c)
    d = a * b * c
    print(d)
add(5, 8, 5)
add(2, 3, 4)

def my_function(fname):
  print(fname + " Patil")

my_function("Santosh")
my_function("Amit")
my_function("Vaishali")

class CarModel: #classname
    name = "BMW" #variable
    gear = 5
    def run(self):   #functions
        print("Car gear is:- ", self.gear)
        print("car name is:- ", self.name)
    def gear1(self):
        print("car gear is:- ", self.gear)
car_obj = CarModel() #create the the object
print(car_obj.name)
car_obj.run() #with the help object, call the function.
car_obj.gear1()