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
# we will now add a few conditional statements to this program, this will reinforce the lessons on on flow contron the first will be a simple if then statement. i will check if a value is tue and print it.
def simple_if_then(num):
    if num >= 5:
        return True
    else:
        return False
result = simple_if_then(7)
print(result)


