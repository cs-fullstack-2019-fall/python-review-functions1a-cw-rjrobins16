# Python review function introduction
#
# ### Problem 1
# Create a ```printNumbers``` function to print integers from -25 to 20 to the console (print in the function)
def printNumbers():
    for x in range(-25, 21, 1):
        print(x)
# created for loop then called the function
printNumbers()

# ### Problem 2
# Create a function called checkPassword. Send two string variables to
# the checkPassword function to check if the strings are equal.
# Return true if they are equal and false if they are not equal. Print the function's return value.
def checkPassword(first, second):
    if first == second:
        return True
    if first != second:
        return False
password = input("Enter your password.")
password2 = input("Re-enter that password.")
print(checkPassword(password, password2))

# ### Problem 3
# Write a function that determines if a number passed to it is odd or even. 
# Pass a number of your choosing (using input a good idea) and then using the result from the function, 
# print if the number was even or not.
# examples:
# ```
# The number 12 is an even number!
# The number 5 is an odd number!
def problem3(number):  # conditions check for division by 2
    if number % 2 == 0:
        return f'The number {number} is even.'
    elif number % 2 != 0:
        return f'The number {number} is odd.'
userNumberInput = int(input("Enter a number to see if it's even or odd."))  # enter number to check even or odd
print(problem3(userNumberInput))  # prints function's return

# ### Problem 4
# * Create a function for the challenge that you call from your ```main```
# * Create a *second* function that takes NO parameters
# * Create a *third* function that takes a single greeting parameter (ex. ```Howdy```)
# and returns a string using the passed in greeting and 'World' (ex. ```Howdy World!```)
# * From your *first* function, call the function(s) and print out the final result returned
def main():
    print(first())
def first():
    return second("Hello ")  # inputs hello into the greeting function
def second(greeting):
    return greeting + "World"
main()

# ### Problem 5:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter
# 'q', ask them to input another string.
def function5():
    userInput = 1  # declares variable
    userInput = input("Enter a word or q to quit.")
    while userInput != "q":
        userInput = input("Enter a word or q to quit.")
# basic while loop that im tired of doing lol :)
function5()

# Challenge
# Create a function that accepts 2 numbers. 
# When the function is called return the sum, difference, product, and quotient as 4 separate return values.
# Print the 4 results that are returned using f-strings.
# Example: If 2 and 6 are passed into the function, output should be similar to the following:
# The sum of 2 + 6 is 8
# The difference of 2 - 6 is  -4
# The product of 2 * 6 is 12
# The quotient of 2 / 6 is .333
def challenge(number1, number2):
    sumofnum = f'The sum of {number1} + {number2} is {number1 + number2}'  # add the numbers
    difference = f'The difference of {number1} - {number2} is {number1 - number2}'  # subtract numbers
    product = f'The product of {number1} * {number2} is {number1 * number2}'  # multiply numbers
    quotient = f'The product of {number1} / {number2} is {number1 / number2}'  # divides numbers
    return sumofnum, difference, product, quotient  # returns the mini equation statements
# f strings that print the smaller math functions
challengenumber1 = int(input("Enter a big number."))  # accepts a number
challengenumber2 = int(input("Enter a lesser number."))  # accepts another number
print(challenge(challengenumber1, challengenumber2))  # prints the function return with the inputted numbers
