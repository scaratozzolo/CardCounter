from shoe import Shoe
from hand import Hand


def main(DECKS):

    shoe = Shoe(DECKS)

    while True:

        choice = input("n: new hand, q: quit")

        if choice == "q":
            break
        elif choice == "n":
            pass


if __name__ == "__main__":


    DECKS = int(input("Number of decks: "))
    # GAME_VERSION = input("Game version (BU, DKI, T): ")

    h = Hand("AH", "10H", "6C")
    print(h)
    h = Hand("AH", "AH", "6C")
    h.split()
    h.hit("10C",handindex=0)
    h.hit("8H", handindex=1)
    print(h)

    # Calculating soft is still weird
