from dict_functions import *
from student_grades import *

COMMANDS = ['l','a','r','g','c' , 'p', "q"]
SUB_COMMANDS = ['s','f','l','g']
def display_commands():
    """
    The available commands are:
    1- L)oad data
    2- A)dd student
    3- R)emove student
    4- G)et students
    5- C)ount number of students passed
    6- P)lot grade distribution
    7- Command line Q)uit
    Please type your command: <one space>
    """
    print("1- L)oad file")
    print("2- A)dd student")
    print("3- R)emove student")
    print("4- G)et students (sorted)")
    print("5- C)ount number of students passed")
    print("6- P)lot grade distribution")
    print("7- Command line Q)uit")
    

def commands():
    loaded = False    
    display_commands()
    text = input("\nPlease type your command: ")
        
    while text.lower() != "q":
        if (text.lower() in COMMANDS) == False:  # if no a valid command
            print("\nError: No such command line\n")   
        elif text.lower() == "l" :
            print("Enter file name: ")
            file_name= input()   
            student_dict = load_data(file_name)    
            loaded = True
            print(" ")            
        elif loaded == False:
            print("Error: No file loaded\n")
        elif text.lower() == "a" : 
            student_number = int(input("Please enter a 10 digit student number: "))
            first_name = input("Please enter student's first name: ")
            last_name = input("Please enter student's last name: ")
            grade = int(input("Please enter student's grade: "))
            while 0 > grade < 100:
                grade = int(input("Error: Value should be between 0 and 100\n: Please enter student's grade: "))
            add_student(student_dict, (student_number, first_name, last_name, grade))
            print(" ")
        elif text.lower() == "r" : 
            student_number = int(input("Please enter a student's number to remove: "))
            remove_student(student_dict,student_number)
            print(" ")            
        elif text.lower() == "g" :
            print("Select how to sort the retrived information:")
            text = input("\t S)tudent Number\tF)irst Name\tL)ast name\tG)rade : ")
            valid = False
            while valid == False:  # if no a valid sub command
                if (text.lower() in SUB_COMMANDS) == False:
                    print("\nError: No such command line\n")
                    print("Select how to sort the retrived information:")
                    text = input("\t N)umber\tF)irst Name\tL)ast name\tG)rade : ")                    
                else:
                    valid = True
                    if text.lower() == "s" : 
                        print_dictionary(get_students_by_number(student_dict))
                    elif text.lower() == "f" : 
                        print_dictionary(get_students_by_first(student_dict))
                    elif text.lower() == "l" : 
                        print_dictionary(get_students_by_last(student_dict))
                    elif text.lower() == "g" : 
                        print_dictionary(get_students_by_grade(student_dict))
                        
        elif text.lower() == "c" :
            number, passed = count_passed(student_dict)
            print("\nNumber of students passed the course " + str(passed) + " out of " + str(number) + " students\n")
        
        elif text.lower() == "p" :
            plot_grades(student_dict)
            
        display_commands()
        text = input("Please type your command: ")        
    
    return

commands()