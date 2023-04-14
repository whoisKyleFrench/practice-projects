# Welcome the user to the program
print(
    "\nWelcome to MLG, the Mad Libs Generator program!\n\nLet's create a silly story!\nI'll ask you for some nouns, verbs and adjectives and we'll use those to generate a silly sentence.\n\nLet's begin!"
)

# Get the user input
noun_input = input("\nEnter a noun: ")
print("Good one!")
verb_input = input("\nEnter verb: ")
print("Nice!")
adjective_input = input("\nEnter an adjective: ")
print("\nPerfect! That's it!\nHere is your silly story:")

# Setup grammar handling
a_an = ["a", "an"]
options = ("a", "e", "i", "o", "u")
if noun_input.startswith(options):
    a_or_an = a_an[1]
else:
    a_or_an = a_an[0]
