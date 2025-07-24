import art
import random
import time

card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

def deal_a_card():
    """Returns a random card from the deck"""
    return random.choice(card_deck)

def count_score(cards):
    """Calculates hand score"""
    score = 0
    for card in cards:
        if card == 'A':
            score += 11
        elif card in ['J', 'Q', 'K']:
            score += 10
        else:
            score += int(card)
    ace_count = cards.count('A')
    while ace_count:
        if score <= 21:
            return score
        else:
            score -= 10
            ace_count -= 1
    return score

if __name__ == "__main__":

    while True:
        choice = input("Do you want to play a game of Blackjack? Type 'y' or'n': ")
        if choice == 'n':
            break
        
        dealer_cards = []
        player_cards = []
        dealer_score = 0
        player_score = 0
        player_blackjack = False
        dealer_blackjack = False
        player_busted = False
        dealer_busted = False

        # Intro
        print('\n' * 25)
        print('#' * 80)
        print(art.blackjack)
        print('#' * 80)
        print('\n')
        
        # Deal Cards
        for _ in range(2):
            player_cards.append(deal_a_card())
            dealer_cards.append(deal_a_card())
        
        player_score = count_score(player_cards)
                       
        print(f"Your cards: {player_cards}, Current Score: {player_score}")
        print(f"Dealer cards: [Hidden, {dealer_cards[1]}]")
        
        # Players Turn
        if player_score == 21:
            player_blackjack = True
        while not player_blackjack:
            choice = input("Do you want to hit or stand? Type 'h' or 's': ")
            if choice == 'h':
                player_cards.append(deal_a_card())
                player_score = count_score(player_cards)
                print(f"Your cards: {player_cards}, Current Score: {player_score}")
                print(f"Dealer's cards: [Hidden, {dealer_cards[1]}]")
            elif choice == 's':
                break
            if player_score > 21:
                player_busted = True
                break

        # Dealers Turn
        dealer_score = count_score(dealer_cards)
        if dealer_score == 21:
            dealer_blackjack = true
        while not player_busted and not player_blackjack:
            print(f"Dealer's cards: {dealer_cards}, Current Score: {dealer_score}")
            if dealer_score <= 16:
                print("The dealer must hit!")
                dealer_cards.append(deal_a_card())
                dealer_score = count_score(dealer_cards)
            else:
                print("The dealer must stay!")
                break
            time.sleep(1)
            if dealer_score > 21:
                dealer_busted = True
                break

        # Game Result
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        if player_blackjack and not dealer_blackjack:
            print("Blackjack, you win!")
        elif player_busted:
            print("You went over. You lose!")
        elif dealer_busted:
            print("Dealer went over. You win!")
        elif player_score == dealer_score:
            print("Draw!")
        elif player_score < dealer_score:
            print("You lose!")
        else:
            print("You win!")

                
            
