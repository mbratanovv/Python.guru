from random import randint

def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(str(item))
    print()

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

fruits = ["Orange", "Apple", "Banana", "Kiwi", "Watermelon", "Peach"]
print("Hello " + first_name + " " + last_name + ", your lucky fruit is : " + fruits[randint(0, len(fruits))])

print_list(fruits, "List of fruits:")

favorite_fruit = input("What is your favorite fruit? ")
if favorite_fruit not in fruits:
    fruits.insert(0, favorite_fruit)
    print_list(fruits, "Now check the list again, your favorite fruit is first! ")
else:
    print_list(fruits, "You can find your favorite fruit in the list below! ")


while first_name and last_name != "":
    age = int(input("Now tell us your age: "))
    status = input("As well as your status [student/employee]? ")

    new_message = "Hello again Mr. " + last_name 

    if status == "employee" and (age >= 23 and age <= 40):
        new_message += ", you have 50% chance of winning our brand new Iphone XS!"
    elif status == "student" and (age <= 23):
        new_message += ", you have 80% chance of winning our brand new Iphone XS!"
    else:
        new_message += ", you are not entitled to participate"

    print(new_message)
    break
    print()
        


print()
input("Press return to continue ...")
