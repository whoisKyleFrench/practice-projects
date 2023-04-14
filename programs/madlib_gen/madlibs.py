# Welcome the user to the program
welcome_msg = "\nWelcome to MLG, the Mad Libs Generator program!\n\nLet's create a silly story!\nI'll ask you for some nouns, verbs and adjectives and we'll use those to generate a silly sentence.\n\nLet's begin!"
print(welcome_msg)

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

# Define and print the sentence
sentence = f"\nOne day, I was walking to the store when I ran into a {noun_input}.\nAt first I was a little confused, but then I decided to just {verb_input}.\nAfter all, how often do you see {a_or_an} {noun_input} that is so {adjective_input}?!\n"
print(sentence)
