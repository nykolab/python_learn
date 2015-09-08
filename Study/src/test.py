in_list = [[[ [1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
summa = 0

def decompose(elem):
    global summa
    if isinstance(elem, list):
        for i in elem:
            decompose(i)
    else:
        summa = summa + int(elem)
        
decompose(in_list)
print "Sum of the elements in the list is {:<4d}".format(summa)
