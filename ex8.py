formatter = "%r %r %r %r"
# %r can read any kind of data, works well for debugging

print formatter % (1, 2, 3, 4)
# calls to replace the %r with the numbers
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# doesn't need quotes as they are built in values
print formatter % (formatter, formatter, formatter, formatter)
# reads formatter variable as text shows %r
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
#split so it doesn't go over 80 characters in a line which is considered bad form
