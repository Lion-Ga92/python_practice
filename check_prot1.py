task_1 = "Cut Corn"
run = True

print("Welcome to our checklist app")
print("To exit type 'quit'")

def checklist_func():
    comp_task1_check = input("Have you comp. task 1?")
    global task_1
    task_list = []
    if comp_task1_check == "Complete":
        task_list.append((task_1, comp_task1_check))
        return print(task_list)
    elif comp_task1_check == "Not complete":
        task_list.append((task_1, comp_task1_check))
        return print(task_list)
    elif comp_task1_check == "quit":
        run = False
    else:
        print("Response not valid")

while run:
     checklist_func()

