# ps2.py
# Problem 5
# Andy Vo
# CS 131 A1
# p: you study cs
# q: you'll be smart
# r: you'll be happy
# if you study cs, you'll be smart and if you study cs, you'll be happy
# if you study cs, you'll be smart and happy

(p <= q) and (p <= r)
((not p) or q) and ((not p) or r) # Conditional Identity Law
(not p) or (q and r) # Distributive Law
p <= (q and r) # Conditional Identity Law
