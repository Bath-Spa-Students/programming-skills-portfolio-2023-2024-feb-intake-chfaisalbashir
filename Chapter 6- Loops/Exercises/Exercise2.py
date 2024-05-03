#A movie theater charges different ticket prices depending on a person’s age. If a person is under 
#the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; 
#and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
#age, and then tell them the cost of their movie ticket



while True:
    age = input("Please enter your age (or 'exit' to finish): ")

    if age.lower() == 'exit':
        print("Thank you for using the movie ticket calculator. Goodbye!")
        break

    age = int(age)

    if age < 3:
        ticket_price = 0  # Ticket is free
    elif 3 <= age <= 12:
        ticket_price = 10  # it cost  $10
    else:
        ticket_price = 15  # it cost $15

    # ticket displaying 
    print(f"The cost of your movie ticket is ${ticket_price}.")

