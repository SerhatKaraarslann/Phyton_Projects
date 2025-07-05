# Card Class

# An instance of Card class represents a card type in card game.
# Card class has two attributes: suit and rank. (heart, diamond, club, spade) and (2, 3, 4, ..., 10, J, Q, K, A)

#heart5 = Card("heart", 5)
#heart5.suit => "heart"

#a method to get the card information as a string
#heart5.get_card_info() => "5 of heart"

# Deck Class
# An instance of Deck class represents a deck of cards.

# We add a method to add 52 cards to the deck with list comprehension and for loop.
# A method to shuffle the deck using random.shuffle.
# A method to deal a card from the deck and return it.
#A method to check card count in the deck.
# Card distribution
# A method to distribute cards to players.
# pick a card from the deck and return it.


import deck as deck

if __name__ == "__main__":
    # Create a deck of cards
    my_deck = deck.Deck()
    
    # Print the deck
    print(my_deck)
    
    # Shuffle the deck
    my_deck.shuffle_deck()
    
    # Deal a card from the deck
    dealt_card = my_deck.deal_card()
    print(f"Dealt card: {dealt_card}")
    
    # Check the number of cards left in the deck
    print(f"Cards left in the deck: {my_deck.card_count()}")
    
    # Distribute cards to players
    players = ["Alice", "Bob"]
    hands = my_deck.distribute_cards(players, 5)
    
    for player, hand in hands.items():
        print(f"{player}'s hand: {hand}")