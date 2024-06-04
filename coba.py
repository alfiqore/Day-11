import random
from replit import clear  # Pastikan ini benar dan diimpor dengan benar
from art import logo


def count(total_card):
    total = 0
    for card in total_card:
        total += card
    return total


def winner(player, dealer):
    if count(player) > 21:
        print("Player busts. Dealer wins.")
    elif count(dealer) > 21:
        print("Dealer busts. Player wins.")
    elif count(player) > count(dealer):
        print("Player wins.")
    elif count(player) == count(dealer):
        print("Draw.")
    else:
        print("Dealer wins.")


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

    player = ex(player)  # Update player hand to handle initial Ace
    dealer = ex(dealer)  # Update dealer hand to handle initial Ace

    print(f"Player : {player} ; {count(player)}")
    print(f"Dealer : {dealer} ; {count(dealer)}")

    keep_playing = True
    while keep_playing:
        clear()
        if count(player) == 21:
            print("Blackjack! Player wins.")
            keep_playing = False
            continue

        decision = (input("Hit or stand? H/S ")).lower()

        if decision == 'h':
            add_card(player)
            print(f"Player : {player} ; {count(player)}")
            if count(player) > 21:
                print("You bust.")
                keep_playing = False
        elif decision == 's':
            while count(dealer) < 17:
                add_card(dealer)
            print(f"Player : {player} ; {count(player)}")
            print(f"Dealer : {dealer} ; {count(dealer)}")
            winner(player, dealer)
            keep_playing = False

    if input("Do you want to play again? y/n : ").lower() == 'y':
        clear()
        play()
    else:
        exit()


play()
