import datetime
def gettime():
    return datetime.datetime.now()
while True:
    user_input=input('you want to log or retrieve the data (press l/r) : ')
    if user_input=='l'or user_input=='r':
        break
    print('you input wrong!, try again please')
if user_input=='l':
    print('ok you want to edit data\n')
    print('press 1 for bhartu : \npress 2 for abhinav : \npress 3 for anshiv :')
    press = int(input('enter input here : '))

    def user_select(name):
        while True:
            print(f'you choose for {name} \npress 1 for diet :\npress 2 for exercise :\npress 3 for back :')
            press = int(input('enter input here : '))
            if press ==1:
                choice = True
                while choice:
                        print(f'you press {press} for diet ')
                        with open(f'{name}_diet.txt','a') as f:
                            diet=input(f'{name} diet plan : \n ')
                            f.write(f'{str(gettime())}: {diet}\n')
                        a=input('press b for back\npress e for edit again\nenter here : ')
                        if a == 'b':
                            break
                        else:
                            continue
            elif press==3:
                break                
            else:
                choice = True
                while choice:
                        print(f'you press {press} for exercise ')
                        with open(f'{name}_exercise.txt','a') as f:
                            exercise=input(f'{name} exercise plan : \n ')
                            f.write(f'{str(gettime())}: {exercise}\n')
                        a=input('press b for back\npress e for edit again\nenter here : ')
                        if a == 'b':
                            break
                        else:
                            continue
    if press==1:
        n = 'bhartu'
    elif press==2:
        n= 'abhinav'
    else:
        n='anshiv'
    user_select(n)
else:
    print('ok you want to edit data\n')
    print('press 1 for bhartu : \npress 2 for abhinav : \npress 3 for anshiv :')
    press = int(input('enter input here : '))

    def user_select_retrieve(name):
            print(f'you choose for {name} \npress 1 for diet :\npress 2 for exercise :')
            press = int(input('enter input here : '))
            if press ==1:
                print(f'you press {press} for diet ')
                with open(f'{name}_diet.txt','r') as f:
                    print(f.read())
            else:
                print(f'you press {press} for exercises ')
                with open(f'{name}_exercises.txt','r') as f:
                    print(f.read())
    if press==1:
        n = 'bhartu'
    elif press==2:
        n= 'abhinav'
    else:
        n='anshiv'
    user_select_retrieve(n)               
