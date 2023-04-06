'''source: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
this problem looks to create a square root function
so we ensure a positive floating point integer as an input'''
def readNum():

    n = float(input ("Enter your positive number:  "))

    while n < 1:
        print("This is not a positive number")
        n = float(input ("Please be sure to input a positive number:  "))

n = readNum()
#and then we look at outputting the square root of the number
#using Newtons Method

def mySqrt(n) : 
    x = n

    count = 0

    while (1) :
        count += 1

        root = 0.5 * (x + (n / x))

        if (abs(root - x) < 1) :
            break
        #update root
        x  = root
    return root
        
print(f"The square root of {n} is approximately {mySqrt(n)}")

