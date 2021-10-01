import random
import time

#Function to check word validity     
def check_if_exists(x):    
    ls = []
    f = open('C:/Users/K/Desktop/scrabblewordlist.txt')  # Loading dictionary
    ls=[]
    for line in f:
        ls.append(line.strip())
    if x.upper() in ls:
        return True
    else:
        return False

# Funtion to get score
def get_score(word):
    SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    total = 0
    for letter in word.lower():
        total += SCORES[letter]
    return total

# Function to check for numbers
def check_for_num(word):   
    for letter in word.lower():
        if letter.isdigit(): # Check for numbers and display appropriate message
            return False                            
    return True          

# Function to generate random word length
def generate_random_length():
    word_length = random.randint(2,10)    
    return word_length

# Function to check word length
def check_length(word,word_length):
    if len(word) ==word_length:
        return True
    else:
        return False

# Function to check time taken by the user
def check_timetaken(time_taken):
    if time_taken > 15:
        print('Time is up!! You took', time_taken, 'seconds')
        return False
    else:
        return True

# Function to calculate time bonus
def calculate_bonus(time_taken):
    bonus=15-time_taken
    return bonus

# Function to get user input   
def get_user_input(word_length):  
    
    print('Please enter a word with', word_length, 'letters..')
    start = int(time.time())
    word = input().strip()
    if check_for_num(word):
        if check_length(word,word_length):
            if check_if_exists(word):
                end = int(time.time())
                time_taken=end-start
                if check_timetaken(time_taken):
                    time_bonus=calculate_bonus(time_taken)
                    score=get_score(word)
                    print("Time taken:", time_taken, "seconds")
                    print('Word Score:',score) # Score for word
                    print('Time Bonus:',time_bonus) # Extra score for answering quickly
                    print('Total Score:',score + time_bonus, '\n')
                    print('~SCRIBBLE~\n')
                else:
                    quit()
            else:
                print('Word is invalid!')
                quit()
        else:

            print('Word length does not match!')
            quit()
    else:
        print('Numbers not allowed') 
        quit()           
                    
# Function to execute main program    
def scrabble():
    print('~SCRIBBLE~\n')
    print("You have 15 seconds to answer!")
    word_length = generate_random_length()
    get_user_input(word_length)
    
scrabble()