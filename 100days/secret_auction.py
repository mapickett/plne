
gavel = """
            ___________
            \         /
            )_______(
            |"""""""|_.-._,.---------.,_.-._
            |       | | |               | | ''-.
            |       |_| |_             _| |_..-'
            |_______| '-' `'---------'` '-'
            )"""""""(
            /_________\\
            `'-------'`
        .-------------.
        /_______________\\"""

def get_bid():
    while True:
        bid = input("What's your bid?: $" )
        try:
            int(bid)
            return(int(bid))
        except ValueError:
            print("Invalid choice.")


if __name__ == "__main__":
    bidders = {}

    print(gavel)              
    print("Welcome to the secret auction program.")

    while True:
        username = input("What is your name?: ")
        bid  = get_bid()
        bidders[username] = bid
        more_bidders = input ("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if more_bidders == 'no':
            break
        print("\n" * 25)
    
    # winning_name = 'nobody'
    # winning_bid = 0
    # for k in bidders:
    #     if bidders[k] > winning_bid:
    #         winning_name = k
    #         winning_bid = bidders[k]

    winner = max(bidders, key=bidders.get)

    print(f'The winner is {winner} with a bid of ${bidders[winner]}')