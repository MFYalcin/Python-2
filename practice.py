##
'''
set_1 = {1,2,3,4,5,2,3}
print(set_1)
#{1,2,3,4,5}
dict_1 = {1:2,3:4}
print(list(set(dict_1)))
#[1,3]
set_2 = {'a','b',3,4}
print(len(set_2))
#4

dict_2 = {'a':2,'b':3}
print(len(dict_2))
#2

set_1 = {1,2,3,4}
set_1.add('a')
print(set_1)
#{1,2,3,4,'a'}

l_1 = ['a','c',5,6]
l_1.append(({1:3,7:8},(1,2),'m'))
l_1.pop(2)
l_1.pop(2)
print(l_1)
#['a', 'c', ({1: 3, 7: 8}, (1, 2), 'm')]
##


a_list = [[0,1],[2,3],[4,5]]

for items in a_list:
    for item in items:
        print(item,end=',')
    
#0,1,2,3,4,5,

a_set = {1,2,3,'a'}

for i in a_set:
    print(i,end=',')
#1,2,3,a,


a_tuple = (1,2,3,[4,5])

b_list = [1,2,3,4]
c = a_tuple[2]
b_list[2] = 2*c
print(b_list)
#[1,2,6,4]


def symmetric_y(x,y)->tuple:
    return (-x,y)

ex1 = (1,2)
ex2 = (7,-3)

x1, y1 = symmetric_y(1,2)
x2 ,y2 = symmetric_y(7,-3)

print(ex1,'->',x1,y1)
print(ex2,'->',x2,y2)
# (1, 2) -> -1 2
#(7, -3) -> -7 -3


RED = 'R'
BLACK = 'B'

checkers = [[BLACK] * 8 for i in range(8)]

print(checkers)
#[['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
#['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], 
#['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], 
#['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], 
#['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], 
#['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], 
#['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], 
#['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]

for i in range(8):
    for j in range(8):
        if (i+j) % 2 != 0:
            checkers[i][j] = RED
    
for i in range(8):
    for j in range(8):
        print(checkers[i][j],end=' ')
        # B R B R B R B R R B R B R B R B B R B R B R B R R B R B R B R B B R B R B R B R R B R B R B R B B R B R B R B R R B R B R B R B 



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
        if (i+j) %2 != 0:
            board[i][j] = RED

board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)

def get_position(colour, rank):
    for i in range(8):
        for j in range(8):
            if board[i][j] == (colour, rank):
                return (i, j)
    return None

print(get_position(RED, QUEEN)) # (0,0)
print(get_position(BLACK, KNIGHT))# (7,7)

## OR OTHER WAY TO DO IT

RED = "R"
BLACK = "B"
KING = "K"
QUEEN = "Q"
BISHOP = "B"
ROOK = "R"
KNIGHT = "N"
PAWN = "P"
board = {(RED,QUEEN):(0,0), (BLACK,KNIGHT):(7,7)}

def get_position2(colour, rank):
    return board.get((colour,rank))


print(get_position2(RED, QUEEN)) # (0,0)
print(get_position2(BLACK, KNIGHT))# (7,7)


grades = {101230:{'Math':91.5,'Social Sciences':87,'Biology':82},101231:{'Math':72,'Social Sciences':88.6,'Biology':92.2},101232:{'Math':64.6,'Social Sciences':85,'Biology':80.3}}


print(grades.get(101230)) # {'Math': 91.5, 'Social Sciences': 87, 'Biology': 82}

print(grades[101232]) # {'Math': 64.6, 'Social Sciences': 85, 'Biology': 80.3}


for i in grades[101230]:
    print(i,end=' ')
    # Math Social Sciences Biology 

for i in grades.values():
    for j in i.values():
        print(j,end=' ') # 91.5 87 82 72 88.6 92.2 64.6 85 80.3 


print(grades[101230]['Math']) # 91.5

for i in grades.items():
    print(i) 
#(101230, {'Math': 91.5, 'Social Sciences': 87, 'Biology': 82})
#(101231, {'Math': 72, 'Social Sciences': 88.6, 'Biology': 92.2})
#(101232, {'Math': 64.6, 'Social Sciences': 85, 'Biology': 80.3})

print(grades.get(101232)['Biology']) # 80.3


grades.pop(101232)
print(grades) 
# {101230: {'Math': 91.5, 'Social Sciences': 87, 'Biology': 82}, 101231: {'Math': 72, 'Social Sciences': 88.6, 'Biology': 92.2}}

grades.update({101234:{'Math': 64.6, 'Social Sciences': 85, 'Biology': 80.3}})
print(grades)
# {101230: {'Math': 91.5, 'Social Sciences': 87, 'Biology': 82}, 101231: {'Math': 72, 'Social Sciences': 88.6, 'Biology': 92.2}, 101232: {'Math': 64.6, 'Social Sciences': 85, 'Biology': 80.3}, 101234: {'Math': 64.6, 'Social Sciences': 85, 'Biology': 80.3}}



text = 'Hello Universe, I am here'
print(text.split())
#['Hello', 'Universe,', 'I', 'am', 'here']


txt = 'Hello World, Helloas;;sd;1234'
print(txt.strip('as;;sd;1234'))
# Hello World, Hello

import string
txt2 = ['HELLOO',1232324, '!$%^&^%$','WORLD']
a = str(txt2)
print((a.strip(string.punctuation)).lower())
# helloo', 1232324, '!$%^&^%$', 'world


lst = [123,'Ford','McLaren','BMW','Aston Martin',456]

lst.pop(0)
lst.pop(4)
lst.sort()
print(lst)
#['Aston Martin', 'BMW', 'Ford', 'McLaren']


def fibonacci(n:int):
    a=1
    b=1
    for i in range(1,n):
        a,b = b, a+b
    return a
print(fibonacci(13)) #377
print(fibonacci(81)) #61305790721611591

n = 6
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
    
n = 5
for i in range(1,n+1):
    for j in range(1,i):
        print(j,end=' ')
    print()
print()



RED = "R"
BLACK = "B"
KING = "K"
QUEEN = "Q"
BISHOP = "B"
ROOK = "R"
KNIGHT = "N"
PAWN = "P"

board = [None] * 8
for i in range(8):
    board[i] = board
    
board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)

print('All', board)
# All [('R', 'Q'), [...], [...], [...], [...], [...], [...], ('B', 'N')]




RED = "R"
BLACK = "B"
KING = "K"
QUEEN = "Q"
BISHOP = "B"
ROOK = "R"
KNIGHT = "N"
PAWN = "P"

board = [[None] * 8 for i in range(8)]

board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)

print('All',board)

def get_piece(x,y):
    return board[x][y]
print('The piece at (6,5) is', get_piece(6,5))
# The piece at (6,5) is None

def get_number_pieces(colour):
    num = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] != None:
                c,r = board[x][y]
                if (c == colour):
                    num+=1
    return num

def get_winner():
    num_black = get_number_pieces(BLACK)
    num_red = get_number_pieces(RED)
    
    if num_black == num_red:
        return 'T'
    elif num_black < num_red:
        return RED
    else:
        return BLACK

print(get_winner())
# T

filename = 'practice.txt'
import string


def histogram_txt(filename:str) -> dict:
    infile = open(filename)
    hist = {}
    
    for line in infile:
        word_list = line.split()
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            
            if word != '':
                count = hist.get(word,0)
                hist[word] = count + 1
    return hist
        


def freq_word(hist: dict)->tuple:
    max_freq = -1
    for word in hist:
        if hist[word] > max_freq:
            max_freq = hist[word]
            most_freq = word
    return (most_freq,max_freq)


if __name__=='__main__':
    hist = histogram_txt(filename)
    print(hist)
    most_freq,freq = freq_word(hist)
    print("The most frequently occuring word is \"", most_freq,
  "\" which occurs", freq, "times")


#Unit Testing for Fibonacci
def fibonacci(n:int)->int:
    a = 1
    b = 1
    for i in range(1,n):
        a,b = b, a+b
    return a

#Test

from practice import fibonacci

def auto_test(desc:str,actual,expected)->None:
    
        
    if actual == expected:
        print('Test passed')
        return 1
        
    else:
        print('Test Failed')
        return 0
        
ex1 = auto_test('fibonacci(1)',fibonacci(1),1)
ex2 = auto_test('fibonacci(2)',fibonacci(2),3)
ex3 = auto_test('fibonacci(7)',fibonacci(7),13)
print(ex1)
print(ex2)
print(ex3)

    
# Exhaustive Search


def exh_s(n:float)->float:
    EPSILON = 0.01
    step = EPSILON ** 2
    guess = 0.0
    num_guesses = 0
    while abs(guess ** 2 - n) >= EPSILON and n>= guess:
        guess += step
        num_guesses += 1
        
    print('# of guesses =', num_guesses)
    if guess > n:
        return None
    else:
        return guess

if __name__=='__main__':
    n = 5
    root_n = exh_s(n)
    
    if root_n:
        print("the square root of",n, "by exhaustive enumeration is", root_n)
    else:
        print("Failed to find the square root of", n)
# 
# of guesses = 22339
# the square root of 5 by exhaustive enumeration is 2.2339000000002898

 
# Bisection

def bisection(n:float)->float:
    EPSILON = 0.01
    num_guesses = 0
    low = 0.0
    high = n
    guess = (low+high)/2
    while abs(guess**2-n)>= EPSILON:
        print('low',low,'high',high,'guess',guess)
        num_guesses +=1 
        if guess ** 2<n:
            low = guess
        else:
            high = guess
        guess = (low+high)/2
    print('# of guesses=',num_guesses)
    return guess

if __name__=='__main__':
    n = 6
    root_n = bisection(n)
    if root_n:
        print("the square root of",n, "by bisection enumeration is", root_n)
    else:
        print("Failed to find the square root of", n)

low 0.0 high 6 guess 3.0
low 0.0 high 3.0 guess 1.5
low 1.5 high 3.0 guess 2.25
low 2.25 high 3.0 guess 2.625
low 2.25 high 2.625 guess 2.4375
low 2.4375 high 2.625 guess 2.53125
low 2.4375 high 2.53125 guess 2.484375
low 2.4375 high 2.484375 guess 2.4609375
# of guesses= 8
the square root of 6 by bisection enumeration is 2.44921875


#Heron

# Example: estimate 25 (to within ε^2 = 0.5)
#1. Set g = 3
#2. Calculate, ε^2 = |25 − 3^2| = 16 > 0.5
#3. Set g = (3 + (25/3))/2) -> 5.67 (rounded)
#4. Calculate, ε^2 = |25 − 5.67^2| = 7.15 > 0.5
#5. Set g = (5.67 + (25/5.67))/2 = 5.04
#6. Calculate, , ε^2 = |25 − 5.04^2| = 0.4 ≤ 0.5
#5.04 * 5.04 = 25.4 is close enough to 25, so 5.04 is an
#adequate approximation of 25

def heron(n:float)->float:
    EPSILON = 0.00001
    guess = 1
    num_guesses = 0
    while abs(guess * guess-n) > EPSILON:
        guess = (guess + n / guess) / 2
        num_guesses += 1
    print('# of guesses', num_guesses)
    return guess

if __name__=='__main__':
    n = 9
    root_n = heron(n)
    if root_n:
        print("the square root of",n, "by heron enumeration is", root_n)

    else:
        print("Failed to find the square root of", n)

# of guesses 5
#the square root of 9 by heron enumeration is 3.000000001396984

# Advance Exhaustive Method for x^3 +x^2 +c (ROOT FINDING)

def exh_new(guess:float,max_guess:float)->float:
    EPSILON = 0.01
    step = EPSILON / 2
    func = guess ** 3 - guess ** 2 - 2
    while abs(func) >= EPSILON and guess <= max_guess:
        guess += step
        func = guess ** 3 - guess ** 2 - 2

    if guess > max_guess:
        return None
    else:
        return guess


print(exh_new(0,10)) # 1.6949999999999859


# Advance Bisection Method(ROOT FINDING)

import numpy
def bis_new(guess_l:float,guess_h:float)->float:
    EPSILON = 0.01
    guess = (guess_l + guess_h)/2
    func_g_l = guess_l**3 - guess_l**2 -2
    func_g_h =guess_h**3 - guess_h**2 -2
    func_g = guess ** 3 -guess**2 - 2
    while abs(func_g)>= EPSILON:
        print('low=',guess_l,'high=',guess_h,'guess=',guess)
        if numpy.sign(func_g) == numpy.sign(func_g_l):
            guess_l =guess
            func_g_l = func_g
        else:
            guess_h = guess
            func_g_h = func_g
        guess = (guess_l + guess_h)/2
        func_g = guess ** 3 - guess ** 2- 2
    return guess
print(bis_new(0,10))

low= 0 high= 10 guess= 5.0
low= 0 high= 5.0 guess= 2.5
low= 0 high= 2.5 guess= 1.25
low= 1.25 high= 2.5 guess= 1.875
low= 1.25 high= 1.875 guess= 1.5625
low= 1.5625 high= 1.875 guess= 1.71875
low= 1.5625 high= 1.71875 guess= 1.640625
low= 1.640625 high= 1.71875 guess= 1.6796875
low= 1.6796875 high= 1.71875 guess= 1.69921875
low= 1.6796875 high= 1.69921875 guess= 1.689453125
1.6943359375


#selection sort
def selection(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(min+1,len(a)):
            if a[min] > a[j]:
                min = j
        a[i],a[min] = a[min],a[i]
arr = [13,4,4,7,9,3]
print(arr)
selection(arr)
print(arr)
#[13, 4, 4, 7, 9, 3]
#[3, 4, 4, 7, 9, 13]


#Bubble sort

def bubble(a):
    n = len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

arr =[64, 34, 25, 12, 22, 11, 90]
print(arr)
bubble(arr) 
print(arr)

#[64, 34, 25, 12, 22, 11, 90]
#[11, 12, 22, 25, 34, 64, 90]


# Insertion Sort

def insertion(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j>= 0 and key< a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1] = key
arr =[64, 34, 25, 12, 22, 11, 90]
print(arr)
insertion(arr) 
print(arr)
#[64, 34, 25, 12, 22, 11, 90]
#[11, 12, 22, 25, 34, 64, 90]

# Merge sort

def merge(a):
    if len(a) > 1:
        mid = len(a)//2 # Finding the mid of the array
        L = a[:mid] # Dividing the array elements
        
        # into 2 halves
        R = a[mid:]
        merge(L) # Sorting the first half
        merge(R) # Sorting the second half
        
        i = j = k = 0
        
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
            
            
            # Checking if any element was left
            while i < len(L):
                a[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                a[k] = R[j]
                j += 1
                k += 1
                
                
# Driver code to test above 
arr =[64, 34, 25, 12, 22, 11, 90]
print(arr)
merge(arr) 
print(arr)                


list_of_op = ['*','+']

def adding(op1,op2)->int:
    return op1 + op2 
def multiplying(op1,op2)->int:
    return op1 * op2
def execute_command(command)->int:
    operator,op1,op2 = command
    
    if operator == '+':
        return adding(op1,op2)
    elif operator == '*':
        return multiplying(op1,op2)
    else:
        return None
    




# Numerical Algorithms Curve Fitting, Interpolation
    
    
x 5 4
y 2 1

import numpy as np

x = [5,4]
y = [2,1]
z = np.polyfit(x,y,1)
print(z) # [1,-3] -> x - 3


x 0 5 4
y 1 4 3

x = [0,5,4]
y = [1,4,3]
z = np.polyfit(x,y,2)
print(z) # [0.1,0.1,1] 0.1x**2 + 0.1x + 1

# Regression, Curve Fitting

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,9,9)
y = [1,4,5,6,7,8,9,12,15]
plt.scatter(x,y)
plt.show()

#x 0 2 3 5 6
#y 2 3 4 5 9 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,6,5)
y = [2,3,4,5,9]
deg = 1
coef = np.polyfit(x,y,deg)
print(coef)
plt.scatter(x,y)
plt.show()

'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,6,5)
y = [2,3,4,5,9]
deg = 2 #1,2,3 # More degree, more curved
coef = np.polyfit(x,y,deg)
x_e = np.linspace(0,6,100)
y_e = np.polyval(coef,x_e)

plt.plot(x,y,'o',x_e,y_e,'-')
plt.show()


# One Dimensional Optimization

import numpy as np
import matplotlib.pyplot as plt

v0 = 50
r = 0.35

def Object_h(v0,r,t):
    if r==0:
        print('Wrong Format')
    else:
        g= 9.81
    
    return ((1/r) * (v0 + g/r) * (1 - np.exp(-r*t)) - (g*t) / r)

t = np.linspace(0,12,100)
h = Object_h(v0,r,t)

plt.plot(t,h)
plt.grid()
plt.show()


#Another Way Without Vectors
#LOOP
import numpy as np
import matplotlib.pyplot as plt

v0 = 50
r = 0.35

def Object_h(v0,r,t):
    if r==0:
        print('Wrong Format')
    else:
        g= 9.81
    
    return ((1/r) * (v0 + g/r) * (1 - np.exp(-r*t)) - (g*t) / r)

t = np.linspace(0,12,100)
h = np.ones(len(t))
for k in range(1,len(t)):
    h[k] = Object_h(v0,r,t[k])
    
plt.plot(t,h)
plt.grid()
plt.show()



# Example 1 Step 2 80m above?

#Time Interval [1.4520,7.0315]

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

v0 = 78
r = 0.35
g = 9.81
def root_fun_4(v0,r,t,desired_h):
    return ((1/r) * (v0 + g/r) * (1 - np.exp(-r*t)) - (g*t) / r) - desired_h

h = 80
def root_fun(t):
    return root_fun_4(v0,r,t,h)

x1 = [0.1, 2]
time1 = fsolve(root_fun, x1)
print(time1) #1.4520

x2 = [6,8]
time2 = fsolve(root_fun, x2)
print(time2) # 7.0315

t = np.linspace(0,12,100)
h_desired = root_fun_4(v0,r,t,h)
plt.plot([time1[0],time2[0]],[0,0],'o')
plt.plot(t,h_desired)
plt.grid()
plt.show()

#[1.45199565 1.45199565]
#[7.03154379 7.03154379]


# When will the object hit the ground?


import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

h=0
v0 = 78
r = 0.35
g = 9.81
def root_fun_4(v0,r,t,desired_h):
    return ((1/r) * (v0 + g/r) * (1 - np.exp(-r*t)) - (g*t) / r) - desired_h


def root_fun(t):
    return root_fun_4(v0,r,t,h)


x3 = [10,12]
time3 = fsolve(root_fun,x3)
print(time3)

t = np.linspace(0,12,100)

h=0
h_desired = root_fun_4(v0,r,t,h)

plt.plot(time3[0],0,'o')
plt.plot(t,h_desired)
plt.grid()
plt.show()
# [10.5378357 10.5378357]



# What max height will be attained?
g = 9.81
r = 0.35
v0 = 78
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def Object_h(v0,r,t):
    if r==0:
        print('Wrong Format')
    else:
        g= 9.81
    
    return ((1/r) * (v0 + g/r) * (1 - np.exp(-r*t)) - (g*t) / r)

def root_fun_4(v0,r,t,desired_h):
    return ((1/r) * (v0 + g/r) * (1 - np.exp(-r*t)) - (g*t) / r) - desired_h



def func(t):
    g = 9.81
    return (1/r) * (v0 + g/r) * (r * np.exp(-r*t)) - (g / r) #dh/dt

tmax = fsolve(func,([3,5])) #tmax = 3.8014 s
t = np.linspace(0,12,100)
maxHeight = Object_h(v0,r,tmax) # 116.3098 m
h=0
h_desired = root_fun_4(v0,r,t,h)
plt.plot(t,h_desired)
plt.plot(tmax[0],maxHeight[0],'o')
plt.grid()
plt.show()


#Option 2
import numpy as np
from scipy.optimize import fminbound, fsolve
import matplotlib.pyplot as plt

v0 = 78
r = 0.35

def Object_h(v0,r,t):
    if r==0:
        print('Wrong Format')
    else:
        g= 9.81
    
    return ((1/r) * (v0 + g/r) * (1 - np.exp(-r*t)) - (g*t) / r)

def root_fun_4(v0,r,t,desired_h):
    return ((1/r) * (v0 + g/r) * (1 - np.exp(-r*t)) - (g*t) / r) - desired_h

def min_h(t):
    return -Object_h(v0,r,t)

tmax = fminbound(min_h,2,5)
print(tmax) # 3.80
hmax = Object_h(v0,r,tmax)
print(hmax) # 116.3098



import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

a = -3
v0 = 20

def Object_h(v0,a,t):
    return v0*t + 0.5*a*t


t = np.linspace(0,20,20)
h = v0*t + 0.5*a*t
h = Object_h(v0,a,t)
print(h)
plt.plot(t,'-',h,'*')
plt.grid()
plt.show()


#Similar Exam Questions Solving

# Previous Exam Question

def sort_student_FirstName(filename:str)->None:
    infile = open(filename)
    count = 0
    student_dict = {}
    for items in infile:
        student_info = items.strip().split(',')
        if count == 0:
            header = student_info
        else:
            if not(int(student_info[0])) in student_dict:
                student_dict[int(student_info[0])] = {}
            for i in range(1,4):
                if i != 3:
                    student_dict[int(student_info[0])][header[i]] = student_info[i]
                else:
                    student_dict[int(student_info[0])][header[i]] = float(student_info[i])
        count+=1
    infile.close()
    return student_dict
        
if __name__=='__main__':
    from import_practice import print_dictionary
    file = 'StudentEx2.csv'
    student_dict = sort_student_FirstName(file)
    print_dictionary(student_dict)
    print()



for items in student_dict.values():
    items = str(items['First Name'])
    items = items.split() 
    print(items,end=' ')


    
    
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(2,12,6)
y = [0.90,3.00,-4.50,-3.00,4.00,2.20]

deg = 10
coef = np.polyfit(x,y,deg)
print(coef)


plt.scatter(x,y)
plt.grid()
plt.show()

'''


































































































































































'''
video_games = {101: 'str',
               102: ("Sonic the Hedgehog", 1991),
               103: ("Super Mario 2", 1993),
               104: ("Super Mario 64", 1996),
               105: ("Final Fantasy VII", 1996)}

# get a key's value
name = video_games[101]
year = video_games.get(101)

print(year)
values = video_games.values()
for value in values:
    print (value)

filename = {'Fiction':[{'title':'abc','author':'d'}],'Comics':[{'title':'efg','author':'z'}]}

for value in filename.values():
    for i in value:
        print(i.get('title'))
    
'''