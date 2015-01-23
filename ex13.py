from sys import argv
# sys means system files
# import that adds functions to python
# constitutes a module of code
# modules can also be libraries
# argv is an argument variable
# variables that you send in or pass to python

script, first, second, third = argv
# unpacks argv into four variables from left to right

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#when you run this script, type the variables
# python ex13.py first_thing second_thing last_thing
