# Strings
# Strings are sets of characters. Strings are easier to understand by looking at some examples.

# Strings are contained by either single or double quotes.


my_string = "Oste"
my_string = 'Oste'

# Example of strings that contain quotations.

quote = "Linus Torvalds once said, 'Any program is only as good as it is useful.' "
quote = 'Linus Torvalds once said, "Any program is only as good as it is useful." '


# Changing case
# You can easily change the case of a string, to present it the way you want it to look.


first_name = 'eric'

print(first_name)
print(first_name.title())


# OUTPUT WOULD LOOK LIKE:
# eric
# Eric


# Some of the most common cases are lower, title, and upper.

print(first_name.title())
print(first_name.upper())
print(first_name.lower())

# OUTPUT WOULD LOOK LIKE:
# Eric
# ERIC
# eric

# Combining strings (concatenation)
# The plus sign combines two strings into one, which is called "concatenation". You can use as many plus signs as you want in composing messages. In fact, many web pages are written as giant strings which are put together through a long series of string concatenations.

first_name = 'lucifer'
second_name = 'morningstar'

full_name = first_name + ' ' + second_name
print(full_name.title())


first_name = 'lucifer'
second_name = 'morningstar'

full_name = first_name + ' ' + second_name

message = full_name.title() + ' ' + "is the main character in Lucifer TV series."
print(message)
