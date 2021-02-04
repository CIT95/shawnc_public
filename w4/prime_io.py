run = 'Y'

while(run == 'Y'):
    try:
        print ('I can tell you the prime numbers of any range you give me. ')
        print('What is your starting number?')
        start = int(input())
    
        print('What is your ending number?')
        end = int(input())
   
        if start > end:
            raise Exception
    except ValueError:
        print('You must enter a number')

    except Exception:
        print('Your start number is higher than your end number. Please order your numbers from lowest to highest ')
    else:
        for num in range (start,end +1):
            if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)
    finally:   
        print ('Do you want me count again? Y for yes.')
    run = input()
    if(run !='Y'):
        # use continue to end the program if the use doesnt press Y
        print('thanks for using prime number generator')
    continue