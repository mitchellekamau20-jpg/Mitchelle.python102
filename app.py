# this single-line comment

name = "John Doe" # this is a variable
# firstName = input() # standard input 
# secondName = input("Enter second name: ")

secondName = 10
secondName = "Mary Peter Jane"   

output =""

"""
Multi-line comment or string
"""

"""
DATA TYPE: 
    - TEXT(strings) type: str
    - NUMBERS(integers, float, complex)
    - LIST(list, tuple, dictionary, sets)
"""

# Numbers: INT -> int()
number = 10 # integer value or 10
output = number
output = type(number) # check the data-type

number =1000000000000 
output = number

numberTwo = 2000
output = numberTwo

# Numbers: FLOAT -> float()
amount = 20.5
output = amount
output = type(amount)

# Numbers: COMPLEX -> complex()
root = -2j
output = root 
output = type(root)

# type conversion
numberTwo = 10
output = type(numberTwo)
output = numberTwo # variable overriding
numberTwo = float(numberTwo)
output = float(numberTwo) # parsing numberTwo variable into a floating point number
output = type(numberTwo)
output = int(numberTwo)
output = type(output)

output =  "120" 
output = type(output)
output = int("120")
output = type(output)

numberThree = 100
output = str(numberThree)
output = type(output)

# Text: STRING -> str()
name = "John Doe"
name = 'Jane Doe'
welcomeMessage = 'It\'s a sunny morning'
welcomeMessage = "It's a sunny morning"

output = welcomeMessage
output = type(welcomeMessage)


# string is a lists of characters
name = "Peter Parker"
output = name[4] # accessing characters sing indexes

#slicing
output = name[1:6]
output = name[1:6:2]
output = name

# string methods
output = name.upper() # changes to uppercase
output = name.lower() # changes to lowercase
output = name.startswith("b") # checks whether the first element is macthing the target
output = name.split(" ") # splits string using the space as the determinant
output = name
output = name.replace("e", "u") # replaces all occurences of the character 'e' with 'u'
output = name.replace("u", "e") # replaces all occurences of the character 'u' with 'e'
output = name.replace("Peter", "Jane")  # replaces all occurences of the word 'Peter' with 'Jane'


"""
Operators & Operands: 

For example given the equation: x + y  = 10. x and y are what we call operands
+ and = are operators. Operators allow you to perform a particular action given operands.

Operators can be grouped into types: 
 
 - Arithmetic Operators
     subraction(-)
     addition (+)
     division (/)
     multiplication (*)
     power (**)
     floor division (//)
     modulus (%)

 - Boolean Operators (and, or, not)
 - Comparison operators (less than, equal to, greater than, less than or equal to, greater than or eq)
 - bit-wise operators (&, | )
 - membership operators 
 - Assignment operators

"""

numberOne = 10
numberTwo = 20

# ARITHMETIC OPERATORS: -,+,**,/,//,%
output = numberOne - numberTwo#  subraction(-)
output = numberOne + numberTwo#  addition (+)
output = numberOne / numberTwo#  division (/)
output = numberOne * numberTwo#  multiplication (*)
output = numberOne ** numberTwo#  power (**)
output = numberOne // numberTwo#  floor division (//)' - truncation
numberOne=10
numberTwo=3
output = numberOne % numberTwo #  modulus (%)

# operation = input("Enter math problem: ")
# output = eval(operation) # this is not recommended because it may allow the user to input dangerous scripts

# BOOLEAN data type => bool()
areLightsOn = True # boolean data type
isRaining = False #boolean data types
 


"""
Comparison operators:
    - less than(<) 
    - equal to(==) 
    - not equal to(!=) 
    - greater than(>)
    - less than or equal to(<=)
    - greater than or eq (>=)
"""
x = 10 
y = 20
output = (x < y) #  less than(<)
output = (x > y) #  greater than(<)
output = type(output)
output = (x >= y) #  greater than or equal to(>=)
output = (x <= y) #  less than or equal to(<=)
output = (x == y) #  equality (==)
output = (x != y) #  not equal (!=)

# LOGIC OPERATORS (and, or, not)
age =17
year = 2026

output = ((2027 >= year ) and (age <= 18))
output = ((2027 > year ) and (age == 18))

output = not ((2027 >= year ) and (age <= 18))
output = not ((2027 >= year ) or (age <= 18))
x = 10
y = 20

## ASSIGNMENT OPERATORS: 
i = 0
x = x+1
x +=1
# i = i+1
i += 1 # same as i = i+1 => 1
i *= 3 # same as i = i*3 => 3
i /= 3 # same as i = i/3 => 1
i *=5 # same as i = i*5 => 5
i //=3 # same as i = i // 3 =>1
i = 10 
i %= 20 #same as i = i%20 => 1
output =  i 

"""
 CONDITIONAL STATEMENTS:
  - if ... else 
  - ternary operator
  - if ... elif ... else
  - match

"""
age = 18
if age > 18 :
    output = "Able to vote"
else: 
    output = "Oops! You cannot vote!"


output = "Able to vote" if age>18  else "Oops you cannot vote" # ternary operator

clothing = "t-shirt"
color = "green"

if (clothing == "t-shirt") and (color == "white"):
    output = "Buy the green T-shirt!"
else: 
    output = "Do not buy!"


clothing = "pants"
color = "black"
shoes = "white"
socks = "happy-socks"

if (clothing == "pants") and (color == "green"):
    output = "green is good but we would black for the cold!"

elif (clothing =="pants")and (shoes =="brown"):
    output = "The brown shoes are not part of the wedding theme"

elif (clothing == "pants") and socks.startswith("official"):
    output = "This is a good start!"

elif (clothing == "pants") and socks.startswith("happy") and (color == "black"):
    output = "You Nailed it!!"
else:
    output = "Oii! we are done!"
 
#  ternary operator
x = 101
output = "ten" if (x == 10)  else "not ten" # ternary operator 

# match 
color = "magenta"
match(color):
    case "green":
        output = "Green Light!"
    case "yellow":
        output = "Get Ready!"
    case "blue":
        output = "Time to swim!"
    case _: # this is the default is neither of the elements match
        output ="I am color-blind!"

age = 12  
match(age):
    case 12:
        output = "able to take Vanilla icecream"
    case 4:
        output = "cannot take alot of ice cream"
    case 1: 
        output =" do not try"
    case _:
        output = "oii drink water!"

start = 0
end  = 10 

# LOOPS: 
# print("================================")
# while loop
# while(start <= end ):
#     print("=>  ",start)
#     if start == 3:
#         break # stop the loop
#     start+=1

name = "Peter Parker" # list of characters

# for letter in name:
#     if letter == "k":
#         break
#     print(letter)

# for num in range(3,10):
#     print(num)

# print("================================")



"""
FUNCTIONS: 
serves the purpose of doing a single task
    - parameterized functions
    - non-parameterized functions
    - lambda functions
"""
# simple function: 

#  defining a function 
def greetings():
    print("Good morning!")

# greetings() # calling a function

#  parameterized function
def welcomeMessage(name):
    print("Welcome home " + name)
    print(f"Welcome home {name}"  )

def addition(x, y):
    print(x+y)

# addition(12,12)
# welcomeMessage(name="Mary")# calling the funciton
# welcomeMessage(name="Ray")# calling the funciton





# wish someone good morning
def morningGreetings():
    print("Good! Morning!")

# morningGreetings() # calling the function


def personalMorningGreetings(name, age):
    print(f"Good morning {name}! I heard you are {age} yrs old!")

# personalMorningGreetings("Andrew",12)


"""
LOGIN: 
1. FORM(UI): 
    - username
    - useemail
    - password

2. PYTHON: 
    - takes your credentials 
    - checks whether they exist
    - log you in
""" 

def login(name, email , password):
    if name == "Wanjiru":
        print("Pass")
    else:
        print("username does not exist")
    if email == "wanjiru254@example.com":
        print("pass!")
    else:
        print("email not found")
    if password == "1234556":
        print("welcome back!")
    else:
        print("wrong credentials")

def signSheet(name, signature):
    print(name)
    print(signature)

#  lambda function : => anonymous function
# lambda params: expression

x = lambda a,b : a + b

stringSize = lambda a : len(a)+1

greeting = lambda name : f"Welcome home {name}"

output = x(10,12)
output = stringSize('Amigos')
output = greeting("Wanjiru")

"""
Summary: 
 - Variables
 - Data Types
 - Loops
 - control flows
 - Functions: 
    - Anonymous(lambda)
    - Paramterized functions
    - Non-paramaterized functions
"""


print("================================")
print(output)# standard output
print("================================")