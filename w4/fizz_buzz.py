#def fizz_buzz():
#    userinput = input('Enter Your Number: ')
 #   userinput = (int(userinput))
  #  # From stack overflow  
    # You can simply use % Modulus operator to check divisibility. 
    # For example: n % 2 == 0 means n is exactly divisible by 2 and n % 2 != 0 means n is not exactly divisible by 2.
   # if(userinput % 5) == 0 and (userinput % 3) == 0:
    #    return('FizzBuzz')
    #elif(userinput % 3) == 0:
    #    return('Fizz')
    #elif(userinput % 5) == 0:
    #    return('Buzz')
    #else:
    #    return(userinput)


print('Please enter your number: ')
userinput = input()
try:
    if (int(userinput) % 5) == 0 and (int(userinput) % 3) == 0:
        print('FizzBuzz')
    elif (int(userinput) % 3) == 0:
        print('Fizz' )
    elif (int(userinput) % 5) == 0:
        print('Buzz')      
except ValueError:
    print('You did not enter a number')
else:
    print('Your number is divisible by 3 and or 5')
finally:
    print('Play Again!')
