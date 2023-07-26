from  slot_machine import *   
def main():
    balance=deposit()
    while True:
        spin=input("Press enter to play or n to  quit? (y/n): ")
        if spin == "n":
            break
        balance+=play_game(balance) 
        print("Your balance is {}".format(balance))
if __name__== "__main__":
    main()         
