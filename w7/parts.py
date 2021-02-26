resistors = {'100k': 14,
             '10k':'6', 
             '10r': '34', 
             '500r': '12', 
             '1k': '3', 
             '390r': '44', 
             '3.3k': '7'}
##add a key to a dd

#print(resistors.setdefault('100r', False))
#output - False

##sort (ascending or descending) 

bin1 = {'a1': '100k',
        'a2': '10r',
        'a3': '1k',
        'a4': '10k' }
#sort_location = sorted(bin1.items())
#print(sort_location)
##output - [('a1', '100k'), ('a2', '10'), ('a3', '1k'), ('a4', '10k')]

##check whether a given key already exists in a dd

#print(resistors.get('100k',0))
##output 14
#print(resistors.get('470r',0))
##output 0 

##iterate over dd using for loops
##filter a dd based on values

#for value, quantity in resistors.items():
#    print('I have  '+ quantity +', '+ value +' resistors')
##output - 
## I have  14, 100k resistors
## I have  6, 10k resistors
## I have  34, 10r resistors
## I have  12, 500r resistors
## I have  3, 1k resistors
## I have  44, 390r resistors
## I have  7, 3.3k resistors


#while True: 
#    print('Enter a resistor value: (blank to quit)') 
#    name = input()
#    if name == '': 
#        break 
#    for value, quantity in resistors.items():
#        if value == name:
#            print('I have  '+ quantity +' '+ value +' resistors')
#        else:
#            print('I do not have a ' + name) 

##take your dd and create a list of dd

allBins = [{
    'location':'bin1',
    'section':'a1',
    'quantity':25
}, {
    'location':'bin1',
    'section':'a2', 
    'quantity': 5
}, {
    'location':'bin1' , 
    'section': 'a3',
    'quantity': 14
}]

##iterate over the list of dd

filter_by_quantity = [f for f in allBins if f['quantity'] < 7]
#print(filter_by_quantity)
##output - [{'location': 'bin1', 'section': 'a2', 'quantity': 5}]

##and output summary data (total, average, min, max etc)

#print(str(len(filter_by_quantity))+ 'bin(s) below quantity threshold' )       
##output - 1bin(s) below quantity threshold    