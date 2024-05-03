 #Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
#As they enter each topping, print a message saying you’ll add that topping to their pizza.

#selecting toppings
prompt="\nwhich topping would you like on your pizza?"
prompt+="\nenter'end when you are done:"

while True:
    topping=input(prompt)
    if topping!='end':
        print(" I'll add{topping} to your pizza.")
    else:
        break

    