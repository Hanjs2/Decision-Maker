import random



should_cont=True
while should_cont:
    add_choice=True
    print('What are the two options to decide from?')
    all_ops=[]
    optOne= input('Enter option 1: ')
    optTwo= input('Enter option 2: ')
    next_ops=""
    for _ in range(2):
        all_ops.append(optOne)
        print(all_ops)
        all_ops.append(optTwo)
        print(all_ops)
    while add_choice:
        multi_ops=input("Do you want to add another choice? 'y' or 'n': ")
        if multi_ops=='y':
            next_ops=input("What is the next option?: ")
            all_ops.append(next_ops)
        else:
            add_choice==False
            break
            
        
# Find way to repeat code above to recieve multiple options for a decision ma
        
    def random_roll():
        funDone=random.choice(all_ops)
        print(f"Your result is {funDone}")
    print(all_ops)
    
    random_roll()
    
    new_decision=input("Would you like to make another decision? 'yes' or 'no' ").lower()
    if new_decision=='no':
        should_cont==False
        print("Have a great day")
        break
    
    
        





