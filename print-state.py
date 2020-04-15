string1 = "Hello "
string2 = "How old are you? "
age = 46
added_years = 10
print(string1 + string2 + str(age))
print("How old will you be in a decade?")
age += added_years
print (str(age))
# let us add a simple output  print statement with a special_item parameter and call the function with special_item= apples
def create_string(special_item):
    print("My favorite food is " + special_item + " and yours?")
create_string("Apples")


