import random

def play():
   choices = ['r', 'p', 's']
   user = None

#def play():
   # choices = ['r', 'p', 's']

   keep_playing = "true"
   while keep_playing == "true":

        computer = random.choice(choices)

        user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
        
        if computer == user:
            print("It is a tie")

        elif user == 'r' and  computer == 's':
             print ("Thumbs up! You won")

        elif user == 'p'and  computer == 'r':
            print ("Thumbs up! You won")

        elif user == 's' and computer == 'p':
            print ("Thumbs up! You won")
        
        elif user == 'p'and computer == 's':
             print ("You lost")

        elif user == 'r' and computer == 'p':
             print ("You lost")

        elif user == 's' and computer == 'r':
             print ("You lost")


        
    

        if user not in choices:
          print("Invalid input. Try again")
play()



