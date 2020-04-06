# The famed unsolved Number Theory problem
# The Collatz conjecture
# written by Andy Vo

# Let a_0 be a positive integer
# a_{i+1} = ((1/2)a_i if a_i is even) and (3a_i + 1 if a_i is odd)

def collatz_function(a):
    """ when given a positive number a_i returns a_{i+1}
        according to the definition of the Collatz Sequence.
    """
    if a >= 1:
        if a%2 != 0:
            return 3*a + 1
        else:
            return a // 2

def collatz_sequence(a):
    """ when given a positive number a returns the
        Collatz Sequence (as a list) starting at a_0 = a
        which terminates at some n where a_n = 1.
    """
    collatzList = []
    collatzList.append(a)
    while a > 1:
        if a%2 != 0:
            a = 3*a + 1
        else:
            a = a // 2
        collatzList.append(a)
    return collatzList

def smallest_int_with_collatz_length(n):
    """ returns the smallest int whose Collatz Sequence
        has length at least n.
    """
    length = 0
    val = 0
    while length < n:
        val += 1
        length = len(collatz_sequence(val))
    return val

# counterexample = 272