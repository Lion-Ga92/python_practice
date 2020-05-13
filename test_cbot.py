# I want to see if i can make a multi input chatbot with the small knowledge that i have.
def chat_bot1():
    print("Hello and welcome")
    response_1 = input("How are you?")
    if response_1 ==  "Fine":
        print("That is great")
        print("What are you doing today?")
        response_2 = input("Are you working?")
        if response_2 == "Yes":
            print("Ok")
        elif response_2 == "No":
            print("Ok let us talk")
    elif response_1 == "Not bad":
        print("Ok that is good")
    else:
        print("Please respomd with either fine or Not bad")
print("Hello and welcome to our prototype chat bot, valid respones are Fine, Not bad, Yes, and No. please try to keep your responses with in this capitalization")
chat_bot1()

