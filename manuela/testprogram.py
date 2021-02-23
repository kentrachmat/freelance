from Ask import *

check = False
while not check:
    some_text = input('Input some text: ')
    check,some_text = check_datatype(some_text,"String","You must input some text")
print(some_text)

check = False
while not check:
    some_text = input('Input an integer: ')
    check,ett_heltal = check_datatype(some_text,"Int","You must input an integer")
print(ett_heltal)

check = False
while not check:
    some_text = input('Input a float: ')
    check,a_float = check_datatype(some_text,"Float","You must input a number")
print(a_float)

check = False
while not check:
    some_text = input('Input an integer between 10 and 20: ')
    check,ett_heltal = check_interval(some_text,10,20,"You must input a number between 10 and 20")
print(ett_heltal)
