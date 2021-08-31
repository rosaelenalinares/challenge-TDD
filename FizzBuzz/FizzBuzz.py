def isDivisible():
    print("Enter a number:", end=" ")
    n = int(input())
    if n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0: 
        print('Buzz')
    else: 
        n % 3 == 0 and n % 5 == 0
        print('FizzBuzz')
isDivisible()