print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheesecake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Play dead."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	elif bear == "3":
		print "It is a common misconception that this works. You die a very horrible death."
	elif bear == "shoot it":
		print "You don't have a weapon so you attempt to shoot it with your fingers. You fail miserably and get eaten."
	else:
		print "Well %s is probably better. You live for now." % bear
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		
else:
	print "You stumble around and fall on a knife and die. Good job!"
