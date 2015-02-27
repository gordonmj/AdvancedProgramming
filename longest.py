def treesort(a): #I find writing trees out hard (matching the brackets) so I just included a tree-builder
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot ]
        right = [x for x in a[1:] if x >= pivot]
        return [treesort(left)] + [pivot] + [treesort(right)]

def _longest(tree): # helper function, because I don't want to print all four elements, just size of longest path and path itself
    if tree==[]:
       return 0,[],0,[] #longest path is zero length, no nodes in longest, depth is 0, no nodes in deepest 
    leftlengthofpath,leftlongestpath,depthofleft,deepestleftpath = _longest(tree[0]) #get all four values for left subtree
    rightlengthofpath,righttlongestpath,depthofright,deepestrightpath = _longest(tree[2]) # get all four values for right subtree
    defaultlongestpath = depthofleft+depthofright+1 
    if depthofleft >= depthofright:
        depth, deepestpath = depthofleft+1,deepestleftpath+[tree[1]] # use depth and path from left
    else:
    	depth, deepestpath = depthofright+1,[tree[1]]+deepestrightpath # use depth and paath from right
    if leftlengthofpath == max(leftlengthofpath,rightlengthofpath,defaultlongestpath):
       nodelist = leftlongestpath 
    elif rightlengthofpath == max(leftlengthofpath,rightlengthofpath,defaultlongestpath):
       nodelist = righttlongestpath
    else:
       nodelist = deepestleftpath+[tree[1]]+deepestrightpath #if longest path not contained entirely in one subtree
    return max(leftlengthofpath,rightlengthofpath,defaultlongestpath),nodelist,depth,deepestpath # return all 4 to caller

def longest(tree):
    return _longest(tree)[0]-1,_longest(tree)[1] #I get the number of edges, not nodes, so I just subtract one


b = treesort([1,2,3])
print b
print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
print longest(b)
c = treesort([1,2,3,4,5,6,7,8,9])
print c
print longest(c)
