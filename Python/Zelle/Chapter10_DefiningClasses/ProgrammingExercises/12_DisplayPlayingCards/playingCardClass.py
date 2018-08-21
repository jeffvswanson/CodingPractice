# playingCardClass.py
"""A module to represent playing cards as a class."""

class playingCard:
    """A playing card object. A card's rank is between 1 and 13 indicating
    the ranks Ace-King, and suit is a single character "d", "c", "h", or
    "s" indicating the suit (diamonds, clubs, hearts, or spades)."""

    def __init__(self, rank, suit):
        self.rank = int(rank)
        self.suit = str(suit)

    def getRank(self):
        """Returns the rank of the card."""
        return self.rank

    def getSuit(self):
        """Returns the suit of the card."""
        return self.suit

    def BJValue(self):
        """Returns the BlackJack value of a card. Aces count as one, face
    cards count as 10."""
        if self.rank > 10:
            self.rank = 10
        return self.rank
            

    def __str__(self):
        """Returns a string that names the card. For example, "Ace of Spades",
    c = Card(1,"s")
    print c
    Ace of Spades"""
        ranks = ["Ace","Two","Three","Four","Five","Six","Seven","Eight", \
                 "Nine","Ten","Jack","Queen","King"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        cardRank = ranks[self.rank - 1]
        for i in suits:
            if i[0] == self.suit.upper():
                cardSuit = i
        cardName = "{0} of {1}".format(cardRank, cardSuit)
        return cardName
        
    def draw(self, win, center):
        """Draws a playing card."""
