import random
from random import randint
def qselect(pos, list):
    if len(list)==1:
        return list[0]
    pivot = list[randint(0,len(list)-1)]
    left  = [x for x in list if x < pivot ] 
    right = [x for x in list if x >= pivot]
    """
    print "Pos is "
    print  pos
    print "Pivot is "
    print  pivot
    print left
    print right
    """
    if pos <= len(left):
        return qselect(pos, left)
    else:
        return qselect(pos-len(left),right)

print qselect(2, [3,10,4,7,19])
print qselect(4, [11,2,8,3])
