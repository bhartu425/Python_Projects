import random
computer=['snake','water','gun']
rounds=0
total_point=0
while rounds<10:
    while True:
        print(f'\nRound {rounds+1}')
        print('press 1 for snake : \npress 2 for gun : \npress 3 for water : ')
        try:
            user_input=int(input('enter here : '))
            break
        except:
            print('opps you input wrong ! try again')

    com=random.choice(computer)
    print(f'your opponant choose : {com}\n')
    rounds=rounds+1
    
    #for snake
    if user_input==1 and com == 'snake':
        print('Round Draw ')
    elif user_input==1 and com=='gun':
        print(f'oops you loose {rounds} round')
    elif user_input==1 and com=='water':
        print(f'congratulation you win the {rounds} round')
        total_point=total_point+1
    #for gun
    elif user_input==2 and com=='gun':
        print('match draw')
    elif user_input==2 and com=='water':
        print(f'oops you loose {rounds} round')
    elif user_input==2 and com=='snake':
        print(f'congratulation you win the {rounds} round')
        total_point=total_point+1
    #for water
    elif user_input==3 and com=='water':
        print('match draw')
    elif user_input==3 and com=='snake':
        print(f'oops you loose {rounds} round')
    elif user_input==3 and com=='gun':
        print(f'congratulation you win the {rounds} round')
        total_point=total_point+1
    else:
        print('game finish!')
print(f'your total point is : {total_point}')