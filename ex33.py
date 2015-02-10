print "\n ZED'S CODE: \n"
i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
	
print "The numbers: "

for num in numbers:
	print num
	
print "\n STUDY DRILL 1: Convert while loop to function and replace 6 with a variable \n"
def drill_1(n):
	i = 0
	numbers1 = []
	while i < n:
		print "Number: %d" % i 
		numbers1.append(i)
		i = i + 1
	print numbers1
	
drill_1(6)

print """\n STUDY DRILL 3: Add another variable to the function arguments that 
you can pass in that lets you change the + 1 on line 8 so you can change how 
much it increments by \n"""

def drill_3(n, s):
	i = 0
	numbers3 = []
	while i < n:
		print "Number: %d" % i 
		numbers3.append(i)
		i = i + s 
	print numbers3
	
drill_3(11, 2)

print "\n STUDY DRILL 5: Write it to use for-loops and range \n"

def drill_5(n, s):
	numbers5 = range(0, n, s)
	for i in numbers5:
		print "Number: %d" % i 
	print numbers5
	
drill_5(13, 2)
