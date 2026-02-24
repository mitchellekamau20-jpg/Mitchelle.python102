"""
- input value 1 
- select operator (+,-,/,//,%,*)
- input value 2
- calculate
- print out the value/ solution

"""

def addition(x,y):
    valueSum = x + y
    return valueSum

print("============================================")
valueOne = input("Enter the first operand: ")
valueTwo = input("Enter the second operand: ")

operatorChoice = input(
"""
Kindly input the number of the operation you want: \n
 1. addition(+)
 2. subtraction(-)
 3. multiplication(*)
 4. division(/)
 5. power(**)
 6. floor division(divsion without decimals //)
 
""")
output = "" # global variable
operatorChoice = int(operatorChoice)
valueOne = int(valueOne)
valueTwo = int(valueTwo)


if (operatorChoice == 1):
    output = addition(valueOne, valueTwo)
elif (operatorChoice == 2):
    output = valueOne - valueTwo
elif (operatorChoice == 3):
    output = valueOne * valueTwo
elif (operatorChoice == 4):
    output = valueOne / valueTwo
elif (operatorChoice == 5):
    output = valueOne ** valueTwo
elif (operatorChoice == 6):
    output = valueOne // valueTwo
else: 
    output ="wrong selection!"

# incase you chooose a match 
match(operatorChoice):
    case 1 :
        output = valueOne + valueTwo
    case 2:
        output = valueOne - valueTwo
    case 3 :
        output = valueOne * valueTwo
    case 4:
        output = valueOne / valueTwo
    case 5:
        output = valueOne ** valueTwo
    case 6:
        output = valueOne // valueTwo
    case _:
        output = "invalid!"


print("*****************************")
print(output)
print("*****************************")

print("============================================")



##OOP
class Car: 
    #  attributes
    def __init__(self,name, color, model, size):
        self.name = name
        self.color = color
        self.model = model
        self.size = size

    # behavoirs - methods

    def carDescription(self):
       print(f"This is a {self.model} it is of color {self.color}")



toyota = Car("Buddy", "green","Toyota", "4X4")

#  accesed the attributes
output = toyota.name
output = toyota.color
output = toyota.model

#  access ythe behaviours:

toyota.carDescription()

mazda = Car("Kadogo", "blue","MAZDA - XR", "4X4")
mazda.carDescription()

output = f" FIRST CAR: {mazda.name} SECOND-CAR: {toyota.name}"
mazda.name
# INHERITANCE:  You have parent class and a child class( the child class inherits evryhitng form the parent class)

print("======================")
print(output)
print("======================")