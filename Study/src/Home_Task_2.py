in_list = [[[ [1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]

def decompose(elem):
    total = 0
    if isinstance(elem, int):
        total = total + elem
    elif isinstance(elem, list):
        for i in elem: 
            total += decompose(i)
    return total

print decompose(in_list)