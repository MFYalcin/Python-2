'''
ECOR1042 - Summer 2022 Review exercise

'''
import string

def load_data(file_name:str)->dict:
    '''
    Return a dictionary that has the students' information from the file 
    file_name
    
    '''
    infile = open(file_name, 'r')
    
    count = 0
    student_dict = {}
    for line in infile:
        student_info = line.strip().split(',')        
        if count == 0:
            table_header = student_info
        else:
            if not(int(student_info[0]) in student_dict):
                student_dict[int(student_info[0])] = {}
            for i in range(1, 4):
                if i != 3:
                    student_dict[int(student_info[0])][table_header[i]] = student_info[i]
                else: # Grades should be saved as integers
                    student_dict[int(student_info[0])][table_header[i]] = int(student_info[i])
        
        count += 1
    infile.close()    
    return student_dict            



# Main Script
if __name__ == "__main__":
    
    from dict_functions import print_dictionary
    file = "Student_info.csv"

    student_dict = load_data(file)
    print_dictionary(student_dict)
    print()





