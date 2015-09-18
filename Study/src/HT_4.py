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

def filter_numbers():
    '''
    Given a string with a random text filter out all numbers from it
    
    Example:
    filter_numbers("Udds, 22! efjeghfjh 45@Hello") # Udds, ! efjeghfjh @Hello

    '''
print unused_digits(2015, 8, 26, "asdasd")