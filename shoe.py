from collections import Counter


class Deck:

    def __init__(self):

        self.suits = ['H', 'S', 'C', 'D']
        self.faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.values = {}
        self.deck = []
        for i in self.suits:
            for j in self.faces:
                self.deck.append(f"{j}{i}")
                try:
                    self.values[f"{j}{i}"] = int(j)
                except:
                    if j == "A":
                        self.values[f"{j}{i}"] = 11
                    elif j == "J" or j == "Q" or j == "K":
                        self.values[f"{j}{i}"] = 10





class Shoe(Deck):

    def __init__(self, decks):
        super(Shoe, self).__init__()

        self.num_decks = decks
        self.shoe = Counter(self.deck * self.num_decks)
        self.cards_shown = []
        self.count = 0
        self.true_count = 0


    def new_shoe(self):

        self.shoe = Counter(self.deck * self.num_decks)
        self.cards_shown = []
        self.count = 0
        self.true_count = 0

    def remove(self, card):

        self.shoe[card] -= 1
        self.cards_shown.append(card)

        if self.values[card] >= 10:
            self.count -= 1
        elif self.values[card] <= 6:
            self.count += 1

        self.true_count = round(self.count / (sum(self.shoe.values())/52),3)



    def probs_all(self, counter=True):

        probs = {}
        current_total_cards = sum(self.shoe.values())

        for card in self.shoe.elements():
            probs[card] = round((self.shoe[card]/current_total_cards)*100, 3)

        if counter:
            return Counter(probs)
        else:
            return probs


    def prob_values(self, counter=True):

        cards = Counter()

        for card in self.shoe.elements():
            value = card[:-1]
            cards[value] += 1

        probs = {}
        for card in cards.elements():
            probs[card] = round((cards[card]/sum(cards.values()))*100, 3)

        if counter:
            return Counter(probs)
        else:
            return probs


    def prob_suits(self, counter=True):

        suits = Counter()

        for card in self.shoe.elements():
            suit = card[-1]
            suits[suit] += 1

        probs = {}
        for suit in suits.elements():
            probs[suit] = round((suits[suit]/sum(suits.values()))*100, 3)

        if counter:
            return Counter(probs)
        else:
            return probs



    def top_values(self, n=5):

        cards = Counter()

        for card in self.shoe.elements():
            value = card[:-1]
            cards[value] += 1

        return cards


    def top_suits(self, n=5):

        suits = Counter()

        for card in self.shoe.elements():
            suit = card[-1]
            suits[suit] += 1

        return suits
