from random import randint
from time import sleep
from os import system 

# const
ATTEMPTS = 8


def print_game(checks, price, wallet, wagered):
    system("clear")
    print("\n===== |BET| =====\n")
    print(f"\nWallet = {wallet}")
    print(f"\nRound price = {price}")
    print(f"\nMoney wagered = {wagered}\n")

    underscores = ATTEMPTS - checks
    counter = 1

    for _ in range(0, checks):
        print(f" |X{counter}| ", end="")
        counter = counter * 2
    for _ in range(0, underscores):
        print(" | | ", end="")


def game(round_price, wallet):
    counter = 1 
    wagered = 0

    for checks in range(1, ATTEMPTS + 1):
        wallet -= round_price
        wagered += round_price
        way = randint(0, 2)
        
        if way >= 1:
            print_game(checks, round_price, wallet, wagered) 
            back = input("\n\ncontinue? [y/n] > ")
            if back == "n":
                break
            counter = counter * 2
        else:
            print_game(checks, round_price, wallet, wagered) 
            print("\n\nYou lost...")
            counter = 0
            sleep(1.4) 
            break 

    final_price = round_price * counter 
    wallet += final_price 
    #return final_price
    return wallet


def main():
    wallet = 100
    print_game(0, 0, wallet, 0)
    continue_game = "y"

    while continue_game == "y":

        round_price = int(input("\n\nHow much each round? $ "))

        if round_price * 8 > wallet:
            print("\n\nYou don't have enough money...")
            continue 
        
        #wallet -= round_price 
        # run game
        game_money = game(round_price, wallet)
        #wallet += game_money 
        wallet = game_money

        print_game(0, 0, wallet, 0)
        
        continue_game = input("\n\ncontinue? [y/n] > ")
        
    print(f"\n\nBye! Wallet = {wallet}")
    sleep(1)


if __name__ == "__main__":
    main()
