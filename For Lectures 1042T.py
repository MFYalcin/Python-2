#Set Tuples Done

a_list = [0, 1, 0]
size_list = len(a_list)
a = a_list[0]
a_list.append(2)
a_list.append(2)
    
a_set = {0, 1, 0}
#a = a_set[0]
size_set = len(a_set)
a_set.add(2)
a_set.add(2)
 
for i in a_list:
    print (i,end=",")
print ()
for i in a_set:
    print (i,end=",")
    

##
    
a_list = [0, 1, 0]
b_list = [0, 0, 1]

a_set = {0, 1, 0}
b_set = {1, 0}

if ( a_list == a_set ):
    print ("1")
elif ( a_set == b_set):
    print ("2")
elif (a_list == b_list):
    print ("3")
elif ( b_list == b_set):
    print ("4")
else:
    print ("5")


##

a_list = [0, 1, 0]

a_tuple = (0, 1, 0)

c = a_tuple[1]
a_list[0] = c*2
# a_tuple[0] = c*2

##

def symmetric_about_x (x, y ) -> tuple:
    """
    returns the symmetric point aboutthe x axis:
    >>> symmetric_about_x ( 3, 5 )
    (3, -5)
    >>> symmetric_about_x ( -3, 5 )
    (-3, -5)
    >>> symmetric_about_x ( 3, -5 )
    (3, 5)
    >>> symmetric_about_x ( 0, 0 )
    (0, 0)
    """
    return (x,-y)
                             
eg1 = symmetric_about_x ( 3, 5 )
eg2 = symmetric_about_x ( -3, 5 )
eg3 = symmetric_about_x ( 3, -5 )
eg4 = symmetric_about_x ( 0, 0 )

x1, y1 = symmetric_about_x ( 3, 5 )
x2, y2 = symmetric_about_x ( -3, 5 )
x3, y3 = symmetric_about_x ( 3, -5 )
x4, y4 = symmetric_about_x ( 0, 0 )

print (eg1, x1, y1)
print (eg2, x2, y2)
print (eg3, x3, y3)
print (eg4, x4, y4)

##

import math

def quad_root (a:int , b:int , c:int ) -> tuple:
    """
    returns the two roots of the quadratic:
    ax^2 + bx +c
    >>> quad_root(0, 1, 2)
    (-math.inf, math.inf)
    
    >>> quad_root(2, 1, 2)
    (None, None)
    
    >>> quad_root(2, 4, 2)
    (-1.0, -1.0)
    
    >>> quad_root(1, -6, 8)
    (4.0, 2.0)
    
    """
    if a == 0:
        return (-math.inf, math.inf)
    disc = b**2 - 4*a*c
    if disc < 0:
        return (None, None)
    sqrt_disc = math.sqrt(disc)
    two_a = 2* a
    return ((-b+sqrt_disc)/two_a, (-b-sqrt_disc)/two_a)

equ_1 = quad_root(0, 1, 2)
equ_2 = quad_root(2, 1, 2)
equ_3 = quad_root(2, 4, 2)
equ_4 = quad_root(1, -6, 8)

(root1,root2) = quad_root(0, 1, 2)
(root3,root4) = quad_root(2, 1, 2)
(root5,root6) = quad_root(2, 4, 2)
(root7,root8) = quad_root(1, -6, 8)

##

import math

def quad_root (a:int , b:int , c:int ) -> set:
    """
    returns a set of the two roots of the quadratic:
    ax^2 + bx +c
    >>> quad_root(0, 1, 2)
    {-math.inf, math.inf}
    
    >>> quad_root(2, 1, 2)
    {None}
    
    >>> quad_root(2, 4, 2)
    {-1.0}
    
    >>> quad_root(1, -6, 8)
    {4.0, 2.0}
    
    """
    if a == 0:
        return {-math.inf, math.inf}
    disc = b**2 - 4*a*c
    if disc < 0:
        return {None, None}
    sqrt_disc = math.sqrt(disc)
    two_a = 2* a
    return {(-b+sqrt_disc)/two_a, (-b-sqrt_disc)/two_a}

equ_1 = quad_root(0, 1, 2)
equ_2 = quad_root(2, 1, 2)
equ_3 = quad_root(2, 4, 2)
equ_4 = quad_root(1, -6, 8)

##

# Import and Modules Done ( from root import quad_root ) 

# Practice Checkerboard

RED = "R"
BLACK = "B"

checkers = [[BLACK] * 8 for i in range(8)]

for i in range(8):
    for j in range(8):
        if (i+j) % 2 != 0:
            checkers[i][j] = RED

for i in range(8):
    for j in range(8):
        print(checkers[i][j], end=' ')
    print()
print()








# Dictioneries

#d = {19:44,13:22}
#print(d[19]) #44
#print(d.get(13)) #22
#print(d[3]) #Error
#print((d.get(3))) #None
#Keys should be unique, not values
# dic = {1:'hello',2:'hello'}



# Without dict
RED = "R"
BLACK = "B"
KING = "K"
QUEEN = "Q"
BISHOP = "B"
ROOK = "R"
KNIGHT = "N"
PAWN = "P"

board = [[BLACK] * 8 for i in range(8)]

for i in range(8):
    for j in range(8):
        if (i+j) % 2 != 0:
            board[i][j] = RED

board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)

def get_position(colour, rank):
    for i in range(8):
        for j in range(8):
            if board[i][j] == (colour, rank):
                return (i, j)
    return None

print(get_position(RED, QUEEN))
print(get_position(BLACK, KNIGHT))


#With dict

RED = "R"
BLACK = "B"
KING = "K"
QUEEN = "Q"
BISHOP = "B"
ROOK = "R"
KNIGHT = "N"
PAWN = "P"

board = {(RED, QUEEN):(0,0), (BLACK, KNIGHT):(7,7)}

def get_position(colour, rank):
    return board.get((colour, rank))

print(get_position(RED, QUEEN))
print(get_position(BLACK, KNIGHT))


# create a dictionary
              #Keys  #Values
video_games = {101: ("Resident Evil", 1996),
               102: ("Sonic the Hedgehog", 1991),
               103: ("Super Mario 2", 1993),
               104: ("Super Mario 64", 1996),
               105: ("Final Fantasy VII", 1996)}

# get a key's value
name = video_games[101]
year = video_games.get(101)

# get an element from key's value
name = video_games[101][0]
year = video_games.get(101)[1]

#get a list of all keys
keys = video_games.keys()
for key in keys:
    print (key)

#get a list of all values
values = video_games.values()
for value in values:
    print (value)
#get a list of all items (key:value pairs)
items = video_games.items()
for item in items:
    print(item)

#Update an item 
video_games.update({105: ("Final Fantasy VII", 1997)})

#Update items (if key doesn't exist, add to the dictionary)
video_games.update({105: ("Final Fantasy VII", 1997), 106:("Donky Kong Country", 1994)})



# Text Icrementing 

#String Split

txt = "welcome to the jungle"
x = txt.split()
print(x)
['welcome', 'to', 'the', 'jungle']

##
#String Strip
#!/usr/bin/python

str = "0000000this is string example....wow!!!0000000";
#print str.strip( '0' )
#When we run above program, it produces following result −

#this is string example....wow!!!



##

# String Punctuation
#https://docs.python.org/2/library/string.html

##

#Simple One-by-One:
word = word.strip(string.punctuation)
word = word.lower()
# Compound Big-Bang:
word = word.strip(string.punctuation).lower()
##

#Python list sort
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)
#['BMW', 'Ford', 'Volvo']

##
# Set to list
Input : {1, 2, 3, 4}
Output : [1, 2, 3, 4]

Input : {'Geeks', 'for', 'geeks'}
Output : ['Geeks', 'for', 'geeks']

 
Approach #1 : Using list(set_name).

#Typecasting to list can be done by simply using list(set_name).

# Python3 program to convert a 
# set into a list
my_set = {'Geeks', 'for', 'geeks'}
  
s = list(my_set)
print(s)
#Output:

['Geeks', 'for', 'geeks']

 

# Python3 program to convert a 
# set into a list
def convert(set):
    return list(set)
  
# Driver function
s = set({1, 2, 3})
print(convert(s))
#Output:

[1, 2, 3]
##

# Chess board using list
RED = "R"
BLACK = "B"
KING = "K"
QUEEN = "Q"
BISHOP = "B"
ROOK = "R"
KNIGHT = "N"
PAWN = "P"

board = [[BLACK] * 8 for i in range(8)]

for i in range(8):
    for j in range(8):
        if (i+j) % 2 != 0:
            board[i][j] = RED

board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)

def get_position(colour, rank):
    for i in range(8):
        for j in range(8):
            if board[i][j] == (colour, rank):
                return (i, j)
    return None

print(get_position(RED, QUEEN))
print(get_position(BLACK, KNIGHT))
##

RED = "R"
BLACK = "B"
KING = "K"
QUEEN = "Q"
BISHOP = "B"
ROOK = "R"
KNIGHT = "N"
PAWN = "P"

board = {(RED, QUEEN):(0,0), (BLACK, KNIGHT):(7,7)}

def get_position(colour, rank):
    return board.get((colour, rank))

print(get_position(RED, QUEEN))
print(get_position(BLACK, KNIGHT))

##



#Unit Testing
#Fibonacci

def fibonacci(n: int) -> int:
    '''Return the Fibonacci number F_n for positive
    values of n, where F_1 = 1, F_2 = 1,
    and F_n = Fn-1 + F_n-2, n > 2
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3) -> 2
    >>> fibonacci(7) -> 13
    '''
    a = 1
    b = 1
    for i in range (1, n + 1):  # Bug! 2nd argument should be n
        a, b = b, a+b
    return a
    
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(7))

##
#https://wiki.python.org/moin/UnitTests

##



#....


#Nested Loops

n=4 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
1
12
123
1234

'''

#range(1,1) = None

n=4 
for i in range(1,n+1):
    for j in range(1,i):
        print(j,end=' ')
    
        
'''

1
12
123
'''


# Chessboard Example

RED = "R"
BLACK = "B"
KING = "K"
QUEEN = "Q"
BISHOP = "B"
ROOK = "R"
KNIGHT = "N"
PAWN = "P"

# wrong way

board = [[None] * 8] * 8
print("All", board)

board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)

print("All 2", board)


# right way - 1 Using nested loops

board = [None] * 8
for i in range(8):
    board[i] = [None] * 8
    
board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)

print("All 3", board)

# right way - 2 Using Generator

board = [[None] * 8 for i in range(8)]
    
board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)

print("All 4", board)


def get_piece(x,y):
    return board[x][y]
    
print("The piece at (7,7) is", get_piece(7,7))


def get_number_pieces(colour):
    num = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] != None:
                c,r = board[x][y]# or c = board[x][y][0]
                if (c == colour):
                    num += 1
    return num
    
def get_winner():
    num_black = get_number_pieces(BLACK)
    num_red = get_number_pieces(RED)
    
    if num_black == num_red:
        return "T"
    elif num_black < num_red:
        return RED
    else:
        return BLACK

print(get_winner())


##

# Version 1 (Poor)

ecor1042 = [["100123456", 8, 9, 0, 5, None],
            ["101987654", 3, 8, 8, 7, None]]
            
for student in range(len(ecor1042)):
    total = 0
    for quiz in range(1, 5):
        total += ecor1042[student][quiz]
    print(total)
    ecor1042[student][5] = total / 4
    
print(ecor1042)

# Version 2 - With sub-lists

ecor1042 = [["100123456", [8, 9, 0, 5], None],
            ["101987654", [3, 8, 8, 7], None]]
            
for stNum in range(len(ecor1042)):
    total = 0
    student = ecor1042[stNum]
    quizzes = student[1]
    for quiz in range(len(quizzes)):
        # (also works with) for quiz in quizzes:
                              #total += quiz
        total += quizzes[quiz]
    print(total)
    student[2] = total / len(quizzes)

print(ecor1042)


# Version 3 - With tuples, but with a hidden range
    # Remember tuples are immutable!

ecor1042 = [("100123456", [8, 9, 0, 5], None),
            ("101987654", [3, 8, 8, 7], None)]
            
for stNum in range(len(ecor1042)):
    total = 0
    student = ecor1042[stNum]
    num, quizzes, average = student
    for quiz in range(len(quizzes)):
        total += quizzes[quiz]
    print(total)
    average = total / len(quizzes)
    ecor1042[stNum] = (num, quizzes, average)
    print(average)
    # without this line, the average is not updated in the list
print(ecor1042)

# Dictionary Version

ecor1042 = {"100123456":[[8, 9, 0, 5], None], "101987654":[[3, 8, 8, 7], None]}
for student in ecor1042:
    
##
    
    
# Numeric Algorithyms

# Numerical Analysis
#https://en.wikipedia.org/wiki/Numerical_analysis
#root_x = math.sqrt(x)


#Exhaustive Enumeration

#def exhaustive_sqrt(x:float)->float:
    EPSILON = 0.01
    step = EPSILON **2
    guess = 0.0
    num_guesses = 0
    while abs(guess**2-x)>=EPSILON and guess <= x:
        guess += step
        num_guesses += 1
        
    print('# of guesses =',num_guesses) # Debug statement
    if guess > x:
        return None
    else:
        return guess



##
    
#Bisection Method

def bisection(x:float)->float:
    EPSILON = 0.01
    num_guesses = 0
    low = 0.0 #Window = [low,high]
    high = x
    guess = (low + high) / 2
    while abs(guess ** 2 - x) >= EPSILON:
        print('low =', low, 'high =', high, 'guess =', guess)
        num_guesses += 1
        if (guess ** 2 <x):
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    
    print('# of guesses =', num_guesses)
    return guess

##


    
#Heron's Algorithm

def heron(x:float) ->float:
    EPSILON = 0.00001
    guess = 1
    num_guesses = 0
    while abs(guess *guess -x) >EPSILON:
        guess = (guess + x /guess) /2
        num_guesses += 1
        
    print('# of guesses =', num_guesses)
    return guess

##

# Root Finding General problem
# Exhaustice Enumaration

def exhaustive_x3_x2_2(guess:float, max_guess:float)->float:
    EPSILON: 0.01
    step = EPSILON / 2
    func_sol = guess **3 -guess **2 -2 
    while abs(func_sol) >= EPSILON and guess <= max_guess:
        guess += step
        func_sol = guess ** 3 - guess ** 2 - 2
        
    if guess > max_guess:
        return None
    else:
        return guess
    #>>>exhaustive_x3_x2_2(0,10)
    #   1.6949999999999859
    
##

# Bisection Search

import numpy

def bisection_x3_x2_2(guess_l:float,guess_h:float)->float:
    EPSILON = 0.01
    #Window = [guess_l,guess_h]
    guess = (guess_l + guess_h) / 2
    func_g_l = guess_l **3-guess_l**2-2
    func_g_h = guess_h **3-guess_h**2-2
    func_g = guess**3-guess**2-2
    while abs(func_g) >= EPSILON:
        print('low =',guess_l,'high =',guess_h,'guess =',guess)
        if (numpy.sign(func_g) == numpy_sign(func_g_l)):
            guess_l = guess
            func_g_l = func_g
        else:
            guess_h = guess
            func_g_h = func_g
        guess = (guess_l + guess_h) / 2
        func_g = guess**3 - guess**2 - 2
    return guess







# Sorting Elements

# Selection Sort

def SelectionSort(A):
    #Traverse through all array elements
    for i in range(len(A)):
        
        #Find the minimum element in remaining
        #Unsorted array
        min_idx = i
        for j in range(i+1,len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        
        #Swap the found minimum element with the first element
        A[i],A[min_idx] = A[min_idx],A[i]

##

# Bubble Sort

def bubbleSort(arr):
    n=len(arr)
    #Traverse through all array elements
    for i in range(n):
        #Last i elements are already in place
        for j in range(0,n-i-1):
            #traverse the array from 0 to n-i-1
            #Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
          
##
                
x = 'Hello'
y = 'HEllo'

if x > y: 
    print('Y') # Y is printed by ASCII
elif x == y:
    print('N')
else:
    print(None)
                
##
                
# Insertion Sort

def insertionSort(arr):
    #Traverse through 1 to len(arr)
    for i in range(1,len(arr)):
        key = arr[i]
        #Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
        
        
##
        

#[3,2|,5,4] -> [2,3,5|,4] -> [2,3,4,5]



##
        
# Merge Sort

def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr) //2 # Finding the mid of array
        L = arr[:mid] # Dividing the array elements
        
        #into 2 halves
        R = arr[mid:]
        mergeSort(L) #Sorting the first half
        mergeSort(R) #Sorting the second half
        
        i=j=k=0
        
        #Copy data to temp arrays L[] and R[]
        while i<len(L) and j<len(R):
            if L[i] < R[i]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
            
            #Checking if any element was left
            while i<len(L):
                arr[k] = L[i]
                i+=1
                k+=1
            while j<len(R):
                arr[k] = R[j]
                j+=1
                k+=1
                
                
##
                
# Interactive Calculator
# Limited error handling
# It is to demontrate UI
'''
This is calculator.py which we are going to import to other UI file
list_of_supported_operators = ['+','*']

def add(op1:int, op2:int)->int:
    return op1 + op2

def multiply(op1:int, op2:int)->int:
    return op1 * op2


def execute_command(command:tuple)->int:
'''
'''
    Return the result of the execution of the given command tuple in the form (operator,op1,op2)
    Return None if the operator is not recognized
    >>>execute_command('+',10,20)
    30
    >>>execute_command('*',10,20)
    200
    >>>execute_command('-',10,20)
    None
####   
    operator, op1, op2 = command
    
    if operator == '+':
        return add(op1,op2)
    elif operator == '*':
        return multiply(op1,op2)
    else:
        None
'''       
# Another Version

dict_operator_function = {'+':add,'*':multiply}
def execute_command(command:tuple)->int:
    operator,op1,op2 = command
    func = dict_operator_function.get(operator)
    return func(op1,op2)


##
#UI part 1

from calculator import *

def get_command()->tuple:
    '''
    Prompts the user for a legal command, returning a tuple
    (operator,op1,op2)
    '''
    operator = input('Please enter an operator (+ or *): ')
    
    while len(operator) != 1 and operator not in list_of_supported_operators:
        operator = input('Illegal Format\nPlease enter an operator (+ or *): ')
    
    op1 = input('Please enter the first integer operand: ')
    op1 = int(op1) # No error handling shown
    
    op2 = int(input('Please enter the second operand: ')) # No error handling shown
    
    return (operator,op1,op2)

#Main Script
# We are not checking if the user enters anything other than Y or N

more = 'Y'

while more.upper() == 'Y':
    command = get_command()
    result = executed_command(command)
    print(command, ' = ', result)
    
    more = input('Shall we go again? Y or N: ')
#UI is not very useful in the case of program testing
# Thats why we use batch UI

# calculator_batch.txt file is created for automated testing 
'''
+ 1 2
+ 3 5
* -8 9
+ -7 9
+ 7 -9
* 1 0
'''
from calculator import *

filename = 'calculator_batch.txt'
batch_file = open(filename)
for line in batch_file:
    items = line.split(' ') # Automatically creates a list of items
    command = (items[0], int(items[1]), int(items[2]))
    
    result = execute_command(command)
    print(command, ' = ', result)
    
batch_file.close()
'''
Sample output
('+', 1, 2) = 3
('+', 3, 5) = 8
('*', -8, 9) = -72
('+',-7,9) = 2
///
'''

##

# General Interpolation
numpy.polyfit(x,y,deg)
ax+b

#Quadratic Interpolation
ax^2+bx+c

#First order - 2 data
#Seconmd order - 3 data
#...

#x 0 1
#y 2 3
import numpy as np
x = [0,1] #or range(1,10)
y = [2,3]
z = np.polyfit(x,y,1)
print(z)
#y = ax+b
#x 0 1 2
#y 2 3 2

x2 = [0,1,2]
y2= [2,3,2]
z2 = np.polyfit(x,y,2)
print(z2)


#Regression
'''
#x y 
#1 5.47
#2 7.08
#3 8.36
///
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,3,3)
y = [5.47,7.08,8.36]
plt.scatter(x,y)
plt.show()

#Error in the approximation
#Best Fit
# Least-squares regression(linera,quadratic,etc.)
#x 0 1 2 3 4
#y 2 3 5 4 6

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,4,5)
y = [2,3,5,4,6]
deg= 1
coef = np.polyfit(x,y,deg)
print(coef)

plt.scatter(x,y)
plt.show()


##

#x 0 1 2 3 4
#y 2 3 5 4 6

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,4,5)
y = [2,3,5,4,6]
deg= 1
coef = np.polyfit(x,y,deg)
print(coef)
x_e = np.linspace(0,4,100)
y_e = np.polyval(coef,x_e)

plt.plot(x,y,'o',x_e,y_e,'-')
plt.show()

##

#x 0 1 2 3 4
#y 2 3 5 4 6

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,4,5)
y = [2,3,5,4,6]
deg= 2
coef = np.polyfit(x,y,deg)
print(coef)
x_e = np.linspace(0,4,100)
y_e = np.polyval(coef,x_e)

ply.plot(x,y,'o',x_e,y_e,'-')
plt.show()



# ECOR1402 - Topic 11 - Optimization Algorithms (Minimization - Maximization ) with Python
# One-Dimensional Optimization Example 1 Step 1
import numpy as np

def Object_Height(v0,r,t):
    '''
    Returns the calculated height of an object shot vertically
    inputs:
    v0 = initial velocity (in m/s)
    r = drag coefficient  (in 1/s). cannot be zero
    t = time (in s)
    '''
    if (r == 0):
        print('Zero drag coefficient are not allowed')
    else:
        g = 9.81
        
    return ((1/r)*(v0 + g/r)*(1- np.exp(-r * t)) - (g*t)/r)

##
# One-Dimensional Optimization
#Example 1 Step 2
# Better Version
import numpy as np
import matplotlib.pyplot as plt

v0 = 78
r = 0.35

def Object_Height(v0,r,t):
    if r == 0:
        print('Zero drag coefficient are not allowed')
    else:
        g = 9.81
        
    return ((1/r)*(v0 + g/r)*(1- np.exp(-r * t)) - (g*t)/r)    

t = np.linspace(0,12,100)
h = ObjectHeight(v0,r,t)

plt.plot(t, h)
plt.grid()
plt.show()

# Poor Version

import numpy as np
import matplotlib.pyplot as plt

v0 = 78
r = 0.35

def Object_Height(v0,r,t):
    if r == 0:
        print('Zero drag coefficient are not allowed')
    else:
        g = 9.81
        
    return ((1/r)*(v0 + g/r)*(1- np.exp(-r * t)) - (g*t)/r)    

t = np.linspace(0,12,100)
h = np.ones(len(t))
for k in range(1,len(t)):
    h[k] = ObjectHeight(v0,r,t[k])
    
plt.plot(t, h)
plt.grid()
plt.show()


# Part 1, When will be the object 80m above the ground?

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

v0 = 78
r = 0.35
G = 9.81

def root_fun_4(r,v0,t,desired_h):
    return ((1/r)*(v0 + g/r)*(1- np.exp(-r * t)) - (g*t)/r) - desired_h

h = 80
def root_fun(t):
    return (root_fun_4(r,v0,t,h))

x1 [0.1,2]
time1 = fsolve(root_fun, x1)
print(time1) # will give time 1 - 1.4520
x2 = [6,8]
time2 = fsolve(root_fun,x2)
print(time2) # will give time2 - 7.0315


t = np.linspace(0,12,100)
h_desired = root_fun_4(r,v0,t,h)
plt.plot(time1[0],time2[0],[0,0],'o')
plt.plot(t,h_desired)
plt.grid()
plt.show()


# Part 2 - When will the object hit the ground?

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

v0 = 78
r = 0.35
G = 9.81

def root_fun_4(r,v0,t,desired_h):
    return ((1/r)*(v0 + g/r)*(1- np.exp(-r * t)) - (g*t)/r) - desired_h


def root_fun(t):
    return (root_fun_4(r,v0,t,h))

x3 = [10,12]
time3 = fsolve(root_fun,x3)
print(time3) # will be time3 = 10.5378

t = np.linspace(0,12,100)
h = 0 # when the object hits the ground
h_desired = root_fun_4(r,v0,t,h)

plt.plot(time3[0],0,'o')
plt.plot(t,h_desired)
plt.grid()
plt.show()
         
   
   
# Part 3 - What maximum height will be attained? - Option 1

import numpy as np
from scipy.optimize import fsolve

def func(t):
    g = 9.81 # Previously only defined in the function
    return ((1/r)*(v0 + g/r)*(1- np.exp(-r * t)) - (g*t)/r) - desired_h

tmax = fsolve(func, ([3,5])) # will return tmax= 3.8014
t = np.linspace(0,12,100)
maxHeight = ObjectHeight(v0 ,r,tmax) # will return maxHeight = 116.3098

h = 0
h_desired = root_fun_4(r,v0,t,h)
plt.plot(t,h_desired)
plt.plit(tmax[0],maxHeight[0],'o')
plt.grid()
plt.show()

   
# Part 3 - What maximum height will be attained? - Option 2

import numpy as np
from scipy.optimize import fminbound,fsolve

v0 = 78
r = 0.35
G = 9.81

def root_fun_4(r,v0,t,desired_h):
    return ((1/r)*(v0 + g/r)*(1- np.exp(-r * t)) - (g*t)/r) - desired_h

h = 80
def root_fun(t):
    return (root_fun_4(r,v0,t,h))


def Object_Height(v0,r,t):
    if r == 0:
        print('Zero drag coefficient are not allowed')
    else:
        g = 9.81
        
    return ((1/r)*(v0 + g/r)*(1- np.exp(-r * t)) - (g*t)/r)    

def min_object_height(t):
    return -Object_Height(v0,r,t)

tmax = fminbound(min_object_height,2,5)
print(tmax)
hmax = Object_Height(v0,r,tmax)
print(tmax) # hmax = 116.3098

##

# Golden Section Search Algorithm

def gsection(ftn,x1,xm,xr,tol = 1e-9):
    # applies the golden-section algortihm to maximize ftn
    # we assume that ftn is a function of a single variable 
    # and that x.L < x.m < x.r and ftn(x.L), ftn(x.r) <= ftn(x.m)
    # the algorithm iteratively refines x.l, x.r and x.m and
    # terminates when x.r -x.l <= tol, then returns x.m
    # golden ratio plus one
    grl = 1 + (1+ np.sqrt(5))/2
    # Successively refine x.l, x.r and x.m
    fl = ftn(x1)
    fr = ftn(xr)
    fm = ftn(xm)
    while ((xr - xl) > tol):
        if (xr - xm) > (xm - xl):
            y = xm + (xr - xm)/grl
            fy = ftn(y)
            if (fy >= fm):
                xl = xm
                fl = fm
                xm = y
                fm = fy
            else:
                xr = y
                fr = fy
        else:
            y = xm = (xm - xl)/grl
            fy = ftn(y)
            if (fy >= fm):
                xr = xm
                fr = fm
                xm = y
                fm = fy
            else:
                xl = y
                fl = fy
    return (xm)