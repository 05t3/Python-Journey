# Whitespace
# The term "whitespace" refers to characters that the computer is aware of, but are invisible to readers. The most common whitespace characters are spaces, tabs, and newlines.

# Tabs and newlines are represented by special character combinations.
# The two-character combination "\t" makes a tab appear in a string. Tabs can be used anywhere you like in a string.

print("Hey there!")
print("\tHey there!")
print("Hey \tThere!")


# Expected output
# Hey there!
#         Hey there!
# Hey     There!


# The combination "\n" makes a newline appear in a string. You can use newlines anywhere you like in a string.

print("Hey there!")
print("\nHey there!")
print("Hey \nThere!")


# Expected output
# Hey there!

# Hey there!
# Hey
# There!


# Stripping whitespace

name = ' eric '

print('-' + name.lstrip() + '-')
print('-' + name.rstrip() + '-')
print('-' + name.strip() + '-')
