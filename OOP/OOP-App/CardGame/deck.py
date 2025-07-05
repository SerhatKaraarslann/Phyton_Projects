import card

class Deck:
    def __init__(self):
        self.cards = []
        suits = {"heart", "diamond", "spade", "club"}
        ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"}
        for suit in suits:
            for rank in ranks:
               print(f"Creating card: {suit} {rank} \n")
               self.cards.append(card.Card(suit, rank))
               
    def shuffle_deck(self):
        import random
        """Shuffle the deck of cards."""
        random.shuffle(self.cards)

    def deal_card(self):
        """Deal a card from the deck."""
        if self.cards:
            return self.cards.pop()
        else:
            return None
        
    def card_count(self):
        """Return the number of cards in the deck."""
        return len(self.cards)
    
    def add_card(self, count):
        """Add a specified number of cards to the deck."""
        if count < 1:
            raise ValueError("Count must be at least 1.")
        if not self.cards:
            self._create_deck()
        if count > len(self.cards):
            raise ValueError("Not enough cards in the deck to add.")
        # Assuming we want to add new cards to the deck

        import random
        from CardGame.card import Card
        for _ in range(count):
            self.cards.append(card.Card(random.choice(self.suits), random.choice(self.ranks)))

    def distribute_cards(self, players, cards_per_player):
        """Distribute cards to players."""
        if cards_per_player * len(players) > len(self.cards):
            raise ValueError("Not enough cards in the deck to distribute.")
        
        hands = {player: [] for player in players}
        for _ in range(cards_per_player):
            for player in players:
                hands[player].append(self.deal_card())
        return hands
    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
    