class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_cars_info(self):
        return f"{self.rank} of {self.suit}"


    def __repr__(self):
        return self.get_cars_info()

    
# Example usage:
heart4 = Card("heart", 4)
print(heart4.suit)  # Output: heart
print(heart4.rank)  # Output: 4
print(heart4.get_cars_info())  # Output: 4 of heart
print(heart4)  # Output: 4 of heart