academy = input("please enter academy name: ")
if academy == "GOA":
    print("true")
else:
    print("you made a HORIBLE desision")
#_______________________________________________
budget = int(input("please enter your budget: "))
phone_value = 2000
if budget >= phone_value:
    print("your able to buy this product, congratz !")
else:
    print(budget - phone_value )

#_________________________________________________

num1 = int(input("please enter whole number: "))
if num1 >= 5:
    print(num1 * 2)
else:
    print(num1 * 4)
#________________________________________________
ticket = 10
ticket_amount = int(input("please enter ticket cuantiity: "))
if ticket_amount <= 5:
    print(ticket * ticket_amount)
else:
    ticket = (ticket - 3)
    print(ticket * ticket_amount)
#___________________________________________________
number = int(input("please enter your first number: "))
number2 = int(input("please enter second number: "))
#____________________________________________________
calculate1 = int(input("please enter any number: "))
calculate2 = int(input("please enter second number: "))
operation = int(input("please enter any operation: "))
if operation == "+":
    print(calculate1 + calculate2)
if operation == "-":
    print(calculate1 + calculate2)
if operation == "*":
    print(calculate1 * calculate2)
else:
    print(calculate1 / calculate2)

    