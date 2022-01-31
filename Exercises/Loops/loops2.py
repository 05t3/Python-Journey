# First List - Loop
# Repeat First List, but this time use a loop to print out each value in the list.

games = ['football', 'golf', 'tennis', 'squash', 'basktball']
for game in games:
    print(game)


# First Neat List - Loop
# Repeat First Neat List, but this time use a loop to print out your statements. Make sure you are writing the same sentence for all values in your list. Loops are not effective when you are trying to generate different output for each value in your list.

games = ['football', 'golf', 'tennis', 'squash', 'basktball']

for game in games:
    print("I play " + game.title() + ".")

# Your First List - Loop
# Repeat Your First List, but this time use a loop to print out your message for each item in your list. Again, if you came up with different messages for each value in your list, decide on one message to repeat for each value in your list.

games = ['football', 'golf', 'tennis', 'squash', 'basktball']

for game in games:
    print("I play " + game.title() + ".")
    print("I really love " + game.title() + ".")
print("\nThose are just some of my favourite games.")
