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
# ok now let us try to add to if statements, starting with an if and moving to an elif than giving an else statment to close it if the conditions are not true

def dual_if_then(num1, num2):
    if num1 == num2:
        return "numbers are equal"
    elif num1 > num2:
        return "number one is greater than number two"
    else:
        return "number one is smaller than number two"

result = dual_if_then(4 , 4)
result2 = dual_if_then(5, 4)
result3 = dual_if_then(3, 4)
print(result)
print(result2)
print(result3)

