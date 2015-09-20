
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
    
    
                
if __name__ == '__main__':
    
    assert unused_digits(2015, 8, 26, "asdasd") == "3479"
    assert unused_digits(12, 34, 56, 78, "asdasd") == "09"

    assert filter_numbers("Udds, 22! efjeghfjh 45@Hello") == "Udds, ! efjeghfjh @Hello"
    
    assert initials('chris whales') == "C. Whales"
    assert initials('Barack Hussain obama') == "B. H. Obama"
    
