# ps3.py
# Andy Vo
# Problem 6

# 3 time slots, 6 classes (A,B,C,D,E,F)
# invalid class pairs: (A,B),(A,C),(A,E),(B,D),(C,E),(C,D),(D,F),(E,F)

# part a
def s(x1,x2,x3):
    """ outputs True if the class X is scheduled at least once.
    """
    return x1 or x2 or x3

# part b
def n(x1,x2,x3):
    """ outputs True if the class X is scheduled no more than once.
    """
    return not(x1 and x2) and not(x1 and x3) and not(x2 and x3)

# part c
def ns(x1,x2,x3):
    """ outputs True if the class X is scheduled exactly once.
    """
    return s(x1,x2,x3) and n(x1,x2,x3)

# part d
def c(x1,x2,x3,y1,y2,y3):
    """ outputs True if the two classes X and Y are scheduled in different time slots.
    """
    return not(x1 and y1) and not(x2 and y2) and not(x3 and y3)

# part e
def isValid(a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3,e1,e2,e3,f1,f2,f3):
    """ outputs True if the schedule is valid for classes A,B,C,D,E, and F.
    """
    return (ns(a1,a2,a3) and ns(b1,b2,b3) and ns(c1,c2,c3) and ns(d1,d2,d3) and \
            ns(e1,e2,e3) and ns(f1,f2,f3)) and not(c(a1,a2,a3,b1,b2,b3)) and \
            not(c(a1,a2,a3,c1,c2,c3)) and not(c(a1,a2,a3,e1,e2,e3)) and \
            not(c(b1,b2,b3,d1,d2,d3)) and not(c(c1,c2,c3,e1,e2,e3)) and \
            not(c(c1,c2,c3,d1,d2,d3)) and not(c(d1,d2,d3,f1,f2,f3)) and \
            not(c(e1,e2,e3,f1,f2,f3))
