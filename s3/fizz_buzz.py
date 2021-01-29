def fizz_buzz():
    userinput = input('Enter Your Number: ')
    val = (int(userinput))
    # From stack overflow  
    # You can simply use % Modulus operator to check divisibility. 
    # For example: n % 2 == 0 means n is exactly divisible by 2 and n % 2 != 0 means n is not exactly divisible by 2.
    if(val % 5) == 0 and (val % 3) == 0:
        return('FizzBuzz')
    elif(val % 3) == 0:
        return('Fizz')
    elif(val % 5) == 0:
        return('Buzz')
    else:
        return(val)

print(fizz_buzz())
