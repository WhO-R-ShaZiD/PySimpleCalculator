"""
In this exercise module we are going to learn about how we can make a calculr by using Python Programming such as: 

"""

# Taking the Numbers from the user:

# Number: 01
num1 = int(input("Enter the First Number:\n"))

# Number: 02
num2 = int(input("Enter the Second Number:\n"))

# Printing the Numbers:
print("You Have Given the Numbers as:" + " " + " ", num1,num2)

# Calculating Part:

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2
floorDiv = num1 // num2
power = num1**2


# Printing Part:
print("Addition is: " , add)
print("Subtraction is: " , sub)
print("Multiplication is: " , mul)
print("Division is: " , div)
print("Power is: " , power)
print("Modulas is: " , mod)
print("Floor Division is: " , floorDiv)
