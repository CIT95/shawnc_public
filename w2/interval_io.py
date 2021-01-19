# must define run to use it for loop
run = 'Y'
# use while to define the beginning of the loop so we can send the user back
while(run == 'Y'):
    print ('I can count. Just tell me where to start')
    print('What is your starting number?')
#need to define input as int
    start = int(input())
    print('What is your ending number?')
    end = int(input())
    if start < end:
        for i in range(start, end + 1):
            print(i)
    else:
        print('Your start number is higher than your end number. Do it right!')
    print ('Do you want me count again? Y for yes.')
    run = input()
    if(run !='Y'):
        # use continue to end the program if the use doesnt press Y
        print('fine I was getting tired of this')
    continue