# Muhammet Furkan Yalcin - 101233944

from lab1_functions import test_float
from lab1_functions import test_int
from lab1_functions import max_min
from lab1_functions import sum_y


# Exercise 1

# Q. What is displayed when Python evaluates point1? 
# >>>point1 = [13.0,12.0]
# >>>point1
# [13.0,12.0]


# Q. What is displayed when Python evaluates point1?
# >>>point1.append(4.0)
# >>>point1
# [13.0,12.0,4.0]


# Q. What is displayed each time Python evaluates point1?
# >>> point1.pop(0) # Remove the item at index 0 in the list
# >>> point1
# [12.0,4.0]
# >>> point1.pop() # Remove the last item in the list
# >>> point1
# [4.0]



# Q. What is displayed when the last two statements are evaluated?
# >>> point1 = (13.0, 12.0)
# >>> type(point1)
# tuple
# >>> point1
# (13.0, 12.0)


# Q. What is displayed when Python evaluates x and y?
# >>> x = point1[0]
# >>> y = point1[1]
# >>> x
# 13.0
# >>> y
# 12.0


# Q. What is displayed when Python evaluates x and y?
# >>> point2 = (14.0, 16.0)
# >>> x, y = point2
# >>> x
# 14.0
# >>> y
# 16.0


# Q. What is displayed when Python executes each statement?
# Q. Also, copy the following code as a comment and write the answers to the questions:
# >>> point2[0] = 12.0 # Can we change the point to (12.0, 16.0)?
# TypeError: 'tuple' object does not support item assignment
# >>> point2.append(4.0) # Can we add a third coordinate?
# AttributeError: 'tuple' object has no attribute 'append'
# >>> point2.pop(0) # Can we remove the first coordinate?
# AttributeError: 'tuple' object has no attribute 'pop'


# >>> points = [(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)]
# >>> points[0]
# (1.0, 5.0)
#>>> points[1]
# (2.0, 8.0)
# >>> points[2]
# (3.5, 12.5)


# Main Script
# Exercise 2




max1 = max_min([(13,11),(9,7)])
max2 = max_min([(24,1),(36,12)])
max3 = max_min([(-122,8),(-1,39),(97,-3)])



#

print('Exercise 2.1: ',max1)
print('Exercise 2.2: ',max2)
print('Exercise 2.3: ',max3)


t2_1 = test_float('Testing 2.1',[(13,11),(9,7),(13,7)], [(13,11),(9,7),(13,7)])
t2_2 = test_float('Testing 2.2',[(24,1),(36,12),(36,1)],[(24,1),(36,12),(36,1)])
t2_3 = test_float('Testing 2.3',[(-122,8),(-1,39),(97,-3),(97,-122)],[(-122,8),(-1,39),(97,-3),(97,-122)])

print('Exercise 2.1: ',t2_1)
print('Exercise 2.2: ',t2_2)
print('Exercise 2.3: ',t2_3)


# Exercise 3

# Q. What is displayed when points is evaluated? 
# >>> points = {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}
# >>> points
# {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}


# Q. What is displayed when points is evaluated? 
# >>> point1 = (1.0, 2.0)
# >>> point2 = (4.0, 6.0)
# >>> point3 = (10.0, -2.0)
# >>> points = {point1, point2, point3}
# >>> points
# {(1.0, 2.0),(4.0, 6.0),(10.0, -2.0)}


# Q. What is displayed when points is evaluated? 
# >>> points = set()
# >>> points.add(point1)
# >>> points.add(point2)
# >>> points.add(point3)
# >>> points
# {(1.0, 2.0),(4.0, 6.0),(10.0, -2.0)}


# >>> points.add(point2)
# >>> points
# {(1.0, 2.0),(4.0, 6.0),(10.0, -2.0)}
# Q. How many copies of point (4.0, 6.0) are in the set?
# Nothing changes since point2 is a replication on set and it only shows up once in set.


# Q. What is displayed when points[0] is evaluated? 
# >>>points[0]
# TypeError: 'set' object is not subscriptable


# Q. What is displayed when this loop is executed? 
# >>> for point in points:
#         ...
#         print(point)
#         ...
# (4.0, 6.0)
# (1.0, 2.0)
# (10.0, -2.0)







# Exercise 4









sum1 = sum_y({(1,3),(5,7),(2,9)})
sum2 = sum_y({(13,34),(12,65)})
sum3 = sum_y({(23,32),(11,21),(9,3)})



#

print('Exercise 4.1: ',sum1)
print('Exercise 4.2: ',sum2)
print('Exercise 4.3: ',sum3)


t4_1 = test_int('Testing 4.1',19,19)
t4_2 = test_int('Testing 4.2',99,99)
t4_3 = test_int('Testing 4.3',56,56)

print('Exercise 4.1: ',t4_1)
print('Exercise 4.2: ',t4_2)
print('Exercise 4.3: ',t4_3)


