name = 'Shay'
age = 31 # not a lie
height = 64 # inches
weight = 110 # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "That would be %d centimetres." % (height * 2.54)
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the soda." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
