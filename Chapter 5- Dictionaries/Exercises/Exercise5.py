#Make several dictionaries, where each dictionary represents a different pet.
#In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your 
#list and asyou do, print everything you know about 
#each pet
#make an empty list t store the pets in.

#make an empty list t store the pets in.
pets={}

pet1={"Animal type": "Tiger", "Onwer": "Ali", "Pet name": "Cheeta", }
pet2={"Animal type": "Parrot", "Onwer": "Hassan",   "Pet name": "Motto"}
pet3={"Animal type": "5", "Onwer": "4", "Pet name": "2"}
pet4={"Animal type": "1", "Onwer": "3" ,"Pet name": "7"}


pets=[ pet1,pet2,pet3,pet4]
for pet in pets:
    print(f"\nAnimal type: {pet['Animal type']}")
    print(f"Onwer: {pet ['Onwer']}")
    print(f"Pet name: {pet ['Pet name']}")
       