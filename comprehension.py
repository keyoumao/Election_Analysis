# Instructions:
# …… Create a file called comprehensions.py.
# …… Create a list that prompts the user for the names of five people they know.
# Run the provided program. Note that nothing forces you to write the name “properly”—e.g., as “Jane” instead of “jAnE”. You will use list comprehensions to fix this.
#  …… First, use list comprehensions to create a new list that contains the lowercase version of each of the names your user provided.
# …… Then, use list comprehensions to create a new list that contains the title-cased versions of each of the names in your lower-cased list.
# Bonuses
# …… Instead of creating a lower-cased list and then a title-cased list, create the title-cased list in a single comprehension.
# Hints
# …… See the documentation for the title method.

names = []
for i in range(5):
    

    names.append(input("put name:"))

print(names)

uppercase = [name.upper() for name in names]
print(uppercase)

lowercase = [name.lower() for name in names]
print(lowercase)

title = [name.title() for name in names]
print(title)

Lower_title= [name.lower().title() for name in names]
print(Lower_title)