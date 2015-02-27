def treesort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot ]
        right = [x for x in a[1:] if x >= pivot]
        return [treesort(left)] + [pivot] + [treesort(right)]

def _search(tree,x):
    if tree==[]:
        return tree
    if tree[1]==x:
        return tree
    if x<tree[1]:
        return _search(tree[0],x)
    else:
        return _search(tree[2],x)
    return tree

def sorted(tree):
    if tree==[]:
        return []
    return sorted(tree[0]) + [ tree[1]] + sorted(tree[2])

def search(tree,x):
    if _search(tree,x)==[]:
        return False
    else:
        return True

def insert(tree,x):
    if _search(tree,x)==[]:                
        subtree = _search(tree,x)
        subtree+=[[],x,[]]
    return tree

a = treesort([4,2,6,3,5,7,1,9])
print a
#print sorted(a)
#print _search(a,3)
#print _search(a,8)
b = insert(a,6.5)
#print b
c = insert(a,3)
#print c
