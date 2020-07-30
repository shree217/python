# guessing the number game
game = input("What game you wanna play either guess the number(G) or car (C): ").lower()
if game == 'g':
    print("Guess a number between 1-9 lets see your luck")
    secret_number =9
    guessing_count=0
    while guessing_count < 3:
        guess = int(input("guess a number: "))
        guessing_count = guessing_count+1
        if guess == secret_number:
            print("You won, congrats!!!")
            break
    else:
        print("you failed")
#car game
else:
    var = " "
    started = False
    stopped = True
    while var != "quit":
        var = input("> ").lower()
        if var == "help" :
            print("Start - to start the car")
            print("Stop - to stop the car")
            print("Quit - to exit from the game")
        elif var == "start":
            if started:
                print("car already started!!")
            else:
                started=True
                print("the car has started.....")
        elif var == "stop":
            if not stopped:
                print("car has already stopped")
            else:
                stopped = False
                print("the car has stoped.")
        elif var == "quit":
            break
        else:
            print("I don't understand what you are saying.")




