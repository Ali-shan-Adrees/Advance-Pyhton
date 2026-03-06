#-1 Three line story
print("The old house had been empty for years. \n"
      "One night, a single light appeared in the top window.\n"
      "Nobody dared to go up and check it" )

# 2-The Border:
print("**********")
print("* PYTHON *")
print("**********")

# 3-The Separator

print("1 ","2 ","3 ","4 ","5 ",sep="-> ")

# 4-The  End Game

print("The old house had been empty for years." ,end='')
print("One night, a single light appeared in the top window."
      )


# 5-The Formatter: Print a decimal number (like 12.34567) rounded to exactly two decimal
# places using an f-string.

num=12.34567
print(f"num is {num:.2f}")

# 6- The Greeter: Ask for a name and a favorite color, then print: "Hi [Name], [Color] looks
# great on you!

name=input("Name Enter your name:")
col= input("Enter your fav color:")
print(f"Hi {name}, {col} looks great on you!")

# 7- The Age Gap: Ask for the user's age and print how old they will be in the year 2050.
from datetime import date

from oauthlib.oauth1.rfc5849.signature import verify_rsa_sha1

current_year = date.today().year
age=int(input("Enter your Age"))
age_in_2050=(2050-current_year)+age
print(f"You Age At 2050 will be {age_in_2050}")

# 8- The Multiplier: Ask for two numbers, multiply them, and print the result. (Watch out for
# string vs. integer errors!)

try:
    num1=int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    mul=num1*num2
    print(f"Number 1 x Number 2 ={mul}")
except ValueError:
    print("Please enter an  Integer")

# 9-Ask for a word and a number, then print that word as many times as the
# number specifies

word=str(input("Enter any word :"))
num=int(input("Enter any number: "))
print(f"{word*num} ")

# 10-Ask for a total bill amount and the number of people. Print how much
# each person owes.

total_bill=int(input("Enter total bill: "))
people=int(input("Enter people: "))
each=print(f"Bill for each person will be {total_bill/people}")

# 3. Operators
# Focus: Arithmetic logic and remainders.
# 1. The Remainder: Ask for two numbers and print only the remainder when the first is
# divided by the second.

num1=int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
div = num1%num2
if num1%num2==0:
    print(div)
else:
    print("Remainder is not equal to 0")


# 2. The Power: Write a program that calculates $x^y$ where $x$ and $y$ are user inputs.

num1=int(input("Enter a number x: "))
num2 = int(input("Enter another number y: "))
power=num1**num2
print(f"x ^ y ={power}")


# 3. The Floor: Perform "floor division" on two numbers and explain why the result is an
# integer.


num1=int(input("Enter a number : "))
num2 = int(input("Enter another number : "))

floor_div=num1//num2
print(f"Floor division{floor_div} ")

div=num1/num2
print(f"Simple division{div} ")


# 4. The Comparison: Ask for a number and print True if it is greater than 100 and False
# otherwise (without using an if statement).

num = int(input("Enter a number: "))
print(num > 100)


# 5. The Swapper: Use operators to swap the values of two variables $a$ and $b$ without
# using a third temporary variable.

a  = int(input("Enter a number: "))
b  = int(input("Enter a number: "))

a, b = b, a

print(f"a is now: {a}")
print(f"b is now: {b}")

# 4. Variables
# Focus: Naming conventions and reassignment.
# 1. The Scoreboard: Create a variable score starting at 0. Update it by 10, then decrease it
# by 3, and print the final value.


score=0
score=score+10
score=score-3
print(score)

# 2. The Constant: Create a variable for PI (3.14159) and calculate the area of a circle
# based on a user-provided radius.

PI =3.14159
rad= int(input("enter the radius of the circle"))
area=PI*rad**2
print(f"Area of the circle is {area}")

# 3. The Concatenator: Store a first name and a last name in different variables, then
# combine them into a full_name variable.

name1= input("Enter your 1st name: ")
name2=input("Enter your 2nd name: ")

print(name1+name2)

# 4. The Type Checker: Create three variables (a string, an integer, and a float) and print the
# type() of each.

var1 = "ali"
var2=12
var3=34.12
print(type(var1))
print(type(var2))
print(type(var3))



# 5. The Dynamic Type: Assign a number to a variable, print it, then assign a string to that
# same variable and print it again.

var1=112
var1="Ali"
print(var1)


# 5. IF / ELSE
# Focus: Conditional logic and branching.
# 1. Odd or Even: Ask for a number and tell the user if it is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")




# 2. The Grade Book: Take a score (0-100) and print "A" for 90+, "B" for 80+, and "F" for
# anything below 60.

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")

# 3. The Bouncer: Ask for a user's age. If they are 18 or older, say "Enter"; otherwise, tell
# them how many years they have to wait.


age = int(input("Enter your age: "))
if age >= 18:
    print("Enter")
else:
    wait = 18 - age
    print("You must wait", wait, "years")

# 4. The Password: Create a "secret password" variable. Ask the user for input; if it
# matches, print "Access Granted."

secret_password = "python123"

user_input = input("Enter password: ")

if user_input == secret_password:
    print("Access Granted")
else:
    print("Access Denied")

# 5. Leap Year: Ask for a year and determine if it is a leap year (divisible by 4 but not 100,
# unless divisible by 400).



year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 6. Loops
# Focus: Iteration and termination.
# 1. The Countdown: Use a while loop to count down from 10 to 1 and then print "Blast off!"

count = 10

while count >= 1:
    print(count)
    count -= 1

print("Blast off!")
# 2. The Multiples: Use a for loop to print the first 10 multiples of 5.
for i in range(1, 11):
    print(i * 5)


# 3. The Accumulator: Write a loop that asks the user for numbers until they type "0", then
# print the total sum of all numbers entered.

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    total += num

print("Total sum:", total)


# 4. The Searcher: Loop through a string and count how many times the letter "a" appears.

text = input("Enter a string: ")

count = 0

for letter in text:
    if letter == 'a':
        count += 1

print("Number of 'a':", count)

# 5. The Breakout: Write an infinite loop that only stops (break) when the user types the
# word "stop".

while True:
    word = input("Type something (type 'stop' to end): ")

    if word == "stop":
        break

# 7. Data Structures (Lists/Tuples/Dicts)
# Focus: Storage and retrieval.

grocery = ["Bread", "Eggs", "Butter", "Rice", "Juice"]

grocery[1] = "Milk"     # replace second item
grocery.pop()           # remove last item

print(grocery)

# 1. The Grocery List: Create a list of 5 items. Replace the second item with "Milk" and
# remove the last item.

grocery = ["Bread", "Eggs", "Butter", "Rice", "Juice"]

grocery[1] = "Milk"     # replace second item
grocery.pop()           # remove last item

print(grocery)


# 2. The Slicer: Given a list of 10 numbers, print only the middle four numbers using slicing.

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[3:7])  # middle four numbers


# 3. The Dictionary: Create a dictionary of a "Phone Book" with 3 names and numbers. Print
# only the phone number of a specific name.

phone_book = {
    "Ali": "03001234567",
    "Ahmed": "03111234567",
    "Sara": "03221234567"
}

print(phone_book["Ali"])

# 4. The Unique List: Given a list with duplicate numbers, create a new list (or set) that
# contains only the unique values.5. The Coordinator: Create a tuple representing coordinates $(x, y)$. Try to change the
# $x$ value and explain why Python throws an error.

numbers = [1,2,2,3,4,4,5,6,6,7]

unique_numbers = list(set(numbers))

print(unique_numbers)
# 8. NumPy (Multidimensional & Indexing)
# Focus: Array shapes and accessing data.
# 1. The Matrix: Create a $3 \times 3$ NumPy array containing the numbers 1 through 9.

import numpy as np

matrix = np.arange(1, 10).reshape(3,3)

print(matrix)
# 2. The Corner: From a $4 \times 4$ array, use indexing to extract the value in the top-right
# corner.

import numpy as np

arr = np.arange(1,17).reshape(4,4)

print(arr)

top_right = arr[0,3]

print("Top right value:", top_right)
# 3. The Row Picker: Create a $5 \times 5$ array of random numbers and print only the 3rd
# row.

import numpy as np

arr = np.random.rand(5,5)

print("Array:\n", arr)

print("Third row:\n", arr[2])
# 4. The Sub-Grid: From a $6 \times 6$ array, extract a $2 \times 2$ "sub-matrix" from the
# center.
import numpy as np

arr = np.arange(1,37).reshape(6,6)

print(arr)

sub_matrix = arr[2:4, 2:4]

print("Center 2x2 matrix:")
print(sub_matrix)

# 5. The Zero-Out: Create a $3 \times 3$ identity matrix (1s on the diagonal) and use
# indexing to change the center value to 10.

import numpy as np

arr = np.eye(3)

print("Original matrix:")
print(arr)

arr[1,1] = 10

print("Modified matrix:")
print(arr)