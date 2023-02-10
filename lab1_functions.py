# Muhammet Furkan Yalcin - 101233944

def max_min(lst:list)->list:
    """Returns a list of tuples such that two values which are minimum and maximum numbers of the current list of tuples are included in the new tuple list.
    >>>max_min([(13,11),(9,7)])
    [(13,11),(9,7),(13,7)]
    >>>max_min([(24,1),(36,12)])
    [(24,1),(36,12),(36,1)]
    >>>max_min([(-122,8),(-1,39),(97,-3)])
    [(-122,8),(-1,39),(97,-3),(97,-122)]
    
    """
    n_min = min(min(lst))
    n_max = max(max(lst))
    new_lst = lst.append((n_max,n_min)) 
    return lst


  
def test_float(desc:str, expected:float, actual:float)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed.
    >>>test_float('Testing 1.1',21.4,21.3)
    Test failed      # Just to emphasize, normally passed.
    0
    >>>test_float('Testing 1.2',40.5,40.2)
    Test failed
    0
    >>>test_float('Testing 1.3',20.4,20.4)
    Test passed
    1
    '''
    print("Expected result:", expected, "Actual result:", actual)
    if expected == actual:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0 


def test_int(desc:str, expected:int, actual:int)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed.
    >>>test_int('Testing 1.1',21,22)
    Test failed      # Just to emphasize, normally passed.
    0
    >>>test_int('Testing 1.2',40,68)
    Test failed
    0
    >>>test_int('Testing 1.3',20,20)
    Test passed
    1
    '''
    print("Expected result:", expected, "Actual result:", actual)
    if expected == actual:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0 


def sum_y(s:set)->int:
    """Returns an integer where a set of tuples indicates x and y coordinate values and a tuple contaning these two elements and sum of y values are returned in the end as integer.
    >>>sum_y({(1,3),(5,7),(2,9)})
    19
    >>>sum_y({(13,34),(12,65)})
    99
    >>>sum_y({(23,32),(11,21),(9,3)})
    56
    """
    sum = 0
    for items in s:
        y = items[1]
        sum += y
    return sum
    
    
    