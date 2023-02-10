#Quizzes
##

#x = {1,2,3}
#print(x(0))
#builtins.TypeError: 'set' object is not callable
#x = {1,2,3}
#print(x[0])
#builtins.TypeError: 'set' object is not subscriptable
#print(x{0})
#Syntax Error: invalid syntax. Perhaps you forgot a comma?: <string

##

import math
print(type(math))
#<class 'module'>

##

def printName(): print(__name__)

#What is printed by the following script:

from modA import printName
from modB import printName
from modC import printName
printName()
#modC

##

#Assume there is a module in a file named f_mod.py that defines a function f(). You import it as follows:
#from f_mod import f

#How do you call the function f() from the main script? 

#f.f_mod()

##

#x = (1,2,3)
#print(x[0])
#1
#print(x(0))
#builtins.TypeError: 'tuple' object is not callable
#print(x{0})
# Syntax error: invalid syntax

##

x= {1,2,3,1,2,3}
print(len(x))
#3
x= {1,2,3,1,2,3}
print(len(x))
#6
x= [1,2,3,1,2,3]
print(len(x))
#6

##
x = (1,2,3)
a = 4
x[0] = a
a = x[2]
print(x)
print(a)
x[0] = a
#builtins.TypeError: 'tuple' object does not support item assignment

##

speeds = {'turtle':0.5, 'rabbit':8, 'cheetah':25}
speeds['self-isolation'] = 0
print(speeds.get('far-too-fast-far-too-furious'))
if speeds['unladend-African-swallow'] == None:
       print('Ni!')
#builtins.KeyError: 'unladend-African-swallow'

##

['good', 'morning', 'sunshine']

#Here is the start of our program:

import string
str = "Good morning Sunshine!"

print(str.strip(string.punctuation).lower().split())
#['good', 'morning', 'sunshine']

##

#Consider the following dictionary.
dict = {'only-entry':'yes'}

#If we want to remove the only entry, we can: (choose one)

#dict.clear()
#dict.pop('only-entry')
#del dict['only-entry'] #(Same solution)
print(dict)

##

'''
sum = 0
lst = [2,4,6]
for item in lst:
    for inner in range(item):
        sum += 1
print(sum)
#12
##

sum = 0
lst = [2,4,6]
for item in lst:
    for inner in range(3):
        sum += 1
print(sum)
#9

##

sum = 0
lst = [2,4,6]
for item in lst:
    for inner in range(lst):
        sum += 1
'''
print(sum)
#builtins.TypeError: 'list' object cannot be interpreted as an integer

##






#Sets

str = "Hello"
c = str[0]

for t in str:
    print(t,end=",")

a_list = [0,1,0]
a = a_list[0]
for i in a_list:
    print(i,end=",")

a_list[1] = 5
#str[1] = 'd' (error)
str = str[:1] + 'd' + str[2:]
for s in str:
    print(s,end=",")
    
Executed = H,e,l,l,o,0,1,0,H,d,l,l,o,

##

a_list = [0,1,0]
size_list = len(a_list)
a = a_list[0]
a_list.append(2)
a_list.append(2)
print(a_list)

Executed = [0, 1, 0, 2, 2]

##

a_set = {0,1,0}
#a = a_set[0] (Set object does not support indexing)
size_set = len(a_set)
a_set.add(2)
a_set.add(2)
print(a_set)

Executed = {0,1,2}

##

for i in a_list:
    print(i,end=",")
print()
for i in a_set:
    print(i,end=",")

Executed 
0,1,0,2,2,
0,1,2,
    
##

a_list = [0,1,0]
b_list = [0,0,1]
a_set = {0,1,0}
b_set = {1,0}

if (a_list == a_set) or (a_set == b_set):
    print("if")
elif (a_list == b_list) or (b_list == b_set):
    print("elif")
else:
    print("else")

Executed = "if"

# Tuples
# Tuples are immutable


s = set()
t = ()
s = {1}
t = (1,)


a_list = [0,1,0]

a_tuple = (0,1,0)

c = a_tuple[1]
a_list[0] = c*2 
Executed [2,1,0]
a_tuple[0] = c*2 #Error(not mutable)

# Aggregate data together

# Packing = time = (9,15,45)
hours = time[0]
mins = time[1]
secs = time[2]
# instead do this
# Unpacking = (hours,mins,secs) = time
(9,15,45)

##

def symmetric_about_x (x,y):
    return x,-y

eg1 = symmetric_about_x (3,5)
eg2 = symmetric_about_x (-3,5)
eg3 = symmetric_about_x (3,-5)
eg4 = symmetric_about_x (0,0)

x1, y1 = symmetric_about_x (3,5)
x2, y2 = symmetric_about_x (-3,5)
x3, y3 = symmetric_about_x (3,-5)
x4, y4 = symmetric_about_x (0,0)

print(eg1, x1, y1)
print(eg2, x2, y2)
print(eg3, x3, y3)
print(eg4, x4, y4)
Executed
(3,-5) 3 -5
(-3,-5) -3 -5
(3,5) 3 5
(0,0) 0 0

##




import math

def quad_roots(a:int, b:int, c:int) -> tuple:
    
    """
 Returns the two roots of the quadratic:
 ax^2 +bx +c
>>> quad_root(0,1,2)
(-math.inf,math.inf)
>>> quad_root(2,1,2)
(None,None)
>>> quad_root(2,4,2)
(-1.0,-1.0)
>>> quad_roots(1,-6,8)
(4.0,2.0)

    """
    if a==a:
        return (-math.inf,math.inf)
    disc = b**2 - 4*a*c
    if disc<0:
        return (None,None)
    sqrtdisc = math.sqrt(disc)
    twoa = 2*a
    return ((-b+sqrtdisc)/twoa,(-b-sqrtdisc)/twoa)


x = quad_root(0,1,2)
y = quad_root(2,1,2)
z = quad_root(2,4,2)
w = quad_roots(1,-6,8)





xr1,xr2 = quad_root(0,1,2)
yr1,yr2 = quad_root(2,1,2)
zr1,zr2 = quad_root(2,4,2)
wr1,wr2 = quad_roots(1,-6,8)

print(x,xr1,xr2)
print(y,yr1,yr2)
print(z,zr1,zr2)
print(w,wr1,wr2)

Executed
(-inf, inf) -inf inf
(None, None) None None
(-1.0, -1.0) -1.0 -1.0
(4.0, 2.0) 4.0 2.0

#

def symmetric_about_x( t:tuple )->tuple:
    """
    Returns the point symmetric around the x-axis with tuple
>>> symmetric_about_x ((3,5))
(3,-5)
>>> symmetric_about_x ((-3,5))
(-3,-5)
>>> symmetric_about_x ((3,-5))
(3,5)
>>> symmetric_about_x ((0,0))
(0,0)
    """
    
    (x,y) = t
    return x,-y
# or could be (return(t[0],-t[1])
eg1 = symmetric_about_x ((3,5))
eg2 = symmetric_about_x ((-3,5))
eg3 = symmetric_about_x ((3,-5))
eg4 = symmetric_about_x ((0,0))

x1, y1 = symmetric_about_x ((3,5))
x2, y2 = symmetric_about_x ((-3,5))
x3, y3 = symmetric_about_x ((3,-5))
x4, y4 = symmetric_about_x ((0,0))

print(eg1, x1, y1)
print(eg2, x2, y2)
print(eg3, x3, y3)
print(eg4, x4, y4)



#

import math

def quad_roots(a:int, b:int, c:int) -> set:
    
    """
 Returns the set roots of the quadratic:
 ax^2 +bx +c
>>> quad_roots(0,1,2)
{-math.inf,math.inf}
>>> quad_roots(2,1,2)
{None}
>>> quad_roots(2,4,2)
{-1.0}
>>> quad_roots(1,-6,8)
{4.0,2.0}

    """
    if a==0:
        return {-math.inf,math.inf}
    disc = b**2 - 4*a*c
    if disc<0:
        return {None,None}
    sqrtdisc = math.sqrt(disc)
    twoa = 2*a
    return {(-b+sqrtdisc)/twoa,(-b-sqrtdisc)/twoa}


x = quad_roots(0,1,2)
y = quad_roots(2,1,2)
z = quad_roots(2,4,2)
w = quad_roots(1,-6,8)


print(x)
print(y)
print(z)
print(w)

Executed
{-inf, inf}
{None}
{-1.0}
{2.0, 4.0}

#

import volumes
x = volumes.volume_of_sphere(1)

from volumes import volume_of_sphere
x = volume_of_sphere(1)



















#Tuple Worksheet

studentinfo = [(10,55.0),(23,66,7),(14,87.0)]

studentinfo += [(99,57.0)]

count = 0
for tuple in studentinfo:
    student,grade = tuple
    if grade >50:
        count += 1

inclass = False
for tuple in studentinfo:
    student,grade = tuple
    if student == 38:
        inclass = True

inclass = False
for i in range(len(studentinfo)):
    student,grade = studentinfo[i]
    if student == 14:
        inclass = True
        
inclass = False
i = 0
while i < len(studentinfo):
    student,grade = studentinfo[i]
    if student == 99:
        inclass = True
    i += 1


#Tuples Checker Board example

RED = 'R'
BLACK = 'B'

checkers = [ [BLACK]*8 for i in range(8)]


for i in range(8):
    for j in range(8):
        if (i+j)%2 != 0:
            checkers[i][j] = RED
            
            
for i in range(8):
    for j in range(8):
        print(checkers[i][j],end='')
    print()
print()
Executed 
BRBRBRBR
RBRBRBRB
BRBRBRBR
RBRBRBRB
BRBRBRBR
RBRBRBRB
BRBRBRBR
RBRBRBRB


        
#

ecor1051 = [('A','Bailey'),('B','Schram'),('C','Bailey'),('G','Bailey')]

for tuple in ecor1051:
    section,instructor = tuple
    print(section,end= ' ')
print()

section,instructor = ecor1051[-1]
ecor1051[-1] = (section,"Marshall")
print()

i=0
while i < len(ecor1051):
    section,instructor = ecor1051[i]
    print(section,instructor)
    i+=1
    
Executed
A Bailey
B Schram
C Bailey
G Marshall

# Nested Loops

n = 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
    
Executed
1
12
123
1234

#
#board = [None]*8
#board = [[None]*8]*8
#board = [[None]*8 for i in range(8)]

RED = 'R'
BLACK = 'B'
KING = 'K'
QUEEN = 'Q'
BISHOP = 'B'
ROOK = 'R'
KNIGHT = 'K'
PAWN = 'P'

# Wrong Way
board = [[None]*8]*8
print("All",board)

board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)
print("All 2", board)

#Executed = All [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
#All 2 [[('R', 'Q'), None, None, None, None, None, None, ('B', 'K')], [('R', 'Q'), None, None, None, None, None, None, ('B', 'K')], [('R', 'Q'), None, None, None, None, None, None, ('B', 'K')], [('R', 'Q'), None, None, None, None, None, None, ('B', 'K')], [('R', 'Q'), None, None, None, None, None, None, ('B', 'K')], [('R', 'Q'), None, None, None, None, None, None, ('B', 'K')], [('R', 'Q'), None, None, None, None, None, None, ('B', 'K')], [('R', 'Q'), None, None, None, None, None, None, ('B', 'K')]]

# Right Way 1 Using Loop

board = [None]*8
for i in range(8):
    board[i] = [None]*8
    
board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)
print("All 3", board)

#Executed = All 3 [[('R', 'Q'), None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, ('B', 'K')]]

# Right Way 2 Using Generator

board = [[None]*8 for i in range(8)]

board[0][0] = (RED, QUEEN)
board[7][7] = (BLACK, KNIGHT)
print("All 4", board)

#Executed = All 4 [[('R', 'Q'), None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, ('B', 'K')]]

def get_piece(x,y):
    return board[x][y]

print("The piece at (7,7) is ", get_piece(7,7))

#Executed = The piece at (7,7) is ('B', 'N')
def get_number_pieces(colour):
    num = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] != None:
                c,r = board[x][y]
                if(c==colour):
                    num+=1
    return num



def get_winner():
    num_black = get_number_pieces(BLACK)
    num_red = get_number_pieces(RED)
    if num_black == num_red:
        return "T"
    elif num_black > num_red:
        return BLACK
    else:
        return RED

print(get_winner())
Executed = 'T'


# Text Processing and Incremental Development. A case study


import string
from typing import List

def build_word_list(filename:str) -> List[str]:
    """Return a list of all the distinct words in the specified file,
    sorted in ascending order.
    
    >>> word_list = build_word_list('sons_of_martha.txt')
    >>> word_list
    >>> len(word_list)  # How many different words are in the file?
    """    
    
    infile = open(filename, 'r')
    
    word_set = set()
    for line in infile:
       #print(line,end='')
        word_list = line.split()
       #print(word_list)
        for word in word_list:
            word = word.strip(string.punctuation)
            word = word.lower()
           #print(word)
            if word != '':
                word_set.add(word)
               #print(word_set)
        
    infile.close()    
    # Convert to list and sort
    word_list = list(word_set)
    word_list.sort()
    
    return word_list
    
    
    
    
    
    
    
    
    


testname = 'sample.txt'
test_list = build_word_list(testname)
print('File', testname, 'contains', len(test_list), 'distinct words')
print('The words are: ', test_list)



filename = 'whyEnglishIsSoHard.txt'
word_list = build_word_list(filename)
print('File', filename, 'contains', len(word_list), 'distinct words')
print('The words are: ', word_list)




testname3 = 'sons_of_martha.txt'
test_list3 = build_word_list(testname3)
print('File', testname3, 'contains', len(test_list3), 'distinct words')
print('The words are: ', test_list3)


Executed

#File sample.txt contains 3 distinct words
#The words are:  ['goodbye', 'hello', 'hi']
#File whyEnglishIsSoHard.txt contains 99 distinct words
#The words are:  ['a', 'also', 'always', 'and', 'anonymous', 'are', 'be', 'becomes', 'beet', 'beeth', 'begin', 'boot', 'booth', 'box', 'boxes', 'brethren', 'brother', 'but', 'called', 'cat', 'cats', 'cose', 'english', 'feet', 'feminine', 'find', 'foot', 'fowl', 'full', 'geese', 'give', 'goose', 'hard', 'hat', 'he', 'hice', 'him', 'his', 'hose', 'house', 'houses', 'i', 'if', 'imagine', 'in', 'is', 'lone', 'man', 'masculine', 'may', 'meese', 'men', 'methre', 'mice', 'moose', 'mother', 'mouse', 'my', 'nest', 'never', 'not', 'of', 'one', 'or', 'ox', 'oxen', 'oxes', 'pair', 'pan', 'pen', 'plural', 'pronouns', 'say', 'set', 'she', 'shim', 'shis', 'should', "shouldn't", 'show', 'so', 'speak', 'teeth', 'that', 'the', 'then', 'those', 'though', 'three', 'tooth', 'two', 'we', "we'll", 'whole', 'why', 'with', 'would', 'yet', 'you']
#File sons_of_martha.txt contains 249 distinct words
#The words are:  ['a', 'afar', 'afraid', 'again', 'against', 'ages', 'all', 'allows', 'already', 'altars', 'and', 'angels', 'any', 'are', 'as', 'at', 'bare', 'be', 'because', 'bed', 'before', 'behind', 'belief', 'birth', 'black', 'blessed', 'blood', 'bother', "brethren's", 'buffet', 'burden', 'but', 'by', 'care', 'careful', 'cast', 'choose', 'city', 'clear', 'cleave', 'common', 'concerned', 'confessed', 'creed', 'cup', 'cushion', 'damn-well', 'dark', 'dawn', 'days', 'death', 'deep', 'deliver', 'desert', 'do', 'drouth', 'dry', 'duly', 'early', 'earth', 'earthline', 'embark', 'end', 'engages', 'entrain', 'ere', 'evenfall', 'fair', 'favour', 'feed', 'feet', 'finger', 'fires', 'flat', 'floods', 'follow', 'for', 'forbidden', 'forth', 'fountains', 'from', 'gates', 'gather', 'gear', 'given', 'gloves', 'goad', 'god', 'good', 'grace', 'guest', 'hale', 'haltered', 'have', 'he', 'hear', 'heart', 'heaven', 'her', 'hidden', 'high', 'hill-tops', 'him', 'his', 'how', 'hungry', 'in', 'inherited', 'into', 'is', 'it', 'kind', 'know', 'ladder', 'laid', 'land', 'lays', 'leave', 'lesser', 'lighted', 'like', 'little', 'living', 'lo', 'lock', 'long', 'loose', 'lord', 'lost', 'main', 'make', 'martha', "martha's", 'mary', "mary's", 'matter', 'may', 'men', 'mercies', 'more', 'mother', 'mountains', 'mouth', 'multiplied', 'must', 'need', 'not', 'nuts', 'of', 'on', 'once', 'or', 'overcome', 'own', 'part', 'path', 'piece', 'pity', 'pleasantly', 'pour', 'preach', 'promise', 'raise', 'rears', 'relief', 'removed', 'repiece', 'reprieve', 'reproved', 'rest', 'restore', 'rocks', 'rods', 'rouse', 'rude', 'run', 'runs', 'say', 'secret', 'see', 'seldom', 'service', 'shake', 'she', 'shock', 'side', 'simple', 'simply', 'sit', 'sleeping', 'smile', 'so', 'some', 'son', 'sons', 'soul', 'spilled', 'stall', 'stand', 'steer', 'stone', 'stumble', 'summit', 'switches', 'take', 'tally', 'teach', 'temper', 'tend', 'terrible', 'that', 'the', 'their', 'them', 'then', 'these', 'they', 'thronged', 'till', 'to', 'transport', 'troubled', 'truly', 'turn', 'unaware', 'under', 'up', 'upon', 'wait', 'wary', 'was', 'watchful', 'waters', 'ways', 'wheels', 'when', 'where', 'which', 'will', 'wires', 'with', 'withdrawn', 'without', 'witness', 'wood', 'word', 'work', 'world', 'ye']


#Dictionary 5 Practice

grades = {10:55.0, 23:66.7, 14:87}
grades[99] = 55.0
grades.update({9:55})
print(grades)

Executed 
{10: 55.0, 23: 66.7, 14: 87, 99: 55.0, 9:55.0}

present38 = grades.get(38) # None
present38b = 38 in grades.keys() #False

stud10 = grades.get(10)# 55.0
stud10b = grades[10]# 55.0

stud38 = grades.get(38) #None
stud38b = gradesp[38] # KeyError

gradevals = grades.values()
gradelist = list(gradevals)
is50 = 50 in gradelist #False
is50b = 50 in gradevals #False

num55s = gradelist.count(55.0) #3
num55sb = gradevals.count(55.0) #AttributeError due to dict not having count function

from math import fabs
num55bs = 0
for grade in gradelist:
    if fabs(grade - 55.0) <0.001:
        num55bs += 1 #3
        

num50s = 0
for grade in gradelist:
    if grade >= 50:
        num50s += 1

i=0
while i<len(gradelist):
    if fabs(gradelist[i] - 55.0) <0.001:
        num50s += 1
    i += 1
print(num50s) #5


over50 = False
i=0
while i<len(gradelist) and not over50:
    if gradelist[i]>50:
        over50 = True
    i+=1

over50b = False
for grade in gradelist:
    if grade>50:
        over50b = True



items = grades.items()
studentOver50 = []
for item in items:
    st,gr = item
    if gr>50.0:
        studentOver50.append(st) #[10,23,14,99,9]
        


grades_before = grades.values() 
del grades[23]
grades.pop(23,None) #It will return None instead of 23
grades.pop(23) #deletes the key and its value
grades_after = grades.values()


studentsort = sorted(grades) # [9,10,14,23,99]
sortedstval = sorted(grades.items())# [(9:55.0),(10:55.0),(14:87),(23:66.7),(99:55.0)]







# Unit testing

#Manual Testing
#fib_lib.py
def fibonacci(n:int) ->int:
    """
    Returns the Fibonacci number F_n for positive values of n, where F_1 = 1, F_2 = 1 and F_n = F_n-1 + F_n-2, n>2.
    >>> fibonacci(1)
    1#expected
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(7)
    13
    """
    a = 1
    b = 1
    for i in range(1, n):
        a, b = b, a + b
    return a

print(fibonacci(1)) #actual
print(fibonacci(1))
print(fibonacci(3))
print(fibonacci(7))


#
#unit_testing.py
def check_equal(expected, actual):
    if(expected == actual):
        print('Passed')
    else:
        print('Failed')
        
        

#test_fib.py
from fib_lib import fib
from unit_testing import check_equal

def test_fibonacci() -> None:

    check_equal('fibonacci(1)', fibonacci(1), 1)
    check_equal('fibonacci(1)', fibonacci(2), 1)
    check_equal('fibonacci(1)', fibonacci(3), 2)
    check_equal('fibonacci(1)', fibonacci(1), 13)
    
test_fibonacci()

Executed
fibonacci(1) PASSED
------
fibonacci(1) PASSED
------
fibonacci(1) PASSED
------
fibonacci(1) FAILED: expected 13, got 1
------






#Main Script
#test_fib()












# Student Quiz Grade Average Example
#Version 1 (Poor)

ecor1051 = [['100123456',8,9,0,5,None],['101987654',3,8,8,7,None]]

for st in range(len(ecor1051)):
    total = 0
    for quiz in range(1,5):
        total += ecor1051[st][quiz]
    print(total)
    ecor1051[st][5] = total / 4
print(ecor1051)

# Version 2 - With sub-lists

ecor1051 = [['100123456',[8,9,0,5],None],['101987654',[3,8,8,7],None]]
    
for stNum in range(len(ecor1051)):
    total = 0
    student = ecor1051[stNum]
    quizzes = student[1]
    for quiz in range(len(quizzes)):
        total += quizzes[quiz]
        student[2] = total / len(quizzes)
        
print(ecor1051)
Executed = [['100123456', [8, 9, 0, 5], 5.5], ['101987654', [3, 8, 8, 7], 6.5]]

# Version 3 - With tuples, but with a hidden danger, tuples are immutable

ecor1051 = [['100123456',[8,9,0,5],None],['101987654',[3,8,8,7],None]]

for stNum in range(len(ecor1051)):
    total = 0
    student = ecor1051[stNum]
    num,quizzes,average = student
    for quiz in range(len(quizzes)):
        total += quizzes[quiz]
    average = total / len(quizzes)
    ecor1051[stNum] = (num, quizzes, average)
    # Without this line, the average is not updated in the
print(ecor1051)
Executed = [('100123456', [8, 9, 0, 5], 5.5), ('101987654', [3, 8, 8, 7], 6.5)]

# Dictionaries

a_str = 'Hello'
print(a_str, a_str[0])

a_list = [3,5,a_str]
item = a_list[1]
for item in a_list:
    print(item)
    
a_set = {2,4,4}
for item in a_set:
    print(item)
    
a_tuple = (4,5)
print(a_tuple)


a_dict = {1:55, 2:66, 3:44} #(key:value)
item1 = a_dict[3] # 3 is key
item2 = a_dict.get(3) # same here, if there is no key value in it, 'None' will be got


#

RED = 'R'
BLACK = 'B'
KING = 'K'
QUEEN = 'Q'
BISHOP = 'B'
ROOK = 'R'
KNIGHT = 'K'
PAWN = 'P'

board = {(RED, QUEEN):(0,0), (BLACK, KNIGHT): (7,7)}

def get_position(colour, rank):
    return board.get( (colour, rank) )

print(get_position(RED, QUEEN))
print(get_position(BLACK, KNIGHT))
Executed 
(0, 0)
(7, 7)

#
d = {111: "Tom", 222:"Dick", 333:"Harry"}
name = d[111]
name = d.get[111]

keys = d.keys()
for key in keys:
    print(key)
Executed 
111
222
333

values = d.values()
for value in values:
    print(value)
Executed
Tom
Dick
Harry

items = d.items()
for item in items:
    print(item)
Executed# We get tuples
(111, 'Tom')
(222, 'Dick')
(333, 'Harry')

d.update( {111:'Thomas',444:'Susan'} )
Executed
(111, 'Thomas')
(222, 'Dick')
(333, 'Harry')
(444, 'Susan')



# Root finding

import math


'''
# Exhaustive Enumartion   

def exhaustive(x: float) -> float:
 """
 Return the square root of x, calculated using an algorithmic technique known as exhaustive enumaration
 """
    EPSILON = 0.01
    step = EPSILON ** 2
    guess = 0.0
    num_guesses = 0
    while abs(guess ** 2 -x) >= EPSILON and guess <= x:
        guess += step
        num_guesses += 1
        
    print('# of guesses = ', num_guesses) # Debug Statement
    
    if guess > x:
        # print('Failed on square root of', x)
        return None
    else:
        # print(guess, 'is close to square root of', x)
        return guess


    #Main Script
if __name__ == '__main__':
    x = 3
    root_x = exhaustive(x)
    
    if (root_x):
        print('The square root of', x, 'by exhaustive numeration is',root_x)
    else:
        print('Failed to find the square root of', x)



Executed:
# of guesses =  17292
The square root of 3 by exhaustive numeration is 1.729199999999826

'''


# Bisection Search



def bisection(x: float) -> float:
    '''
    Return the square root of x, calculated using an algorithmic technique known as bisection search
    '''
       
       
    EPSILON = 0.01
    num_guesses = 0
    low = 0.0    #Window = [low,high]
    high = x
    guess = (low + high) / 2 
    while abs(guess ** 2 - x) >= EPSILON:
        print('low =', low, 'high =', high, 'guess =', guess)
        num_guesses += 1
        
        if(guess ** 2 < x):
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    print('# of guesses:', num_guesses)   
    return guess
   
   #Main Script
   
if __name__ == '__main__':
    x = 3
    root_x = bisection(x)
       
    if (root_x):
        print('The square root of', x, 'by bisection method is', root_x)
    else:
        print('Failed to find the square root of', x)
      

Executed:
       low = 0.0 high = 3 guess = 1.5
       low = 1.5 high = 3 guess = 2.25
       low = 1.5 high = 2.25 guess = 1.875
       low = 1.5 high = 1.875 guess = 1.6875
       low = 1.6875 high = 1.875 guess = 1.78125
       # of guesses: 5
       The square root of 3 by bisection method is 1.734375

##
  
# Heron Search

def heron(x: float) -> float:
    '''
    This is an example of a guess-and-check algorithm: it is easy to check whether or not a guess is a good one/
    __author__ = 'Cheryl Schramm'
    '''
    EPSILON = 0.00001
    guess = 1
    while abs(guess * guess -x) > EPSILON:
        guess = (guess + x / guess) / 2
        print('new guess:', guess) #Debug statement
    return guess


    
    
    
    
   
    
#Main Script
    
if __name__ == '__main__':
    x = 3
    root_x = heron(x)
       
    if (root_x):
        print('The square root of', x, 'by Heron search is', root_x)
    else:
        print('Failed to find the square root of', x)
      

 Executed:      
       




       new guess: 2.0
       new guess: 1.75
       new guess: 1.7321428571428572
       new guess: 1.7320508100147274
       The square root of 3 by Heron search is 1.7320508100147274

##
       
# More Practices on Exhaustive and Bisection Search


Equation: f(x) = x^3 - x^ 2; f(x) = 0
Epsilon = 0.05; Initial Guess: 0; Step Size: 0.1; Stop Condition: Maximum Guess = 10

f(0) = 0 - 0 - 2 = -2 -> abs(-2) > 0.05
...
f(0.1) = 0.1^3 - 0.1^2 - 2 = -2.009 -> abs(-2.009) > 0.05
f(1.6) = 1.6^3 - 1.6^2 - 2 = -0.464 -> abs(-0.464) > 0.05
f(1.7) = 1.7^3 - 1.7^2 - 2 = 0.023 -> abs(0.023) < 0.05 +++


##

def exhaustive_x3_x2_2(guess:float, max_guess:float) -> float:
    '''
     Return the square root of x, calculated using an algorithmic technique known as exhaustive enumaration
     >>> exhaustive_x3_x2_2(0,10)
     1.6949999999999859
    '''
    EPSILON = 0.01
    step = EPSILON / 2
    max_guess = 10       # Instead of max_guess we could have used max_steps
    func_sol = guess ** 3 - guess ** 2 - 2
    while abs(func_sol) >= EPSILON and guess <= max_guess:
        guess += step
        func_sol = guess ** 3 - guess ** 2 - 2
        
        
    if guess > max_guess:
        return None
    else:
        return guess
 
 
    
    
#Main Script
?????
if __name__ == '__main__':
    x = 3
    root_x = bisection(x)
       
    if (root_x):
        print('The square root of', x, 'by bisection method is', root_x)
    else:
        print('Failed to find the square root of', x)

????
##


import numpy
def bisection_x3_x2_2(guess_l:float, guess_h:float) -> float:
    '''
    Return the square root of x, calculated using an algorithmic technique known as bisection search
     >>> exhaustive_x3_x2_2(0,10)
    '''
    EPSILON = 0.01
    #Window = [guess_l,guess_h]
    guess = (guess_l + guess_h) / 2
    func_g_l = guess_l ** 3 - guess ** 2 - 2
    func_g_h = guess_h ** 3 - guess ** 2 - 2
    func_g = guess ** 3 - guess ** 2 - 2
    while abs(func_g) >= EPSILON:
        print('low =', guess_l, 'high =', guess_h, 'guess =', guess)
        if (numpy.sign(func_g) == numpy.sign(func_g_l)):
            guess_l = guess
            func_g_l = func_g
        else:
            guess_h = guess
            func_g_h = func_g
        guess = (guess_l + guess_h) / 2
        func_g = guess ** 3 - guess ** 2 - 2
    return guess

????
if __name__ == '__main__':
    x = 3
    root_x = bisection(x)
       
    if (root_x):
        print('The square root of', x, 'by bisection method is', root_x)
    else:
        print('Failed to find the square root of', x)

?????


##

# Selection Sort

# 2(cur_min) 6 5 1 3 4(2 is looking for smaller number compare to itself) is converted into first 1 6 5 2 3 4(2 and 1 were swapped)
# then 1 6(cur_min) 5 2 3 4(same goes for 6) is converted into 1 2 5 6 3 4(6 and 2 were swapped)
# steps go on until 1 2 3 4 5 6 is resulted.

    
              
def selection_sort(arr):
    '''
    
    '''
    for i in range(0, len(arr) - 1):
        cur_min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
                
                
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i] # swap


arr = [2, 6, 5, 1, 3, 4]

selection_sort(arr)
print(arr)

Executed
[1, 2, 3, 4, 5, 6]             



##

# Bubble Sort
 
# 5 3 8 6 7 2 (in this case first two integers are compared and when first integer is greater than second they are swappep -> 3 5 8 6 7 2, then 5 and 8 are compared. This time 5 is not greater than 8, so it is skipped. 8 is greater than 6, so it is swapped -> 3 5 6 8 7 2. then 3 5 6 7 8 2 then 3 5 6 7 2 8. Now first iteration is ended. But we still did not get 2 in the first place as current minimum. So there goes 2. iteration
# 3 5 6 7 2 8 goes 3 5 6 2 7 8 after 7 8 are gotten, iteration ends. At the 5. iteration what is gotten is 2 3 5 6 7 8


def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)
Executed
[2, 3, 5, 6, 7, 8]

##


# Insertion Sort
# we got 2 6 5 1 3 4, the formula for this sort is that first integer is labelled as sorted and the rest of them are unsorted. 2(sorted)|6 5 1 3 4(unsorted), then it becomes 2 6(sorted)| 5 1 3 4(unsorted), 2 and 6 are not swapped for 2 is already smalled than 6. Then we get 2 6 5|1 3 4, then 5 and 6 are swapped (2 5 6 1 3 4) -> 2 5 6| 1 3 4
#2 5 6 1| 3 4
#2 5 1 6| 3 4 #Swapping goes on until 1 is in the first place.
# 1 2 5 6| 3 4
# 1 2 5 6 3| 4
# 1 2 5 3 6|4
# 1 2 3 5 6|4
# 1 2 3 5 6 4|
# 1 2 3 5 4 6
# 1 2 3 4 5 6 Done

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
            




arr = [2, 6, 5, 1, 3, 4]
insertion_sort(arr)
print(arr)
Executed
[1, 2, 3, 4, 5, 6]


##

# Merge Sort

# Divide and Conquer
#Optimal running time
# Split array in half... 

# 2 6 5 1 7 4 3 split it 2 6 5 1 | 7 4 3
# 2 6|5 1       7 4 3
# 2 6     5 1         7 4 3
# 2 6     5 1        7 4      3
#Until 1 entry left
#2    6     5     1      7     4    3
# Merging them now much easier
# first 2 and 6 comes then for the second area it is 1 and 5, third one if 4 and 7 last one remains 3 
# (2 6) (1 5) (4 7) 3 now first two and last two areas are compared with each other

# (1 2 5 6) (3 4 7) like this/
# now this 2 area are compared lastly.
# 1 2 3 4 5 6 7 it is sorted completely now


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        
        #Merge
        i = 0 # left_arr idx
        j = 0 # right_arr idx
        k = 0 # merge _arr idx
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            
            
            
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1



arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]

merge_sort(arr)
print(arr)

Executed
[0, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7]

##

# Interpolation

#-Polynomial Interpolation

f(x) = an*x^n+....a1*x+a0
# 2 points uniquely  define a straight line(first order polynomial)

f(x) = y1 +(y2-y1) *((x-x1)/(x2-x1))

#x = 0 1
#y = 2 3  # Linear Interpolation

y = a*x + b
2 = a*0 + b
3 = a*1 + b     # b = 2  a = 1
# y = x + 1

# Now lets check 2. point (3 data points) polynomial

# x = 0 1 2
# y = 2 3 2   # Quadratic Interpolation


#y = ax^2 +bx +c
#2 = a*0^2 +b*0 +c
#3 = a*1^2 + b*1 +c
#2 = a*2^2 +b^2 +c
#2 = c
#3 = a + b + 2
#2 = 4a + 2b + 2
#y = -x^2 + 2x + 2


# Numpy = numpy.polyfit
#numpy.polyfit(x, y, deg)
#Example 1
x = [0,1]
y = [2,3]
deg = 1
import numpy

pol = numpy.polyfit(x, y, deg)
print(pol)
#Executed
#[1. 2.]

#Example 2
x = [0,1,2]
y = [2,3,2]
deg = len(x) - 1
pol_2 = numpy.polyfit(x, y, deg)
print(pol_2)
#Executed [-1.  2.  2.]

##

# Polynomial Regression

# Involves Errors
# Do not need to pass through any points as Interpolation

#Exercise 1

import numpy
import matplotlib.pyplot as plt

x = [0,1]
y = [2,3]
deg = 1

pol = numpy.polyfit(x, y, deg)
print(pol)
#Executed
#[1. 2.]

#Example 2
x = [0,1,2]
y = [2,3,2]
deg = len(x) - 1
pol_2 = numpy.polyfit(x, y, deg)
print(pol_2)
#Executed [-1.  2.  2.]

x = numpy.linspace(1,4,4)
y = [5.47, 7.08, 3.12, 2.90]
print(x)
#Executed [evaluate ecor1042 practice.py]
#[1. 2. 3. 4.]

plt.scatter(x,y)
plt.show()


#Example Regression

x = numpy.linspace(0,4,5)
y = [2,3,5,4,6]
deg = 1

coef = numpy.polyfit(x, y, deg)
print(coef)
#Executed [0.9 2.2]
x_e = numpy.linspace(0,4,100)
y_e = numpy.polyval(coef, x_e)
print(y_e)
#Executed
# [2.2        2.23636364 2.27272727 2.30909091 2.34545455 2.38181818
 2.41818182 2.45454545 2.49090909 2.52727273 2.56363636 2.6
 2.63636364 2.67272727 2.70909091 2.74545455 2.78181818 2.81818182
 2.85454545 2.89090909 2.92727273 2.96363636 3.         3.03636364
 3.07272727 3.10909091 3.14545455 3.18181818 3.21818182 3.25454545
 3.29090909 3.32727273 3.36363636 3.4        3.43636364 3.47272727
 3.50909091 3.54545455 3.58181818 3.61818182 3.65454545 3.69090909
 3.72727273 3.76363636 3.8        3.83636364 3.87272727 3.90909091
 3.94545455 3.98181818 4.01818182 4.05454545 4.09090909 4.12727273
 4.16363636 4.2        4.23636364 4.27272727 4.30909091 4.34545455
 4.38181818 4.41818182 4.45454545 4.49090909 4.52727273 4.56363636
 4.6        4.63636364 4.67272727 4.70909091 4.74545455 4.78181818
 4.81818182 4.85454545 4.89090909 4.92727273 4.96363636 5.
 5.03636364 5.07272727 5.10909091 5.14545455 5.18181818 5.21818182
 5.25454545 5.29090909 5.32727273 5.36363636 5.4        5.43636364
 5.47272727 5.50909091 5.54545455 5.58181818 5.61818182 5.65454545
 5.69090909 5.72727273 5.76363636 5.8       ]

plt.plot(x,y, 'o', x_e, y_e, '-')
plt.show()


##




































'''
# User Input
#calculator.py
list_of_supported_operators = ['+','*']

def add( op1, op2 ):
    return op1+op2

def multiply( op1, op2 ):
    return op1 * op2
# Add any command you want

def execute_command( command ):
    
    operator, op1, op2 = command
    
    if operator == '+':
        return add( op1, op2 )
    elif operator == '+':
        return multiply( op1, op2 )
    else:
        return None
    
command1 = ('+', 10, 20)
command2 = ('*', 10, 20)
result1 = execute_command( command1 )
result2 = execute_command( command2 )
print ( command1, ' = ', result1)
print( command2, ' = ', result2)

Executed
('+', 10, 20)  =  30
('*', 10, 20)  =  200

#Version of Using dict

dict_operator_functions = {'+':add, '*':multiply}

def execute_command( command ):
    
    operator, op1, op2 = command
    func = dict_operator_functions[operator]
    return func(op1, op2)

Executed
('+', 10, 20)  =  30
('*', 10, 20)  =  200

# Calculator

from calculator import *

def get_command():
    """
    Prompts the user for a legal  command, returning a tuple(operator, op1, op2)
    """
    
    operator = input('Please enter an operator + or * : ')
    while len(operator) != 1 and operato not in list_supported_operators:
        operator = input('Illegal format.\n Please enter an operator (+ or *): ')
        
    op1 = input('Please enter the first integer operand: ')
    op1 = int(op1)
   #op2 = int(op2)
    op2 = int(input('Please enter the second integer operand: '))
#Main Script    
more = 'Y'

while more.upper() == 'Y':
    command = get_command()
    result = execute_command( command )
    print(command, '=', result)
    
    more = input('Shall we go again? Y or N : ')

 
Executed
#Please enter the first integer operand: 1
#Please enter the second integer operand: 9
#('*', 1, 9) = 9
#Shall we go again? Y or N : Y
#Please enter an operator + or * : d
#Illegal format.
 #Please enter an operator (+ or *): d
#Illegal format.
# Please enter an operator (+ or *): 2
#Illegal format.
# Please enter an operator (+ or *): *
#Please enter the first integer operand: 9
#Please enter the second integer operand: 10
#('*', 9, 10) = 90
#Shall we go again? Y or N : n
#>>>

#
#batch_ui.py
from calculator import *
filename = 'calculator_batch.txt'

batch_file = open(filename)

for line in batch_file:
    items = line.split(' ')
    command = (items[0], int(items[1]), int(items[2]))
    result = execute_command( command )
    print(command, '=', result)
    
batch_file.close()
    
