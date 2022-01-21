import random
import time

def your_choise(options):
    while True:
        your_guess = input("Make your guess: ").upper()
        if your_guess in options:
            break
        else:
            print("Please introduce a valid option")
            continue
    return your_guess
def machine_choise(options):
    rand = random.randint(0, 2)
    mach_guess = options[rand]
    return mach_guess

def conditions(mach_guess, your_guess):
    if mach_guess == your_guess:
        return "deuce"
    else:
        if (mach_guess == "PAPER" and your_guess == "ROCK" or 
        mach_guess == "ROCK" and your_guess == "SCISSOR" or
        mach_guess == "SCISSOR" and your_guess == "PAPER"):
            print("My guess: ", mach_guess, " Your guess: ", your_guess)
            return "lost"
        else:
            print("My guess: ", mach_guess, " Your guess: ", your_guess)    
            return "won"

def countdown():
    num_of_secs = 3
    while num_of_secs >= 1:
        print(num_of_secs)
        num_of_secs -= 1
        time.sleep(1)

def main():
    print("Try to beat me, choose rock, paper or scisor")
    options = ("ROCK", "PAPER", "SCISSOR")
    
    tries = 0
    while True:
        tries += 1
        your_guess = your_choise(options)
        mach_guess = machine_choise(options)
        countdown()
        results = conditions(mach_guess, your_guess)
        if results == "won":
            print("CONGRATULATIONS!")
            break
        elif results == "deuce":
            print("Deuce, try again")
            continue
        else:
            print("You lost, try again")
            continue
    print("You won in", tries, "times")    

if __name__ == "__main__":
    main()