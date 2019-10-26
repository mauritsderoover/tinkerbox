from tkinter import *
#from PIL import Image, Tkimage

#Here I initialize my global variables

check1 = False #this keeps track of the first input 
check2 = False #this keeps track of the second input
player1 = ""
player2 = ""
names = []
player_amount = 0
index = 0
frames = []
entry1 = ""
frameindex = 0

#I also initialize the master screen so i can use it through all functions without passing it in
master = Tk()
master.geometry("500x500")
master.configure(bg="gray")
e1,e2,e3,e4 = StringVar(),StringVar(),StringVar(),StringVar()
entries = [e1,e2,e3,e4]

    
def main():

    picturelabel =  PhotoImage(file = 'landscape.png')
    piclabel = Label(master, image = picturelabel).place(relwidth=1,relheight=1)
    
   #☺ "C:\Users\mauri\Pictures\testgif.gif"
    startlabel = Label(master, text = "Do you want to start?", font = 50, bd = 5, bg = "#80c1ff").place(relx=0.15, rely = 0.2, relheight=0.2, relwidth=0.70)
    startbutton = Button(master, text = "Yes!", command = game_logic).place(relx= 0.15, rely = 0.40, relwidth=0.70, relheight=0.2)
    exitbutton = Button(master, text = "No, exit game!", command = master.destroy).place(relx = 0.15, rely = 0.6, relwidth=0.70, relheight=0.2)
    
    mainloop() 

#This starts the game
def game_logic():
    #ask how many players will play
    amount_players()

#this function asks how many players will play and jumpstarts asking for names
def amount_players():
    #ask how many players will play
    a = "In the white entry box you need the enter the amount of players!! "
    b = "Please enter the amount of players: " 
    request_input_screen(a,b, e1,check_amount,1)
    
def ask_name():
    global player_amount,index
    a = "In the white entry box you need to enter player name!! "
    b = "Please enter the name of player: " 
    player_amount = int(e1.get())
    n = player_amount
    print("This is ask nametest : ",player_amount)
    print("This is n : ",n)
    
    request_input_screen(a,b,e3,lambda : name_tracker(2),1)    
    request_input_screen(a,b,e2,lambda : name_tracker(1),1)
    
#this function tracks players names and jumpstarts next step
def name_tracker(i):
    global names
    destroy_screen()
    #entry1.delete(0,END)
    if i == 1: #since i create all of the frames at once, the frame is the last to go so i need ot junmpstart next function from here
        name = e2.get().strip()
        names.append(name)
        print("Let´s see if this works: ",names)
        #test_function()
    if i == 2:
        name = e3.get().strip()
        names.append(name)
        print("Let´s see if this also works: ",names)
        get_player_input()
        
#This is the function that takes care of all the 
def request_input_screen(a, b, c,function,d):
    global tests, entry1
    request, request1 = Frame(master,bg = 'black'), Frame(master, bg = '#80c1ff')
    tests = [request, request1]
    request.place(relwidth = 1, relheight = 1)
    request1.place(relwidth = 1, relheight = 0.4, rely = 0.6)
    
    #This label provides context to the request you´re making     
    Label(request, text = a).place(relwidth = 1, relheight = 0.2, rely = 0.2)
    
    #The label, Entry and Button Widgets to take in the input
    RELY = 0.5
    HEIGHT = 0.20
    Label(request1, text = b, font = 40).place(relwidth = 0.5, relheight = HEIGHT, rely = RELY)
    if d == 1:
        entry1 = Entry(request1, textvariable = c)
    else:
        entry1 = Entry(request1, textvariable = c, show = "*")
    entry1.place(relwidth = 0.25, relheight = HEIGHT, rely = RELY, relx = 0.5)
    Button(request1, text = "Enter", command = function).place(relwidth = 0.25, relheight = HEIGHT, rely = RELY, relx = 0.75)
    Button(request1, text = "Exit", command = destroy_screen).place(relwidth = 0.25, relheight = HEIGHT, rely = RELY+0.2, relx = 0.75)

    
#this is a     
def get_player_input():
    #for i in names:
     a = "Player {0} can go now!!! ".format(names[0])
     b = "Please enter your input in the white box!"
     request_input_screen(a,b,e1,lambda : check_playerinput(names[0]),0)
     a = "Player {0} can go now!!! ".format(names[1])
     b = "Please enter your input in the white box!"
     request_input_screen(a,b,e2,lambda : check_playerinput(names[1]),0)

#destroy a screen
def destroy_screen():
    #global tests
    new = tests
    for item in new:
        item.destroy()
        print("this has been executed")

#this function makes sure that amount input is correct
#if it´s correct then it start´s the ask name functions
def check_amount():
    n = e1.get()
    if n.isdigit() == True:
        destroy_screen()
        ask_name()
    else:
        c = "It has to be a number you stupid!! "
        errormessage(c)
        #entry1.delete(0,END)
        
#make sure that the provided input is correct
#and if both are entered and correct then jump start comparing
def check_playerinput(a):
    #initialize  global variables
    global check1,check2,player1,player2
    #initialize local variables
    accepted_input = ["scissors", "rock", "paper"]
    
    if a == names[0]:
        userinput = e1.get().strip().lower()
        print("do i get here A ")
        print("this is a userinput in case A : ",userinput)
    else:
        userinput = e2.get().strip().lower()
        print("do i get here B")
        print("this is userinput in case B : ",userinput)

    #clear the input in the inputbox
    #entry1.delete(0,END)
    
    #checks is the user input is correct
    if userinput in accepted_input:
        #destroy the input screen
        destroy_screen()
        if a == names[0]:
            player1 = userinput
            check1 = True
            print(player1)
            print(check1,check2)
        else:
            player2 = userinput
            check2 = True
            print(player2)
            print(check1,check2)
        #if both check1 and check2 are True then it starts comparing
        #after that all values are reset to be able to keep the game running
        if check1 == True and check2 == True:
            destroy_screen()
            compare(player1,player2)
            reset_values()
    else:
        errormessage("The input was wrong, please close this and try again! ")


#this function produces errormessages
def errormessage(c):
    new2 = Frame(master, bg = '#80c1ff')
    new2.place(relwidth = 1, relheight = 1)
    errormessage = StringVar()
    errormessage.set(c)
    Message(new2, textvariable = errormessage).place(relwidth = 0.8, relheight = 0.3, rely = 0.35)
    Button(new2, text = "OK", command = new2.destroy, bd = 10, bg = "green").place(relwidth = 0.2, relheight = 0.3, rely = 0.35, relx = 0.8)

def compare(a,b):
    #initialize the two inputs
    inp1 = a
    inp2 = b

    #the three inputs
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    
    #the different possible outcomes elements
        
    sit1 = "Sciccors beats paper! "
    sit2 = "Rock beats Sciccors! "
    sit3 = "Paper beats Rock! "
    pl1 = "Player 1 wins"
    pl2 = "Player 2 wins"
    pl0 = "It is a DRAW !!"
    # some if functions to check who won     
    if inp1 == scissors and inp2 == paper:
        print("{0} , {1}".format(sit1,pl1))
        response(sit1,pl1)
    elif inp1 == scissors and inp2 == rock:
        print("{0} , {1}".format(sit2,pl2))
        response(sit2,pl2)
    elif inp1 == rock and inp2 == paper:
        print("{0} , {1}".format(sit3,pl2))
        response(sit3,pl2)
    elif inp1 == rock and inp2 == scissors:
        response(sit2,pl1)
        print("{0} , {1}".format(sit2,pl1))
    elif inp1 == paper and inp2 == scissors:
        response(sit1,pl2)
        print("{0} , {1}".format(sit1,pl2))
    elif inp1 == paper and inp2 == rock:
        response(sit3,pl1)
        print("{0} , {1}".format(sit3,pl1))
    elif inp1 == inp2:
        response(pl0,"")

#this function resets all global values
def reset_values():
    #initialize player and check values values as global values so they can be adapted throughout the programm
    global player1, player2,check1,check2
    
    player1 = ""
    player2 = ""
    check1 = False
    check2 = False

#response function
def response(a,b):
    resp = a + b
    errormessage(resp) #this not actually an error message but like this i have to write less code

if __name__ == "__main__":
    main()
