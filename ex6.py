# variable x assigned to a string %d means decimal value
x = "There are %d types of people." % 10
# variable assigned to strings
binary = "binary"
do_not = "don't"
# variable assigned to string with %s variables as strings
y = "Those who know %s and those who %s." % (binary, do_not)

# code begins - print the values
print x
print y

# print the strings with the values
print "I said: %r." % x
print "I also said: '%s'." % y

#boolean set to false
hilarious = False
# %r stands for repr string containing a printable representation of an object
joke_evaluation = "Isn't that joke so funny?! %r"

#calls for the boolean
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#prints without a space between
print w + e

#print with a space between
print w, e
