class Library:
    def __init__(self,listofbook,libraryname):
        self.listofbook=listofbook
        self.libraryname=libraryname
    
    def displaybooks(self):
        print('\n\nHere is the list of books\n')
        j=0
        for i in self.listofbook:
            j+=1
            print(j,':',i)

    def lendbooks(self,lendbook):
        if lendbook in self.listofbook:
            global store
            store=lendbook
            print('successfully book lend from the library')
            return self.listofbook.remove(lendbook)
        return print('No book found !')

    def addbooks(self,newbook):
        if newbook in self.listofbook:
            print('Already book in library')
        elif newbook==store:
            print('Already book in library,but lend by someone')
        else:
            print('successfully book added into library')
            return self.listofbook.append(newbook)
    
    def returnbooks(self,returnbook):
        if returnbook in self.listofbook:
            print('book is already in liberary')
        elif returnbook==store:
            print('book successfully returned')
            return self.listofbook.append(returnbook)
        else:
            print('you input wrong')
    def runfunction(self):
        while True:
            print(f'\n\nWelcome to the {libraryname} library\n')
            user_input=int(input('Press 1 For List Of Books :\nPress 2 For Lend the Book :\nPress 3 For Add New Book :\nPress 4 For Return Book :\nPress 5 For exit :\nInput here :  '))
            if user_input==1:
                while True:
                    self.displaybooks()
                    user_input2=input('\nenter back for main menu : ')
                    if user_input2=='back':
                        break
                    else:
                        print('please type back for main menu,you input wrong')
            elif user_input==2:
                while True:
                    print('Here is the list of book which you want to lend \n')
                    self.displaybooks()
                    user_input2=input('enter the name of book that you want to lend : ')
                    self.lendbooks(user_input2)
                    user_input2=input('\nenter back for main menu : ')
                    if user_input2=='back':
                        break
                    else:
                        print('please type back for main menu,you input wrong')
            
            elif user_input==3:
                while True:
                    user_input2=input('enter the name of the book that you want to add : ')
                    self.addbooks(user_input2)
                    user_input2=input('\nenter back for main menu : ')
                    if user_input2=='back':
                        break
                    else:
                        print('please type back for main menu,you input wrong')
            
            elif user_input==4:
                while True:
                    user_input2=input('enter the name of the book that you want to return : ')
                    self.returnbooks(user_input2)
                    user_input2=input('\nenter back for main menu : ')
                    if user_input2=='back':
                        break
                    else:
                        print('please type back for main menu,you input wrong')
            else:
                if user_input==5:
                    break
         
libraryname=input('enter the library name : ')
booklist=['book a','book b','book c','book d','book e','book f','book g']
l1=Library(booklist,libraryname)
l1.runfunction()

        