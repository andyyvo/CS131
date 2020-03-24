# ps4-code
# Andy Vo

def js(A,B):
    """ inputs two sets A and B and
        returns the Jaccard similarity.
        """
    C = []
    D = []
    for i in A:
        if i in B:
            C.append(i)
    for i in A:
        D.append(i)
    for i in B:
        if i not in D:
            D.append(i)
    return (len(C)) / (len(D))

def jd(A,B):
    """ inputs two sets A and B and
        returns the Jaccard distance.
        """
    return 1 - js(A,B)
