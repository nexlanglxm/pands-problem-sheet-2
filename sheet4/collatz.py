#defining the function
def collatz(number):
    if (number % 2 == 0):#if the number is even
        return number // 2
    elif (number % 2 == 1):
        return number * 3 + 1   #if the number is odd
    else:
        print ("Something went wrong in collatz")
        return None
#if forget to assign type there will be an error!
#creation of the user input area
number = int(input("Please type in your number : ")) 
#defining the conditions for quit()
while (number == 1):
    print("This will not work when the number is equal to 1")
    quit()

#the other
print("The Collatz sequence for the number you entered : ")
print(number)
while (number != 1):
    number = collatz(number)
    print(number)

print(number)