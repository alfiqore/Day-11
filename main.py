import random
from replit import clear
from art import logo


def count(total_card):
    total = 0
    for card in total_card:
        total += int(card)
    return total


def winner(player, dealer):
    if count(player) > count(dealer):
        print("Player win")
    elif count(player) == count(dealer):
        print("Draw")
    else:
        print("Dealer win")


def ex(who):
    if 11 in who and count(who) > 21:
        index = who.index(11)
        who[index] = 1
    return who


def add_card(who):
    who.append(card[random.randint(0, 12)])
    who = ex(who)
    return who


card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play():
    print(logo)
    player = []
    dealer = []

    player.append(card[random.randint(0, 12)])
    player.append(card[random.randint(0, 12)])
    dealer.append(card[random.randint(0, 12)])

    print(f"Player : {player} ; {count(player)}")
    print(f"Dealer : {dealer} ; {count(dealer)}")
    keep_playing = True
    if count(player) == 21:
        while count(dealer) < 17:
            add_card(dealer)
        if count(dealer) > 21:
            print(f"Dealer : {dealer} ; {count(dealer)}")
            print("Dealer Bust")
            if input("do you want to play again : y/n ") == 'y':
                play()
            else:
                exit()
        if count(dealer) > 17:
            print(f"Player : {player} ; {count(player)}")
            print(f"Dealer : {dealer} ; {count(dealer)}")
            winner(player, dealer)
            if input("do you want to play again : y/n ") == 'y':
                play()
            else:
                exit()
    else:
        while keep_playing == True:
            decision = (input("Hit or stand? H/S ")).lower()

            if decision == 'h':
                add_card(player)
                print(f"Player : {player} ; {count(player)}")
                if count(player) > 21:
                    print("You Bust")
                    keep_playing = False
            elif decision == 's':
                while count(dealer) < 17:
                    add_card(dealer)
                if count(dealer) > 21:
                    print(f"\nDealer : {dealer} ; {count(dealer)}")
                    print("Dealer Bust")
                    keep_playing = False
                elif count(dealer) > 17:
                    print(f"\nPlayer : {player} ; {count(player)}")
                    print(f"Dealer : {dealer} ; {count(dealer)}")
                    winner(player, dealer)
                    keep_playing = False
        if input("do you want to play again : y/n ") == 'y':
            play()
        else:
            exit()


play()
