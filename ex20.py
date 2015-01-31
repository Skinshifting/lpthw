from sys import argv

script, input_file = argv

#  "f" is just a variable name for the file
def print_all(f):
    print f.read()

# creates a function to go to the beginning of a file
# seek means to go to a particular place in file 0 is bytes	
def rewind(f):
    f.seek(0)

# create a function to print out one line
# line_count is the line number we want to read
# readline is a built in function that prints out one line	
def print_a_line(line_count, f):
    print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

# move to next line by incrementing the variable
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
