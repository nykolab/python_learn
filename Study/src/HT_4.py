import re

def unused_digits(*args):
    
    '''
    Given few numbers, you need to print out the digits that are not being used.

    Example:

    unused_digits(12, 34, 56, 78) # "09"
    unused_digits(2015, 8, 26) # "3479"

    '''
    
    all_int = []
    exp_int = []

    for i in args:
        if isinstance(i, int):
            all_int.extend(map(int, str(i)))
    
    for n in xrange(10):
        if n not in all_int:
            exp_int.append(n)
    
    if exp_int:
        return "".join(map(str, exp_int))


def filter_numbers(string):
    
    '''
    Given a string with a random text filter out all numbers from it
    
    Example:
    filter_numbers("Udds, 22! efjeghfjh 45@Hello") # Udds, ! efjeghfjh @Hello

    '''
    
    output = []

    if isinstance(string, str):
        for i in string:
            try:
                map(int, i)
            except ValueError:
                output.append(i)
        return "".join(output)

                
def initials(string):
    
    '''
    Format a "U.S."-like name

    Example:
    initials('chris whales') # C. Whales
    initials('Barack Hussain obama') # B. H. Obama

    '''
    
    if isinstance(string, str):
        name = []
        surname = string.split()[-1].title()
        
        for i in string.split()[:-1]:
            abr = i[0].title() + "."
            name.append(abr)
        if surname:
            name.append(surname)
        if name:
            return " ".join(name)


def high_and_low(string):    
    
    '''
    Given a string of space separated numbers, and have to return the highest and lowest number.

    Example:

    high_and_low("1 2 3 4 5")  # "5 1"
    high_and_low("1 2 -3 4 5") # "5 -3"
    high_and_low("1 9 3 4 -5") # "9 -5"

    '''
    
    if isinstance(string, str):
        l = map(int, string.split())
        return "{} {}".format(max(l), min(l))
    
    
def encryption(string):
    
    '''
    Morse Code
    Given Morse code map:
    
    
    Write a function that will translate text into Morse:
    encryption("HELLO WORLD") # ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
    encryption("THE QUICK BROWN FOX") #  "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-"

    '''
    
    CODE = {'0': '-----', '1': '.----', '2': '..---', '4': '....-', '6': '-....', 
            '8': '---..', 'B': '-...', 'D': '-..', 'F': '..-.', 'H': '....', 
            'J': '.---', 'L': '.-..', 'N': '-.', 'P': '.--.', 'R': '.-.', 
            'T': '-', 'V': '...-', 'X': '-..-', 'Z': '--..', 'b': '-...', 
            'd': '-..', 'f': '..-.', 'h': '....', 'j': '.---',  'l': '.-..', 
            'n': '-.', 'p': '.--.', 'r': '.-.', 't': '-', 'v': '...-', 
            'x': '-..-', 'z': '--..', '1': '.----', '3': '...--', '5': '.....',  
            '7': '--...', '9': '----.', 'A': '.-', 'C': '-.-.', 'E': '.', 
            'G': '--.', 'I': '..', 'K': '-.-', 'M': '--', 'O': '---', 
            'Q': '--.-', 'S': '...', 'U': '..-', 'W': '.--', 'Y': '-.--', 
            'a': '.-', 'c': '-.-.', 'e': '.', 'g': '--.', 'i': '..', 
            'k': '-.-', 'm': '--', 'o': '---', 'q': '--.-', 's': '...', 
            'u': '..-', 'w': '.--', 'y': '-.--'}
    output = []

    if isinstance(string, str):
        for char in string:
            try:
                if re.match('\s', char):
                    output.append(char)
                elif CODE[char]:
                    output.append(CODE[char])
            except KeyError:
                print "Character {} cannot be decoded".format(char)
        return " ".join(output)            
                

def divisors(number):     
    
    '''
    Find the number of divisors of a positive integer n.

    Example:
    
    divisors(4) # 3 -- 1, 2, 4
    divisors(5) # 2 -- 1, 5
    divisors(12) # 6 -- 1, 2, 3, 4, 6, 12
    divisors(30) # 8 -- 1, 2, 3, 5, 6, 10, 15, 30
    '''
    
    if isinstance(number, int) and number >= 0:
        d = [i for i in range(1, number//2 + 1) if not number % i] + [number]
        return len(d)
    
    
        
# --------------------------------------                

if __name__ == '__main__':
    
    # task 1 
    assert unused_digits(2015, 8, 26, "asdasd") == "3479"
    assert unused_digits(12, 34, 56, 78, "asdasd") == "09"
    
    # task 2
    assert filter_numbers("Udds, 22! efjeghfjh 45@Hello") == "Udds, ! efjeghfjh @Hello"
    
    # task 3
    assert initials('chris whales') == "C. Whales"
    assert initials('Barack Hussain obama') == "B. H. Obama"
    
    # task 4
    assert high_and_low("1 2 3 4 5") == "5 1"
    assert high_and_low("1 2 -3 4 5") == "5 -3"
    assert high_and_low("1 9 3 4 -5") == "9 -5"
    
    # task 5
    assert encryption("HELLO WORLD") == ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
    assert encryption("THE QUICK BROWN FOX") == "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-"
    
    # task 6
    assert divisors(4) == 3
    assert divisors(5) == 2
    assert divisors(12) == 6
    assert divisors(30) == 8
