'''
   The purpose of this file is to demonstrate automatic testing
   using the Unit Testing Framework
'''
from fib_lib import fibonacci
from unit_testing import check_equal
def test_fib( ) -> None:
    '''
       Test cases for function fibonacci
    '''
    # Test fibonacci(1) because this a boundary case (fibonacci's docstring
    # states that n must be positive int, so 1 is the smallest integer
    # for which fibonacci should return a value.)
    
    # Test fibonacci(2) because this is also a boundry case, as it also
    # returns 1
    
    # Test fibonacci(3) because 3 is the smallest argument for which the 
    # function returns a different value than fibonacci(1)
    # (What if fibonacci always returned 1? fibonacci(1) and fibonacci(2)
    # would return correct values; i.e., 1, but the function isn't correct.
    # We wouldn't detect this unless we have a test case where the expected
    # result is an int other than 1).
    
    # Test fibonacci(7) because the previous two cases aren't sufficient to
    # determine if the function generates the correct sequence.
    check_equal('fibonacci(1)', fibonacci(1), 1)
    check_equal('fibonacci(2)', fibonacci(2), 1)
    check_equal('fibonacci(3)', fibonacci(3), 2)
    check_equal('fibonacci(7)', fibonacci(7), 13)
    
    

    
# Main script
test_fib()