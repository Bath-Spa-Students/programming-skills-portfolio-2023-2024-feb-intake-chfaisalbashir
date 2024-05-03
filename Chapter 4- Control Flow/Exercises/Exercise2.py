#Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

#•If the alien’s color is green, print a statement that the player just earned 5 points 
#for shooting the alien.

#•If the alien’s color isn’t green, print a statement that the player just earned 10 points.

#•Write one version of this program that runs the if block and another that runs the else block.


# Version that runs the if block (black alien)
alien_color = str(input("Enter the color of alien "))
if alien_color == 'black':
    print("Player just earned 5 points for shooting the black alien.")
else:
    print("Player just earned 10 points.")