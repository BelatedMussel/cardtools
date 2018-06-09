# French Tarot scoring
# A script designed to calculate the scores for French Tarot based on the traditional method of
# ((25 + pt + pb) * mu) + pg + ch

min_pt = 0

real_pt = 0

pt = 0

bout = 0

pb = 0

mu = 1

pg = 0

ch = 0

players = 0

taker = True

score = 0


def get_players():
    global players
    get = int(input("How many are playing? >> "))
    if int(get) == 4:
        players = 4
    elif int(get) == 3:
        players = 3
    elif int(get) == 2:
        players = 2
    else:
        print("Please put a valid integer to represent the number of players.")
        get_players()


def bouts():
    global bout, min_pt
    bout = int(input("How many bouts did the taker have? >> "))
    if bout == 0:
        min_pt = 56
    elif bout == 1:
        min_pt = 51
    elif bout == 2:
        min_pt = 41
    elif bout == 3:
        min_pt = 36
    else:
        print("Please put a valid integer.")
        bouts()


def card_points():
    global real_pt
    real_pt = int(input("How many card points did the taker take? >> "))


def petit_au_bout():
    global pb
    get = input("Did the winning side win the last trick with the 1 of trump in it (petit au bout)? [Y/N] >> ")
    if get.capitalize() == "Y":
        pb = 10
        print("Petit au bout bonus scored.")
    else:
        pb = 0
        print("No petit au bout bonus.")


def contract():
    global mu
    print("1. Petite")
    print("2. Garde")
    print("3. Garde sans le chien")
    print("4. Garde contre le chien")
    get = input("What contract was played? >> ")
    if get == "1" or get == "1.":
        mu = 1
        print("The contract was Petite.")
    elif get == "2" or get == "2.":
        mu = 2
        print("The contract was Garde.")
    elif get == "3" or get == "3.":
        mu = 4
        print("The contract was Garde sans le chien.")
    elif get == "4" or get == "4.":
        mu = 6
        print("The contract was Garde contra le chien.")
    else:
        print("Please input a valid number as an answer.")
        contract()


def poingee():
    global pg, players
    get = input("Was poingee declared? [Y/N] >> ")
    if get.capitalize() == "Y":
        if players == 3:
            print("1. 13 trumps")
            print("2. 15 trumps")
            print("3. 18 trumps")
        elif players == 5:
            print("1. 8 trumps")
            print("2. 10 trumps")
            print("3. 13 trumps")
        else:
            print("1. 10 trumps")
            print("2. 13 trumps")
            print("3. 15 trumps")
        getit = input("How many trumps were declared? >> ")
        if getit == "1" or getit == "1.":
            pg = 20
            print("Single poingee declared.")
        elif getit == "2" or getit == "2.":
            pg = 30
            print("Double poingee declared.")
        elif getit == "3" or getit == "3.":
            pg = 40
            print("Triple poingee declared.")
        else:
            print("Please input a valid number as answer.")
            poingee()
    else:
        print("No poingee bonus.")


def chelem():
    global ch
    get = input("Was chelem announced? [Y/N] >> ")
    if get.capitalize() == "Y":
        getit = input("Was it successful? [Y/N] >> ")
        if getit.capitalize() == "Y":
            ch = 400
            print("Successful chelem annonce.")
        else:
            ch = -200
            print("Unsuccessful chelem annonce.")
    else:
        getmore = input("Did chelem occur anyway? [Y/N] >> ")
        if getmore.capitalize() == "Y":
            ch = 200
            print("Chelem non annonce.")
        else:
            ch = 0
            print("No chelem bonus.")


def taker_win():
    global taker
    get = input("Did the taker win the hand? [Y/N] >> ")
    if get.capitalize() == "Y":
        taker = True
        print("The taker was successful.")
    else:
        taker = False
        print("The taker failed.")


def final_calc():
    global pt, pb, mu, pg, ch, players, taker, score
    pt = (real_pt - min_pt)
    score = (((25 + pt + pb) * mu) + pg + ch)
    if taker is True:
        payup = score * (players - 1)
        print("")
        print("")
        print("The taker scores", payup, "points total.")
        print("The rest lose", score, "points.")
    if taker is False:
        payouts = score * (players - 1)
        print("")
        print("")
        print("The winning players each score", score, "points.")
        print("The taker loses", payouts, "points.")


def two_calc():
    global pt, pb, ch
    pt = (real_pt - min_pt)
    points = (25 + pt + pb) + ch
    print("")
    print("")
    print("The winner of the hand takes", points, "points.")
    print("The loser of the hand loses", points, "points.")


def main():
    print("")
    print("")
    print("")
    bouts()
    card_points()
    contract()
    petit_au_bout()
    poingee()
    chelem()
    taker_win()
    final_calc()
    main()


def for_two():
    print("")
    print("")
    print("")
    bouts()
    card_points()
    petit_au_bout()
    chelem()
    two_calc()
    for_two()


def start():
    print("Tarot Calculator v1.0")
    print("(C) 2018 Josh Kurtenbach")
    print("Licenced under GPLv3")
    print("")
    get_players()

    if players == 2:
        for_two()
    else:
        main()


start()
