# Integers

# Addition +
# Subtraction -
# Division /
# Multiplication *
# Exponents **

print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3**2)


# Expected output
# 5
# 1
# 6
# 1.5
# 9


# You can use parenthesis to modify the standard order of operations.
standard_order = 2+3*4
print(standard_order)

my_order = (2+3)*4
print(my_order)


# Expected output
# 14
# 20


# Floating-Point numbers

# Floating-point numbers refer to any number with a decimal point.


print(0.1+0.1)

# Expected output
# 0.2


# However, sometimes you will get an answer with an unexpectly long decimal part:

print(0.1+0.2)

# Expected Output
# 0.30000000000000004

# Explanantion
# This happens because of the way computers represent numbers internally; this has nothing to do with Python itself. Basically, we are used to working in powers of ten, where one tenth plus two tenths is just three tenths. But computers work in powers of two. So your computer has to represent 0.1 in a power of two, and then 0.2 as a power of two, and express their sum as a power of two. There is no exact representation for 0.3 in powers of two, and we see that in the answer to 0.1+0.2.

# You can also get the same kind of result with other operations.
# i.e

print(3*0.1)


# Expected Output
# 0.30000000000000004

# NB: There are a couple differences in the way Python 2 and Python 3 handle numbers. In Python 2, dividing two integers always results in an integer, while Python 3 always returns a float. This is fine when the result of your integer division is an integer, but it leads to quite different results when the answer is a decimal.


# Python 2.7
print 4/2
print 3/2

# Expected Output
# 2
# 1

# Python 3.3
print(4/2)
print(3/2)

# Expected Output
# 2.0
# 1.5
