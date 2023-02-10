from student_grades import load_data
import numpy as np
import matplotlib.pyplot as plt

def print_dictionary (dictionary:dict):
    '''
    function to print the dictionary one item in a line
    '''
    for item in dictionary:
        print("{" + str(item) + ":" + str(dictionary.get(item)) + "}")
    
    
    
def add_student(dictionary:dict, studentTuple:tuple)->dict:
    """
    The function takes two arguments, the dictionary where the student must be added and 
    a tuple argument (student number, first name, last name and grade).
    The function adds a student to the dictionary and verifies that the student has been added. 
    The function returns the updated dictionary and prints a message stating, 
    The student has been added correctly or There was an error adding the student. 
    
    >>> student_dict = add_student(student_dict, (123456780,"Rami", "Sabouni", 100))
    The student has been added correctly
    
    >>> student_dict = add_student(student_dict, (123456780,"Rami", "Sabouni", 100))
    Student wasn't added as their record exists
    """

    student_number = studentTuple[0]
    student = {}
    student['First Name'] = studentTuple[1]
    student['Last Name'] = studentTuple[2]
    student['Grade'] = studentTuple[3]

    if student_number in dictionary:
        print("Student wasn't added as their record exists") 
    else:
        dictionary.update({student_number:student})
        print("The student has been added correctly") 
    
    return dictionary

def remove_student(dictionary:dict, student_number:int)->dict:
    """
    The function takes two arguments, the dictionary from where the student must
    be removed and the student number that needs to be removed
    The function removes a student from the dictionary and verifies that the student has been removed. 
    The function returns the updated dictionary and prints a message stating, 
    The student has been removed correctly or There was an error removing the student. 
    
    >>> student_dict = remove_student(student_dict, 123456780)
    The student has been removed correctly

    >>> student_dict = remove_student(student_dict, 123456780)
    There was an error removing the student. student number not found.
    """
    
    if student_number in dictionary:         
        student_info = dictionary.pop(student_number)
        print("The student has been removed correctly")     
    else:
        print("There was an error removing the student. student number not found.") 

    return dictionary

# bubble sort
def get_students_by_number(dictionary:dict)->dict:
    '''
    Returns sorted dictionary based on student numbers using bubble sort algorithm
    '''
    student_numbers = list(dictionary.keys())
    j = 0
    n = len(student_numbers)
    for i in range (n):
        for j in range (0, n - i - 1):
            if student_numbers[j] > student_numbers[j+1]:
                student_numbers[j], student_numbers[j+1] = student_numbers[j+1], student_numbers[j]
                
    result = {}
    for number in student_numbers:
        student = dictionary.get(number)
        result.update({number: student})
        
    return result 

# insertion sort
def get_students_by_first(dictionary:dict)->dict:
    '''
    Returns sorted dictionary based on first name using insertion sort algorithm
    '''    
    n = len(dictionary)
    student_numbers = list(dictionary.keys())
    
    for i in range(1, n):
        key = student_numbers[i]
        key_value = dictionary[key]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        
        while j >=0 and key_value['First Name'] < dictionary[student_numbers[j]]['First Name']:
            student_numbers[j+1] = student_numbers[j]
            #dictionary[student_numbers[j+1]] = dictionary[student_numbers[j]]
            #pprint(dictionary)    
            j -= 1
            
        student_numbers[j+1] = key
        
    result = {}
    for number in student_numbers:
        student = dictionary.get(number)
        result.update({number: student})        
    return result
    
# Selection sort
def get_students_by_last(dictionary:dict)->dict:
    '''
    Returns sorted dictionary based on last name using selection sort algorithm
    '''     
    n = len(dictionary)
    student_numbers = list(dictionary.keys())
    
    # Traverse through all array elements 
    for i in range(n):
        
        # Find the minimum element in remaining
        # unsorted array
        min_idx =i
        for j in range(i+1, n):
            if dictionary[student_numbers[min_idx]]['Last Name'] > dictionary[student_numbers[j]]['Last Name']:
                min_idx =j
                
        # Swap the found minimum element with
        # the first element
        student_numbers[i], student_numbers[min_idx] = student_numbers[min_idx], student_numbers[i]
        
    result = {}
    for number in student_numbers:
        student = dictionary.get(number)
        result.update({number: student})        
    return result


# Merge sort
def get_students_by_grade(dictionary:dict)->dict:
    '''
    Returns sorted dictionary based on student grades using merge sort algorithm
    '''     
    n = len(dictionary)
    student_numbers = list(dictionary.keys())
    student_grades = []
    for student in student_numbers:
        student_grades += [dictionary[student]['Grade']]
    
    mergeSort(student_numbers, student_grades)
    
    result = {}
    for number in student_numbers:
        student = dictionary.get(number)
        result.update({number: student})        
    return result


def mergeSort(arr1, arr2):
    '''
    Sort both arrays based on the values in arr2
    '''
    if len(arr1) > 1:
        mid = len(arr1)//2 # Finding the mid of the array
        L1 = arr1[:mid] # Dividing the array elements
        L2 = arr2[:mid] # Dividing the array elements
        
        # into 2 halves
        R1 = arr1[mid:]
        R2 = arr2[mid:]
        mergeSort(L1, L2) # Sorting the first half
        mergeSort(R1, R2) # Sorting the second half
        
        i = j = k = 0
        
        # Copy data to temp arrays L[] and R[]
        while i < len(L1) and j < len(R1):
            if L2[i] < R2[j]:
                arr1[k] = L1[i]
                arr2[k] = L2[i]
                i += 1
            else:
                arr1[k] = R1[j]
                arr2[k] = R2[j]
                j += 1
            k += 1
            
        # Checking if any element was left
        while i < len(L1):
            arr1[k] = L1[i]
            arr2[k] = L2[i]
            i += 1
            k += 1
        while j < len(R1):
            arr1[k] = R1[j]
            arr2[k] = R2[j]
            j += 1
            k += 1

def count_passed(dictionary:dict) -> tuple:
    '''
    Returns number of students in the course and number of students passed (over C-)
    
    '''
    count = 0
    for student in dictionary:
        if dictionary.get(student)['Grade'] >= 60:
            count += 1
            
    return (len(dictionary), count)

def plot_grades(dictionary:list):
    '''
    Plots the histogram of student's grades (A, B, C, D, F)
    Features used:
    - Dictionary to create the histogram
    - polyfit( ) for Curve fitting
    - polyval( ) for finding the y value based on the x value
        (plugging in the x values in the function from the curve fitting)
    - Some extra plot manipulation settings
    '''
    student_numbers = list(dictionary.keys())
    student_grades = []
    for student in student_numbers:
        student_grades += [dictionary[student]['Grade']]
    
    hist = {'F':0, 'D':0, 'C':0, 'B':0, 'A':0}
    for grade in student_grades:
        if 0 < grade < 50:
            count = hist.get('F', 0)
            hist.update({'F':count+1})
        elif 50 <= grade < 60:
            count = hist.get('D', 0)
            hist.update({'D':count+1})
        elif 60 <= grade < 70:
            count = hist.get('C', 0)
            hist.update({'C':count+1})
        elif 70 <= grade < 80:
            count = hist.get('B', 0)
            hist.update({'B':count+1})
        elif 80 <= grade:
            count = hist.get('A', 0)
            hist.update({'A':count+1})
    
        
    x = np.linspace(0, 4, 5)
    y = list(hist.values())
    deg = 2
    coef = np.polyfit(x, y, deg)
    #print(coef)    

    x_e = np.linspace(0,4,100)
    y_e = np.polyval(coef,x_e)
    
    plt.plot(x, y, '*',x_e, y_e, '-')

    x_ticks = list(hist.keys())    
    plt.xticks(range(len(x_ticks)), x_ticks)    

    plt.xlabel("Grade")
    plt.ylabel("# of occurences")

    plt.grid()
    plt.show()
    

if __name__ == "__main__":
    student_dict = load_data("Student_info.csv")
    print_dictionary(student_dict)
    student_dict = add_student(student_dict, (123456780,"Rami", "Sabouni", 100))
    print()
    print_dictionary(student_dict)
    student_dict = get_students_by_number(student_dict)
    print()
    print_dictionary(student_dict)
    student_dict = get_students_by_first(student_dict)
    print()
    print_dictionary(student_dict)
    student_dict = get_students_by_last(student_dict)
    print()
    print_dictionary(student_dict)
    student_dict = get_students_by_grade(student_dict)
    print()
    print_dictionary(student_dict)
    print()
    print(count_passed(student_dict))
    
    plot_grades(student_dict)