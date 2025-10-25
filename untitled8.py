names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #a list of names

search_name = input("who are you trying to find: ") #user inputs a name they're trying to find


if search_name in names: #if user inputs a name that is in the list "{search_name} was found in the list!" will appear
    print(f"{search_name} was found in the list!")
else: #if not "{search_name} was NOT found in the list." will appear
    print(f"{search_name} was not found in the list.")

