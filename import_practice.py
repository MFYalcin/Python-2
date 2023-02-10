'''
import practice

filename = 'practice.txt'
print('test case')
hist = practice.histogram_txt(filename)
print(hist)
most_freq, freq = practice.freq_word(hist)
print("The most frequently occuring word is \"", most_freq,
      "\" which occurs", freq, "times") 


from practice import fibonacci

def auto_test(desc:str,actual,expected)->None:
    
        
    if actual == expected:
        print('Test passed')
        return 1
        
    else:
        print('Test failed')
        return 0
        
ex1 = auto_test('fibonacci(1)',fibonacci(1),1)
ex2 = auto_test('fibonacci(2)',fibonacci(2),3)
ex3 = auto_test('fibonacci(7)',fibonacci(7),13)
print(ex1)
print(ex2)
print(ex3)
# Test passed
# Test failed
# Test passed
#1
#0
#1


from practice import *

filename = 'calculator2.txt'
infile = open(filename)

for file in infile:
    items = file.split(' ')
    command = (items[0],int(items[1]),int(items[2]))
    
    result = execute_command(command)
    print(command,' = ', result)
infile.close()

('*', 2, 3)  =  6
('+', 10, 20)  =  30
('-', 10, 30)  =  None
('+', 30, 89)  =  119
('*', 1, 9)  =  9


def get_command()->tuple:
    operator = input('Please enter and integer(+ or *): ')

    while len(operator) != 1 and operator not in list_of_op:
        operator = input('Illegal Format\nPlease enter an operator(+ or *): ')
    
    op1 = input('Please enter the first integer operand: ')
    op1 = int(op1)
    
    op2 = int(input('Please enter the second integer operand: '))
    return (operator, op1, op2)

more = 'Y'

while more.upper() == 'Y':
    command = get_command()
    result = execute_command(command)
    print(command, ' = ', result)
    more = input('Shall we go again? Y or N: ')

'''


def print_dictionary(dictionary:dict):
    for item in dictionary:
        print("["+str(item)+':'+str(dictionary.get(item))+']')

