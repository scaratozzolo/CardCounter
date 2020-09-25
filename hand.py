from shoe import Deck


class Hand(Deck):

    def __init__(self, p1, p2, du):

        super(Hand, self).__init__()

        self.hands = {1: {'hand':[p1, p2], 'soft': False, 'total': 0}}
        self.dealer = [du]

        self.calc_hand_total(1)


    def get_hand_total(self, handindex=1):

        return self.hands[handindex]['total']



    def calc_hand_total(self, handindex=1):

        hand = self.hands[handindex]['hand']

        soft_total = 0
        hard_total = 0

        if hand[0][:-1] == "A" and hand[1][:-1] == "A":
            soft_total = 2
            hard_total = 12
            self.hands[handindex]['soft'] = True
            for card in hand[2:]:

                if card[:-1] == "A":
                    hard_total = soft_total + self.values[card]
                    soft_total += 1

                else:
                    hard_total += self.values[card]
                    soft_total += self.values[card]

                if hard_total > 21:
                    self.hands[handindex]['soft'] = False
        else:
            for card in hand:

                if card[:-1] == "A":
                    hard_total += self.values[card]
                    soft_total += 1
                    self.hands[handindex]['soft'] = True

                else:
                    hard_total += self.values[card]
                    soft_total += self.values[card]

                if hard_total > 21:
                    self.hands[handindex]['soft'] = False

        if hard_total > 21 and soft_total > 21:
            self.hands[handindex]['total'] = -1

        elif hard_total > 21 or soft_total > 21:
            self.hands[handindex]['total'] = min([hard_total, soft_total])

        else:
            self.hands[handindex]['total'] = max([hard_total, soft_total])


        return soft_total, hard_total


    def hit(self, card, handindex=1):

        self.hands[handindex]['hand'].append(card)
        self.calc_hand_total(handindex)


    def split(self, handindex=1):

        self.hands[max(self.hands.keys())+1] = {'hand':[self.hands[handindex]['hand'].pop()], 'soft': False, 'total': 0}


    def __str__(self):

        string = ""
        for i in self.hands.keys():
            string += f"Hand {i}: {self.hands[i]['hand']}\n"
            # soft, hard = self.calc_hand_total(handindex=i)
            # string += f"Total: {soft}/{hard}\n\n" if self.hands[i]['soft'] else f"Total: {self.hands[i]['total']}\n\n"
            string += f"Total: {self.hands[i]['total']}\n"
            string += f"Soft: {self.hands[i]['soft']}\n\n"

        return string
