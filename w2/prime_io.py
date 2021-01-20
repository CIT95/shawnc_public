# must define run to use it for loop
run = 'Y'
# use while to define the beginning of the loop so we can send the user back
while(run == 'Y'):
    print ('I can tell you the prime numbers of any range you give me. ')
    print('What is your starting number?')
#need to define input as int
    start = int(input())
    print('What is your ending number?')
    end = int(input())
    for num in range (start,end +1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print (num)
    
    if start > end:
    #    for i in range(start, end + 1):
    #        print(i)
    #else:
             print('Your start number is higher than your end number. Please order your numbers from lowest to highest ')
    print ('Do you want me count again? Y for yes.')
    run = input()
    if(run !='Y'):
        # use continue to end the program if the use doesnt press Y
        print('thanks for using prime number generator')
    continue