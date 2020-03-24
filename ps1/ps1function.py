# ps1.py
# CS 131 - Spring 2020, Assignment 1
# Problem 4
# Name: Andy Vo

def shouldWeSki(a,b,c,d,e):
    """ All five inputs are Boolean values. True is a preference
        to ski. False is a preference to study. Output reflects
        True if the majority wants to ski, and False if the majority
        wants to study.
        """
    return (a and b and c) or (a and b and d) or (a and b and e) or\
           (a and c and d) or (a and c and e) or (a and d and e) or\
           (b and c and d) or (b and c and e) or (b and d and e) or\
           (c and d and e)
