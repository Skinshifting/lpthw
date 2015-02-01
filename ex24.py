print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# \\ to show the \
# \n newline
# \t for tab
# \' to show the '


poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# """ to span multiple lines

print "-------------"
print poem
print "-------------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
# it is 5

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
# So the argument 'started' confused me at first
# it can be any argument, just used in the function
# as a local variable and return saves it for later use
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)
# calls the function and uses the the 3 variables
# stored in the return, name doesn't matter
# it follows the order

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
#the rest of the code is obvious
