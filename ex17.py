from sys import argv
from os.path import exists
#os.path is used because different operating
#systems specify file paths differently
#exists is a function that returns
#"TRUE" if file path is valid

script, from_file, to_file = argv
#give name of files that you are copying
#from and to in the command line

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()
#one line: indata = open(from_file).read()
#you would have to remove in_file.close()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

#one line version
#from sys import argv; from os.path import exists; script, from_file, to_file = argv; indata = open(from_file).read(); out_file = open(to_file, 'w'); out_file.write(indata); out_file.close()
