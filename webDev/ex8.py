# makes formatter into a string of four {} 
formatter = "{} {} {} {}"

# prints 1,2,3,4 in the format of formatter formatted
print(formatter.format(1,2,3,4))

# prints one,two,three,four in the format of formatter formatted 
print(formatter.format("one", "two", "three", "four"))

# prints True, False, False, True, in the format of formatter formatted
print(formatter.format(True, False, False, True))

# prints formatter in the format of format
print(formatter.format(formatter, formatter, formatter, formatter))

# prints text in the format of formatter formatted
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear",
))