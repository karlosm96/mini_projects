import random

def ran_num(range):
    num_gen = random.randint(0, range)
    return num_gen

def main():
    range = input("Introduce a range number: ")

    while True:
        range = input("Introduce a range number: ")
        if range.isdigit():
            if range <= "1":
                print("Please, introduce a number greater than 1")
            else:
                range = int(range)
                break
        else:
            print("Please, introduce a number next time")

    num_generator = ran_num(range)
    attemps = 0

    while True:
        attemps += 1
        your_num = input("Make a guess: ")

        if your_num.isdigit():
            your_num = int(your_num)
        else:
            print("Please introduce a number next time")
            continue

        if num_generator == your_num:
            print("You got it!")
            break
        else:
            if num_generator < your_num:
                print("You are abrove the number")
            else:
                print("You are below the number")
                continue

    print("Number of attemps: ", attemps)

if __name__ == "__main__":
    main()
            
            
