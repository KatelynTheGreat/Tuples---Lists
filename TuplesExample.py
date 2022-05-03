
from turtle import turtles


tuples = ("apples","One",True,1)
tuples2 = (5, 2, 3,4)

#To change you have to make list!
tupleTOlist = list(tuples2)
tupleTOlist[0] = 1
print(tupleTOlist)


if "apples" in tuples:
    print(f"Apple can be found here is the full list: {tuples}")
    print(f"{tuples[0]}:{tuples2[0]}")  

