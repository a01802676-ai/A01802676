# Exercise 1: Write a python script that asks the user for their age and determine if they are adults or not

age   = 0 
age = int(input("What is your age?"))
if age < 18:
    print("You are not an adult.")
else:
    print("You are an adult.")

# Exercise 2: Write a python script that asks the user for their age and determine if they are teenagers or not

age   = 0 
age = int(input("What is your age?"))
if 13 <= age <= 19:    
    print("You are a teen.")
else:
    print("You are not a teen.")

# Exercise 3: Write a python script that asks the user for their birthday and determine their age

year = 0
year = int(input("What year where you born?"))
currenttime = int(input("What year is it now?"))

birthday = input("Have you had already your birthday? (yes/no):")
age = currenttime - year

if birthday == "no" :
    age = age - 1 
    print(age)

else:
    print(age)






