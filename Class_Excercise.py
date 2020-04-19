# Instructions
# Create a Python list to store your grocery list as a list of strings. You need to buy:
#  Milk
#  Bread
#  Eggs
#  Peanut Butter
#  Jelly
# Print out the list
# Wait! Your cousin is visiting next week, and they’re allergic to peanuts! Change “peanut butter” in the list to “almond butter”.
# You just remembered that you have homemade jam that your neighbor made for you. Remove “jelly” from the list.
# You just used up the last of your coffee. Add “coffee” to your grocery list.
# Print out the updated list.

grocery_List = ["Milk", "Bread", "Eggs", "Peanut Butter", "Jelly"]
print(grocery_List)
grocery_List[3] = "Almond Butter"
grocery_List.remove("Jelly")
grocery_List.append("Coffee")
print(grocery_List)

