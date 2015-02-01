#read and try to figure out other code
#I went to pydata/pandas and used some of their smaller .py files to see what I understand
#and don't understand

# imports the module 'matplotlib.pyplot'  and saves it as 'plt'
import matplotlib.pyplot as plt

#imports the module random
import random

# imports the module pandas.util.testing and saves it as 'tm;
import pandas.util.testing as tm

#what the hell is the .N?
tm.N = 1000

#makes a data time frame called 'df'
df = tm.makeTimeDataFrame()

#imports a string (from where?)
import string

#creates an object called 'foo' might be a list of the first 5 letters
#from the first 200 lines?
foo = list(string.letters[:5]) * 200

#puts the list into a dictionary in data frame? not really sure
df['indic'] = list(string.letters[:5]) * 200

#shuffles the data object 'foo'
random.shuffle(foo)

#Totally confused at this point, another dictionary list...thing 
df['indic2'] = foo

#places them both in a boxplot with a fontsize of 8 and rotates them 90 degrees, horizontal?
df.boxplot(by=['indic', 'indic2'], fontsize=8, rot=90)

#displays it all
plt.show()


#another code source from pydata/pandas

# import 'numpy' and save it as np
import numpy as np

# import 'pandas.util.testing' and save it as tm
import pandas.util.testing as tm

# fairly obvious, from that place import this 
from pandas.core.internals import _interleaved_dtype

# create a variable called df and use the import from 'pandas.util.testing'
# which was saved as tm and make a data time frame, which I haven't learned
#a thing about
df = tm.makeDataFrame()

# in df there are these different values(?) and they are equal to these other values, maybe
df['E'] = 'foo'
df['F'] = 'foo'
df['G'] = 2

#something weird happens here, so df H is equal to df A if it is greater than 0?
df['H'] = df['A'] > 0

#variable blocks is now 'df._data.blocks' and I am not sure what blocks is
blocks = df._data.blocks

#variable items is now df.columns, also not sure where columns came from
#think it is a panda thing
items = df.columns

#learning is fun, even if I'm wrong
#feel free to explain things to me
