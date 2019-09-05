#Design an algorithm that finds the maximum positive integer input by a user
#The user repeatedly inputs numbers until a negative value is entered
#Algorihm
#1) Input numbers until negative value is entered
#2) When a negative number is entered 

max_int = 0

num_int = int(input("Input a number: "))    # Do not change this line

while num_int > 0:
    if num_int > max_int:
        max_int = num_int
    if max_int > 0:
        num_int = int(input("Input a number: "))
else:
    print("The maximum is", max_int)    # Do not change this line