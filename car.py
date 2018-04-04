'''
Author: Daryll Osis
Date: April 04, 2018
Description: simple program that has a class and few instances. 
'''

class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        
        #this is to set the tax variable to 15% if the price of the car is greater than 10,000, otherwise, it sets it to 12% 
        if (self.price > 10000):
            self.tax =  0.15
        else:
            self.tax = 0.12
        #This just runs the display_all() everytime a new instance is added.
        print("*****************")       
        self.display_all()
        
    def display_all(self):
        print("Price: ", self.price, sep='')
        print("Speed: ", self.speed, sep='')
        print("Fuel: ", self.fuel, sep='')
        print("Mileage: ", self.mileage, "mpg", sep='')
        print("Tax: ", self.tax)

#instances of the class Car
car1 = Car(15000, 35, "full", 23)
car2 = Car(10000, 56, "almost empty", 23)
car3 = Car(11000, 32, "full", 23)
car4 = Car(9000, 70, "quarter", 23)
car5 = Car(32000, 51, "no gas", 23)
car6 = Car(8900, 23, "half", 23)

##run the instances
# print("*****************")      #the asterisks are just to separate the results
# car1.display_all()
# print("*****************")
# car2.display_all()
# print("*****************")
# car3.display_all()
# print("*****************")
# car4.display_all()
# print("*****************")
# car5.display_all()
# print("*****************")
# car6.display_all()
