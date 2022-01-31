# Lists
# A list is a collection of items, that is stored in a variable. The items should be related in some way, but there are no restrictions on what can be stored in a list. Here is a simple example of a list, and how we can quickly access each item in the list.

students = ['bernice', 'aaron', 'cody']

for student in students:
    print("Hello, " + student.title() + "!")


# Since lists are collection of objects, it is good practice to give them a plural name. If each item in your list is a car, call the list 'cars'. If each item is a dog, call your list 'dogs'. This gives you a straightforward way to refer to the entire list ('dogs'), and to a single item in the list ('dog').

# In Python, square brackets designate a list. To define a list, you give the name of the list, the equals sign, and the values you want to include in your list within square brackets.

# Eg. dogs = ['border collie', 'australian cattle dog', 'labrador retriever']


# Items in a list are identified by their position in the list, starting with zero. This will almost certainly trip you up at some point. Programmers even joke about how often we all make "off-by-one" errors, so don't feel bad when you make this kind of error.

# To access the first element in a list, you give the name of the list, followed by a zero in parentheses.

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

dog = dogs[0]
print(dog.title())


# The number in parentheses is called the index of the item. Because lists start at zero, the index of an item is always one less than its position in the list. So to get the second item in the list, we need to use an index of 1.

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

dog = dogs[1]
print(dog.title())


# You can probably see that to get the last item in this list, we would use an index of 2. This works, but it would only work because our list has exactly three items. To get the last item in a list, no matter how long the list is, you can use an index of -1.

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

dog = dogs[-1]
print(dog.title())

# This syntax also works for the second to last item, the third to last, and so forth.

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

dog = dogs[-2]
print(dog.title())


# NB: You can't use a negative number larger than the length of the list


# -----------------


# Lists and Looping
# Accessing all elements in a list

# We use a loop to access all the elements in a list. A loop is a block of code that repeats itself until it runs out of items to work with, or until a certain condition is met. In this case, our loop will run once for every item in our list. With a list that is three items long, our loop will run three times.

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print(dog)

# Lets understand how the last two lines work.
# -----------------------------------------------------------------------------
# - The keyword "for" tells Python to get ready to use a loop.
# - The variable "dog", with no "s" on it, is a temporary placeholder variable. This is the variable that Python will place each item in the list into, one at a time.
# - The first time through the loop, the value of "dog" will be 'border collie'.
# - The second time through the loop, the value of "dog" will be 'australian cattle dog'.
# - The third time through, "dog" will be 'labrador retriever'.
# - After this, there are no more items in the list, and the loop will end.


# Doing more with each item

# We are not limited to just printing the word dog. We can do whatever we want with this value, and this action will be carried out for every item in the list. Let's say something about each dog in our list.

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print('I like ' + dog.title() + 's.')


# Inside and outside the loop
# Python uses indentation to decide what is inside the loop and what is outside the loop. Code that is inside the loop will be run for every item in the list. Code that is not indented, which comes after the loop, will be run once just like regular code.

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print('I like ' + dog + 's.')
    print('No, I really really like ' + dog + 's!\n')

print("\nThat's just how I feel about dogs.")


# Enumerating a list
# When you are looping through a list, you may want to know the index of the current item. You could always use the list.index(value) syntax, but there is a simpler way. The enumerate() function tracks the index of each item for you, as it loops through the list:

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print("Results for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index)
    print("Place: " + place + " Dog: " + dog.title())


# The value in the variable index is always an integer. If you want to print it in a string, you have to turn the integer into a string:
# The index always starts at 0, so in this example the value of place should actually be the current index, plus one:

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print("Results for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index + 1)
    print("Place: " + place + " Dog: " + dog.title())
