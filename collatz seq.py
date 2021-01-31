def collatz(number):

    if number % 2 == 0:
        x = (number // 2)
    
    elif number % 2 == 1:
        x = (3 * number + 1)
        
    print(x)
    return x
    

try:
    n = int(input('enter a number: '))
    while n != 1:
        n = collatz(n)
        
except ValueError:
    print("You didn't enter an integer!")


