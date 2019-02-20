'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''
class Car():
    """making a car"""

    def __init__(self, desc, model, year, maxspeed):
        """initializes car attributes"""

        self.model = model
        self.year = year
        self.desc = desc
        self.maxspeed = maxspeed


    def speedup(self, increment_by):
        self.maxspeed += increment_by

    def car_details(self):
        print(f"My {self.desc} was a  {self.model}, year {self.year} and it goes {self.maxspeed} km p/h.")


my_first_car = Car("first car", "Nissan Pulsar", 1986, 120)
my_lastest_car = Car("last car", "Subaru Forrester", 2009, 160)


my_lastest_car.speedup(5)
my_lastest_car.speedup(50)


my_first_car.car_details()
my_lastest_car.car_details()



