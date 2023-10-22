import pandas as pd
import numpy
import json
import pathlib as Path
from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockBarsRequest
from alpaca.data.historical import StockHistoricalDataClient # Create stock historical data client
client = StockHistoricalDataClient(
        "PKM8F6A2IOLKO0SL5AA1", 
        "CfRu550DgykSbbnvaMWlb8apxyKSj11dEXmGWvST"
    )
tickers = ["QD"]
request_params = StockBarsRequest(
                            symbol_or_symbols=tickers,
                            timeframe=TimeFrame.Day,
                            start = pd.Timestamp("2023-10-01", tz="America/New_York"),
                            end = pd.Timestamp("2023-10-19", tz="America/New_York")
                    )
bars = client.get_stock_bars(request_params)
bars_df = bars.df
bars_df = bars_df.reset_index()
    # Creating the dataframe from class
    # Empty dataframe
final_dataframe = pd.DataFrame()
    # Grab the close of each ticker and set it to a column in the new dataframe
for ticker in tickers:
        #print("Ticker:", ticker, "Done")
        #display(bars_df[bars_df['symbol'] == ticker]['close'].head())
        #print(bars_df[bars_df['symbol'] == ticker]['close'].shape)
        final_dataframe[ticker] = pd.DataFrame(bars_df[bars_df['symbol'] == ticker]).reset_index()['close']
    # Grab the index from the old dataframe and set it to the new
final_dataframe.index = pd.to_datetime(bars_df[bars_df['symbol'] == 'QD']['timestamp']).dt.date
display(final_dataframe.head())
final_dataframe.plot()

def decide_buy_sell_hold(dataframe, threshold):
    # Calculate the number of days the closing price is above the threshold
    days_above_threshold = (dataframe['QD'] > threshold).sum()
    
    # Make a decision based on the number of days
    if days_above_threshold >= 5:
        return "buy"
    elif days_above_threshold <= 2:
        return "sell"
    else:
        return "hold"

# Example usage
threshold = 13  # Your chosen threshold
decision = decide_buy_sell_hold(final_dataframe, threshold)
print(f"Decision: {decision}")

# Calculate percentage change in stock price over the specified time frame (e.g., 13 days)
closing_price = final_dataframe['QD']  # Replace 'META' with your stock symbol
percentage_change = (closing_price / closing_price.shift(13) - 1) * 100

# Define threshold values
buy_threshold = 5  # Example: Buy if the stock has increased by more than 5%
sell_threshold = -5  # Example: Sell if the stock has decreased by more than 5%

# Decision logic
if percentage_change > buy_threshold:
    decision = "Buy"
elif percentage_change < sell_threshold:
    decision = "Sell"
else:
    decision = "Hold"

print(f"Decision: {decision}")




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
