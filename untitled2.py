name = input("Enter your name: ")#will  show "enter your name:" and user will enter their name
hometown = input("Enter your hometown: ")#will  show "enter your hometown:" and user will enter where their from
age = int(input("Enter your age: "))#will  show "enter your age:" and user will enter how old they are


person = { 
    "name": name,
    "hometown": hometown,
    "age": age
} #will store data or the values as pairs


print(person["name"], person["hometown"], person["age"], sep="\n") #prints the saved values for ""person"

