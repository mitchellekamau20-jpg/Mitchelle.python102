"""
CLASS: blueprint that helps create an real object
"""

# defining a Class
class Monitor:
    # attribute
    # shape ="rectangular"
    # resolution="1080"
    # size = "large"
    # yom = 2020
    #  an initialize invoked the moment the object is created
    def __init__(self, shape, resolution,size, yom, color):
        self.shape = shape
        self.resolution = resolution
        self.size = size
        self.yom = yom 
        self.color = color 

    # methods (function taht resides inside a class)
    def switchOnMonitor(self):
        print("turning on monitor")

    def displayInterface(self):
        print("diplaying OS")

# OBJECTS: Instances of classes ("a real world thing")
# create objects
hpMonitor = Monitor("rectangular", 1080,21, 2000,"gray")
dellMonitor = Monitor(shape="oval", resolution=1280, size =34, yom =2050, color ="black" )

# hpMonitor.switchOnMonitor()
# dellMonitor.switchOnMonitor()

# print(f"===> {hpMonitor.shape}")
# print(f"===> {dellMonitor.shape}")


"""
- INHERITANCE: 
    get attributes | methods from the parent class

- ENCAPSULATION
- POLYMORPHISM
"""
#inhertance
class Vehicle: 
    # attributes: 
    def __init__(self, model, color, isElectric): 
        self.model = model
        self.color = color
        self.isElectric = isElectric

    # methods
    def carFeatures(self):
        print(f"This vehicle is of model {self.model} it is color {self.color}. Is it electric? {self.isElectric}")
    
    def startCar(self):
        print(f"Starting your {self.model} car!")

tesla = Vehicle("Tesla","Space-Gray", True)
toyota = Vehicle("Toyota", "White", False)

class Tuktuk(Vehicle): # inheritance, the parent is Vehicle an child: Tuktuk
    # attribute
    def __init__(self,model, color, isElectric,numberOfWheels):
        super().__init__(model, color, isElectric) 
        self.numberOfWheels = numberOfWheels 
    
    def wheelNumber(self):
        print(f"Your tuktuk has {self.numberOfWheels} wheels")

# redTuktuk = Tuktuk("TKTK", "RED", True,"3")

# redTuktuk.carFeatures()
# redTuktuk.wheelNumber()

#encapsulation
class Book:

    def __init__(self, title, author, yop, publisher, costOfProduction):
        self.title = title 
        self.author = author
        self.yop = yop
        self.publisher = publisher
        self.__costOfProduction = costOfProduction


    def aboutBook(self):
        print(f"TITLE: {self.title}")
        print(f"AUTHOR: {self.author}")
        print(f"Year of Publication: {self.yop}")
        print(f"PUBLISHER: {self.publisher}")
        print(f"PUBLISHER: {self.__costOfProduction}")


alchemist = Book("The Alchemist","Paulo Coelho",1988,"penguine", 250)
alchemist.aboutBook()

print("=======================")
print(f"TITLE: {alchemist.title}")
print(f"AUTHOR: {alchemist.author}")
print(f"Year of Publication: {alchemist.yop}")
print(f"PUBLISHER: {alchemist.publisher}")
# print(f"PUBLISHER: {alchemist.__costOfProduction} /=")
print("=======================")

print("***********************")
alchemist.aboutBook()
print("***********************")



# age = 10
# name = "Jane"
# output = "Mme. " + name + " is " + str(age) + "years old!"
# output = f"Mme. {name} is {age} years old!"
output = "John DOe"
output = len(output)
print(output)