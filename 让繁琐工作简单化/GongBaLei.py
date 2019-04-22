# this program says hello and ask for my name
print('Hello world')
print('What is your name?') # ask for their name
myname = input()
# the return from  input is 'str'.
print('It is good to meet you,' + myname)
print('The length of your name is:')
print(len(myname)) # the return from len() is int.
print('What is your age?')
myage = input()
print('You will be ' + str(int(myage) + 1) + ' in a year.') 
# '+' only work for int and int, or str and str, not for others.
# str() convert ('') into str forcibly.
print('What is your goal for studying pyton?')
mygoal = input()
print('Your goal is to reducing work time!')
print('GonBaLei!')
print('How much do you exercise?')
myextime = input()
print('Ok!' + ' Do you study python today?')
print('Yes' + ' or ' + 'No')
myanswer = input()
if myanswer == 'Yes':
    print('Congratulations!' + ' See you tommorow.')
else:
    print('The key to success is adhering to your target.')

