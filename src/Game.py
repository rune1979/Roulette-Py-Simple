import tkinter
import settings as s
import wheel
import Bin
import money as m
import time

#top = tkinter.Tk()
class Player:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = m.wallet(s.wallet_start)
        print("Hi " + name, "you have " + str(wallet) + " in your wallet!")


    def bet(self):
        bet_comb = int(input("What bet are you gonna make?: "))
        print("Your current holdings are: " + str(self.wallet.print_amount()))
        bet_ammount = int(input("How much are you gonna bet?: "))
        self.wallet.withdraw_amount(bet_ammount)
        return bet_comb, bet_ammount




        #print("Now your current holding is", str(self.wallet.print_amount()))
        #B = Tkinter.Button(top, text="Hello", command=helloCallBack)
        #top.mainloop()









if __name__ == "__main__":


    player_name = input("Player name: ")
    player = Player(player_name, s.wallet_start)
    time.sleep(3)
    Bin.b.printoutcomes()
    betting = "y"
    bets = []
    while betting == "y":
        bets.append(player.bet())
        betting = input("Do you want to make more bets? (y/n): ")

    print("Spinning has begun...")
    number = wheel.run_wheel()
    print("The wheel number was:", number, "!")
    print(bets)



