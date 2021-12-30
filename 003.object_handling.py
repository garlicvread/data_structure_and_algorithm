"""
Object Handling
Python considers everything as an object. Within the function below, You can
    1. add a parameter 'color'
    2. add a function 'speedDown'
    3. add a function 'changeColor'
    4. change a function 'wheelChange'
"""


class Car:
    def __init__(self):
        self.speed = 0
        self.year = 2017
        self.wheel = Wheel("aluminum")
        self.color = "white"
        
        
    def speedUp(self, addSpeed):
        self.speed += addSpeed
        
        
    # An object function, 'speedDown'.
    # Its function is to decrease the car speed as much as the inputted value.
    def speedDown(self, subSpeed):
        self.speed -= subSpeed
    
    
    # An object function, 'changeColor'.
    # Its function is to change the car color according to the inputted color information.
    def changeColor(self, newColor):
        self.color = newColor
        
    # An object can be used as the data of another object.
    # In case of 'Car' object, use 'Wheel' object as its parameter.
    # 'Wheel' object receives new color information of the wheel (newWheelType)
    # then create new 'Wheel' object.
    def wheelChange(self, newWheelType):
        self.wheel = Wheel(newWheelType)
    

class Wheel:
    def __init__(self, newWheelType):
        self.wheelType = newWheelType


def main():
    audi = Car()
    print("Your car has been shipped out in year {}.".format(audi.year))
    print("Your current speed is {} km/h.".format(audi.speed))
    audi.speedUp(200)
    print("The speed has been changed to {} km/h.".format(audi.speed))
    
    randomWheel = Wheel("aluminum")
    print("A wheel made of {} has been placed on the ground.".format(randomWheel.wheelType))
    
    
if __name__ == "__main__":
    main()
