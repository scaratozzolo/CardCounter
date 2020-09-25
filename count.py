from shoe import Shoe
from hand import Hand


def main(DECKS):

    shoe = Shoe(DECKS)

    while True:

        choice = input("n - new hand, q - quit: ").upper()

        if choice == "Q":
            break
        elif choice == "N":

            p1 = input("Your first card: ").upper()
            du = input("Dealer up card: ").upper()
            p2 = input("Your second card: ").upper()

            h = Hand(p1, p2, du)
            shoe.remove(p1)
            shoe.remove(p2)
            shoe.remove(du)
            print(h)

            while True:

                choice2 = input("h - hit, p - split, s - stand: ").upper()
                if choice2[0] == "S":
                    break

                elif choice2[0] == "H":
                    choicesplit = choice2.split(" ")
                    try:
                        handindex = int(choicesplit[2])
                    except:
                        handindex = 1

                    h.hit(choicesplit[1], handindex=handindex)
                    shoe.remove(choicesplit[1])
                    print(h)

                elif choice2[0] == "P":

                    choicesplit = choice2.split(" ")
                    try:
                        handindex = int(choicesplit[1])
                    except:
                        handindex = 1

                    h.split(handindex=handindex)
                    print(h)

            print(shoe.count)
if __name__ == "__main__":


    DECKS = int(input("Number of decks: "))
    # GAME_VERSION = input("Game version (BU, DKI, T): ")

    main(DECKS)


    # h = Hand("AH", "AH", "6C")
    # print(h)
    # h.split()
    # h.hit("8H", 1)
    # h.hit("6C", 2)
    # print(h)
    # h.hit("10C", 2)
    # print(h)

    # Calculating soft is still weird
