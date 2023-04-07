import random
inventory = []

# think about having a time variable

def isPresent(data):
    if data != '':
        return True
    else:
        print('*************')
        print('You have not written anything')
        print('**************')
        return False

def office():
    choice = ''
    while True:
        print('Table in front of you, a set of shelves to the left and a book case to the right and the hall behind you')
        print('Where do you want to look?')
        print('Options: Shelves/Desk/Bookcase/Leave')
        choice = input()
        if isPresent(choice):
            if choice.upper() in ['SHELVES','DESK','BOOKCASE','LEAVE']:
                break
    if choice[0].capitalize() == 'S':
        print('You walk up to the shelves')
        print("You walk over to you dads office shelves, there isn't a lot of there apart from family photos and no real sign of a front door key")
        print('With that you walk over to the middle of the office again')
        office()
    elif choice[0].capitalize() =='D':
        print('You walk up to you dads desk')
        print("You sit down at your dads old desk, on the left side is a shopping list that says you're out of custard creams, on the right side is a photo of you and you sister jess")
        print('There is nothing else on his desk apart from his pencils, pens a paper tray and a desk light')
        print('You stand up and go back to the center of his office')
        office()
    elif choice[0].capitalize() =='B':
        print('You walk up to the boockase')
        print('You walk up to the bookcase, running your fingers along the books')
        print('Your hand clasps the copy of 1984, your dads favourte book')
        print('When you take the book you see the corner of a safe, you push all the books aside and you are left standing looking at a safe that needs a 4 digit code')
        if 'Safe Code' in inventory:
            print('You pull out the piece of paper where you noted the code from your mums computer and type it in')
            print('The safe door opens, inside is some old family photos, an envolope of cash and a note')
            print('You pick up the note and read it "I took the key of here because I cannot find the spare one from the kitech, J"')
            print()
            print('You put the node down and go back to the center of the room')
            office()
        else:
            print("It doesn't look like you have the code, you know your parents were forgetful so they had to have left a note somewhere")
            print('So you get up from the bookcase and move back into the middle of the room ')
            office()           
    else:
        hall()
                    
            
def diningTable():
    if 'Safe Code' in inventory:
        print('You already have the safe code, you do not need to look at your passowrd anymore')
    else:
        attempts = 0
        print('You pull one of the chairs out and site down at the table')
        print('At the center of the tabe, is your mums laptop, you open the lid and are met with a password box')
        while True:
            print('Please enter your password:') 
            password = input()
            if password == 'Rose':
                print('You are logged into your mums computer, you look through the different files that are open')
                print('You find an email across your computer that says he has changed the password to the safe, you write this down on paper and put it in your pocket')
                inventory.append('Safe Code')
                print('You shut the laptop and get up from the table')
                break
            else:
                attempts += 1

            if attempts == 2:
                print('Here is a hint, it is 4 letters long')
            elif attempts == 3 or attempts == 5:
                while True:
                    print('You are locked from trying another password until you pass this math question:')
                    #create question
                    numOne = random.randint(0,10)
                    numTwo = random.randint(0,10)
                    print(f'Question: {numOne}x{numTwo}')
                    userAnswer = input('Please input your answer here:')
                    if isPresent(userAnswer):
                        if userAnswer == str(numTwo*numOne):
                            break
                        else:
                            print('Your answer is incorrect, try another question')
            elif attempts == 6:
                print('Here is another hint, it is my favourte flower')
            elif attempts == 8:
                print('You have had too many attempts please try again later')
                print('You get up from the table and stand in the middle of the desk')
                print('You wait a few moments pass while you stand in the centre of the room')
                break
    diningRoom()

                
             
        

def diningRoom():
    choice = ''
    while True:
        print('The room is cold, with a window to your right and the table infront of you')
        print('Where do you want to look?')
        print('Options:Table/Window/Leave')
        choice = input()
        if isPresent(choice):
            if choice.upper() in ['TABLE','WINDOW','LEAVE']:
                break
            else:
                print('*************')
                print('Please write one of the options given to you')
                print('**************')
    if choice[0].capitalize() == 'W':
        print('You walk up to the window and peer through, to your old front garden. The rose bush you mum loved, fron and center. But something about it seemed off')
        print('You step away and return to the middle of the room')
        diningRoom()
    elif choice[0].capitalize() == 'L':
        hall()
    else:
        diningTable()
    

def kitchen():
    choice = ''
    while True:
        print('You are stood in the middle of your kitchen, the fridge is to your left and the cupbards are on your right')
        print('Where do you want to look?')
        print("Options:Left/Forwards/Right/Backwards")
        choice = input()
        if isPresent(choice):
            if choice.upper() in ['LEFT','RIGHT','BACKWARDS']:
                break
            else:
                print('*************')
                print('Please write one of the options given to you')
                print('**************')
    if choice[0].capitalize() == 'L':
        print('You open the fridge and see nothing but milk')
        print('You shut the fridge and go back to the middle of the kitchen')
        kitchen()
    elif choice[0].capitalize() =='R':
        print('You go to the cupbards')
        snackChoice = ''
        while True:
            print('What should you look for?')
            print('Options:Biscuits/Apple/Choclate')
            snackChoice = input()
            if isPresent(snackChoice):
                if snackChoice.upper() in ['BISCUITS','APPLE','CHOCLATE']:
                    break
        if snackChoice[0].capitalize() == 'B':
            if 'key' not in inventory:
                print('You go to the cupbard where the biscuits are')
                print('There is no packet, instead there seems to be a key')
                print('You pick it up and realise it is the key for the front door')
                print('You get up and go back to the middle of the kitchen')
                inventory.append('key')
                kitchen()
            else:
                print('You go to look for biscuits but there is nothing in the cupbard')
                print('You get up and go back to the middle of the kitchen')
                kitchen()
        elif snackChoice[0].capitalize() == 'A':
            print('You look in the fruit bowl, there is an apple inside, you pick it up and put it in your pocket')
            inventory.append('apple')
            print('You get up and go back to the middle of the kitchen')
            kitchen()
        else:
            print('You look in the draw where the chocolate usually is but there is none')
            print('You get up and go back to the middle of the kitchen')
            kitchen()
        
    else:
        hall()
    


    

def hall():
    direction = ''
    print('You return to the hall.')
    while True:
        print('To your left you have you front door, infront is you dads old office, to your right is the kitchen and behind you is the dining room')
        print('Which way do you want to go')
        print('Options: Forwards/Backwards/Left/Right')
        direction = input()
        if isPresent(direction):
            if direction.upper() in ['FORWARDS','BACKWARDS','LEFT','RIGHT']:
                break
            else:
                print('*************')
                print('Please write one of the options given to you')
                print('**************')
                
    if direction[0].capitalize() == 'F':
        print('You walk into your dads old office')
        office()
                    
    #Backwards
    elif direction[0].capitalize() == 'B':
        print('You walk into your old family dining room')
        diningRoom()
                    
    #Left
    elif direction[0].capitalize() == 'L':
        if 'key' in inventory:
            print('You pull the key out your bag, slot it in the door and push on the handle to escape the house')
            print('You left the house with:')
            for i in inventory:
                print(i)
            print('You then feel the light hit you face, as you realise the whole sthing was a dream')


        else:
            print('You go up to the door and try to turn the handle, you need a key!')
            print('Dad used to keep a key in his office')
            hall()
    else:
        print("You walk into the kitchen")
        kitchen()

 

                
        

def main():
    direction = ''
    while True:
        print('You find yourself in your childhood home, stood in the hallway')
        print('To your left you have you front door, infront is you dads old office, to your right is the kitchen and behind you is the dining room')
        print('You have to get out the house, which way do you want to go first?')
        print('Options: Forwards/Backwards/Left/Right')
        direction = input()
        if isPresent(direction):
            if direction.upper() in ['FORWARDS','BACKWARDS','LEFT','RIGHT']:
                break
            else:
                print('*************')
                print('Please write one of the options given to you')
                print('**************')
    #Forwards
    if direction[0].capitalize() == 'F':
        print('You walk into your dads old office')
        office()
        #Backwards
    elif direction[0].capitalize() == 'B':
        print('You walk into the old dining room')
        diningRoom()
    #Left
    elif direction[0].capitalize() == 'L':
        print('You go up to the door and try to turn the handle, you need a key!')
        print('Dad used to keep a key in his office')
        hall()
    #Right
    else: 
        print('You walk into the kitchen')
        kitchen()
        
main()