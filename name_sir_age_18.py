name = str(input("Enter your name: "))
sirname = str(input("Enter your sirname: "))
age = int(input("You must be 18 or older to proceed. Enter your age: "))

def user_info(name, sirname, age):
    if age >= 18:
        print(f"Hello {name} {sirname}, you are {age} years old.")
    else:
        print("You are not old enough.")

# Αυτή η γραμμή "καλεί" τη συνάρτηση.
user_info(name, sirname, age)