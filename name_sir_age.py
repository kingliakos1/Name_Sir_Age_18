name = str(input("Enter your name: "))
sirname = str(input("Enter your sirname: "))
age = int(input("Enter your age: "))

def user_info(name, sirname, age):
    print(f"Hello {name} {sirname}, you are {age} years old.")
    return name, sirname, age

user_info(name, sirname, age)
