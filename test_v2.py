from scr_code_v2 import *

# Entering a valid word returns True
def test_case1(): 
    print('"Cabbage" is a valid word so it returns True')
    assert check_if_exists('cabbage') == True    
    
# Entering an invalid word returns False
def test_case2(): 
    print('"sfksdfji" is not a valid word, so it returns False')
    assert check_if_exists('sfksdfji') == False 

# Entering a valid word with lower and upper cases returns True
def test_case3(): 
    print('The word "Cabbage" with lower and upper cases is valid')
    assert check_if_exists('Cabbage') == True    
    
# Entering a valid word with upper case returns True
def test_case4(): 
    print('The word "CABBAGE" with upper case is valid')
    assert check_if_exists('CABBAGE') == True
    
# Entering a valid word returns True
def test_case5():
    print('The word "sunny" has no digits in it so it returns True')
    assert check_for_num('sunny') == True   
    
# Entering a digit returns False
def test_case6():
    print('The word "cabb2ge" has digit in it so it returns False')
    assert check_for_num('cabb2ge') == False   
    
# The function calculates the correct score
def test_case7():
    print('The word "Cabbage" returns the correct score of 14') 
    print('C:3\na:1\nb:3\nb:3\na:1\ng:2\ne:1\nScore:14')
    assert get_score('Cabbage') == 14 
  
# The function calculates the correct score
def test_case8():
    print('The word "boat" returns the correct score of 6')
    print('b:3\no:1\na:1\nt:1\nScore:6')
    assert get_score('boat') == 6 

# The function asks to input a random number (from 2 to 10)
def test_case9(): 
    print('The program randomly generates word length requirement between 2 and 10 every time')
    num = generate_random_length()
    print('Random word length generated is',num)
    assert num >1 and num<11
   
# The function compares the word length with the required length
def test_case10():
    print('The word "Cabbage" matches the required length "7" and returns True')
    assert check_length('Cabbage',7) == True
  
# The function compares the word length with the required length
def test_case11():
    print('The word "Boat" doesn not match the required length "7" and returns False')
    assert check_length('Boat',7) == False

# The function checks if the time taken by user is under 15 seconds, and should return True
def test_case12():
    print('The user has taken less than 15 seconds and returns True')
    assert check_timetaken(14) == True  

# The function checks if the time taken by user is more than 15 seconds, and should return False
def test_case13():
    print('The user has taken more than 15 seconds and returns False')
    assert check_timetaken(16) == False

 # The function calculates the time bonus
def test_case14():
    print('More points are given as a bonus if the user takes less time')
    print('Time taken = 5\nTime bonus = 10 (15-5)')
    assert calculate_bonus(5) == 10  

 # The function calculates the time bonus
def test_case15():
    print('Less points are given as a bonus if the user takes more time')
    print('Time taken = 10\nTime bonus = 5 (15-10)')
    assert calculate_bonus(10) == 5   