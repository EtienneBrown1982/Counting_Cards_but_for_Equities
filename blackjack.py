
# Define card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Initialize the deck with four sets of 52 cards
deck = list(card_values.keys()) * 4

def simulate_blackjack():
    player_hand = []
    dealer_hand = []

    # Shuffle the deck
    random.shuffle(deck)

    # Deal two initial cards to the player and the dealer
    player_hand.extend([deck.pop(), deck.pop()])
    dealer_hand.extend([deck.pop(), deck.pop()])

    while sum(card_values[card] for card in player_hand) < 21:
        print(f"Player's hand: {', '.join(player_hand)}")

        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
        elif action == 'stand':
            break

    while sum(card_values[card] for card in dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    print(f"Player's hand: {', '.join(player_hand)}")
    print(f"Dealer's hand: {', '.join(dealer_hand)}")

    player_sum = sum(card_values[card] for card in player_hand)
    dealer_sum = sum(card_values[card] for card in dealer_hand)

    if player_sum > 21:
        return -1
    elif dealer_sum > 21 or player_sum > dealer_sum:
        return 1
    elif player_sum == dealer_sum:
        return 0
    else:
        return -1

def main():
    rounds = 1000
    win_count = 0
    for _ in range(rounds):
        result = simulate_blackjack()
        if result == 1:
            win_count += 1

    win_percentage = (win_count / rounds) * 100
    print(f"Win percentage over {rounds} rounds: {win_percentage:.2f}%")

if __name__ == "__main__":
    main()

