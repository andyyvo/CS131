# Python code that checks if a set of sets 'p' (a list of sets in Python because Python does not allow for sets of sets)
# is a partition of a set 's'.
# 'p' is a partition of 's' if and only if the union of the elements 'p' is equal to 's'
# and the intersection of any two elements of 'p' is an empty set.

def are_parts_nonoverlapping(p):
    """ returns True iff the intersection of any two elements
        of 'p' is the empty set.
    """
    for x in range(len(p)):
        for y in range(x+1,len(p)):
            if p[x].intersection(p[y]):
                return False
    return True

def do_parts_contain_element(x, p):
    """ returns True iff the element 'x'
        is an element of some element 'p'.
    """
    for a in range(len(p)):
        if x in p[a]:
            return True
    return False

def do_parts_cover_set(s, p):
    """ returns True iff every element of 's'
        is in some element of 'p'.
    """
    total = len(s)
    count = 0
    for i in s:
        if do_parts_contain_element(i,p):
            count += 1
    if count == total:
        return True
    else:
        return False

def do_parts_have_nothing_extra(s, p):
    """ returns True iff every element of every element
        of 'p' is in 's'.
    """
    for i in p:
        for j in i:
            if not j in s:
                return False
    return True

def is_partition(s, p):
    """ return True iff 'p' is a partition of 's'.
    """
    return are_parts_nonoverlapping(p) and do_parts_cover_set(s, p) and \
        do_parts_have_nothing_extra(s, p)


#print(are_parts_nonoverlapping([{0, 1}, {3, 5, 1}]))#false

#print(do_parts_contain_element(3, [{0, 1}, {3, 5}]))#true

#print(do_parts_cover_set({0,1,2,3,4}, [{0,5},{1,2},{3}]))#false

#print(do_parts_have_nothing_extra({0,1,2,3,4,5},[{0,1},{2},{3,4,5}]))#true
#print('\n')
#s = {1,2,3,4,5,6}
#p = [{1,4,5},{2,3},{6}]
#p1= [{1,4},{2,3},{6}]
#p2= [{1,4,5},{2,3},{6},{6}]
#p3= [{1,4,5},{},{2,3},{6}]
#print(is_partition(s,p))#true
#print(is_partition(s,p1))#false
#print(is_partition(s,p2))#false
#print(is_partition(s,p3))#false