# Análisis de temperaturas x semana
temp  = [20,30,26,21,23,32,25]

promedio= sum (temp)/ len(temp)
print( promedio)

for item in temp :
    if item >= promedio:
        print(item,"is above average")
    
    else:
        print(item,"is belove avarage")

#Students exercises
students=["Maria,Pablo,Pato,Romina,Regina,Pedro"],
st_grades=[90,60,80,95,75,88,92]

print((sum (st_grades)/ len(st_grades)), "is the avarage")

FailSudent=0

PassStudent=0

for grade in st_grades:
    if grade < 70:
        FailStudent= FailStudent + 1

    else:
        PassStudent=  PassStudent +1
    
print(PassStudent,"students passed" )

print(FailStudent,"students Fail" )

# Lists
shopping_list = ["Milk", "Bread", "Eggs", "Butter"]
purchased = [False, True, False, False]

# a) Show items not yet purchased
for i in range(len(shopping_list)):
    if not purchased[i]:
        print(f"You still need to buy: {shopping_list[i]}")

# b) Ask user if they have purchased the remaining items
for i in range(len(shopping_list)):
    if not purchased[i]:
        answer = input(f"Have you bought {shopping_list[i]}? (yes/no): ").lower()
        if answer == "yes":
            purchased[i] = True

# c) Remove purchased items from the list
remaining_items = [shopping_list[i] for i in range(len(shopping_list)) if not purchased[i]]

print("\nUpdated shopping list (still need to buy):", remaining_items)
    

numbers = [10, 15, 22, 33, 42, 55, 60]

# Separate lists
even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

usernames = ["anna", "bob", "carla"]

# Check duplicates and ask for new username
while True:
    new_name = input("Enter a username: ").lower()
    if new_name not in usernames:
        usernames.append(new_name)
        print("Username added successfully!")
        break
    else:
        print("That name already exists. Try another one.")

print("Updated list of usernames:", usernames)


