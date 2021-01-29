def program1(age = 0):
    userinput = input('Guess my age: ')
    age = (int(userinput))
    if age != 50:
       return ('wrong!')
    else:    
       return ('how did you know?!?!?')
print(program1())

def program2():
    userinput2 = input('Guess my name: ')
    name = userinput2
    if name != 'steve':
        return ('wrong! my name is not ' + name)
    else:    
       return ('how did you know?!?!?')
print(program2())