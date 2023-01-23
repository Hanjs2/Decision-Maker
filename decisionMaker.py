import random
# # list of fast food options

# getActive = ['Running','Biking','Climbing','Dancing','Swimming','Coding','Reading']

# funDone = random.choice(optOne,optTwo)
should_cont=True
while should_cont:
    print('What are the two options to decide from?')
    all_ops=[]
    optOne= input('Enter option 1: ')
    optTwo= input('Enter option 2: ')
    next_ops=""
    for _ in range(2):
        all_ops.append(optOne)
        all_ops.append(optTwo)
        
    multi_ops=input("Do you want to add another choice? 'y' or 'n'")
    if multi_ops=='y':
        next_ops=input("What is the next option?: ")
        all_ops.append(next_ops)
        print(all_ops)
    def random_roll():
        funDone=random.choice(all_ops)
        print(f"Your result is {funDone}")
    
    random_roll()
    
    new_decision=input("Would you like to make another decision? 'yes' or 'no' ").lower()
    if new_decision=='no':
        should_cont==False
        print("Have a great day")
        break
    



# print(funDone)

# if funDone == 'Running':
#     print('Lets get started')
# elif funDone == 'Climbing':
#     print('Dont forget your shoes')
# elif funDone == 'Coding':
#     print('Which coffee shop should we go to then')
# elif funDone == 'Dancing':
#     print('Time to get funky')
# elif funDone == 'Reading':
#     print('Wow time to feed the brain')
# elif funDone == 'Biking':
#     print('Feel the speed')
# else:
#     print('Maybe just stay in')




# # Section to decide what mood I am in
# mood = input('What mood are you in:')
# if funDone == 'Reading':
#     print('I am in a ' + mood + ' mood') 
# elif funDone == 'Coding':
#     print('I feel' + mood + ' enough to code')
# else:
#     print('I am in a ' + mood + ' mood today!')




