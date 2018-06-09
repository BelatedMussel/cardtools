import sys

players = []


score_to = False


final_score = False


def get_end():
    print("")
    is_end = input("Is there a final score to reach [Y/N]? >> ")
    if is_end.upper() == "Y":
        global score_to, final_score
        score_to = True
        print("")
        final_score = int(input("What is the goal of the final score to reach? >> "))
    else:
        score_to = False


def add_players():
    while True:
        name = input("Enter names of players, leave blank if done: ")
        if not name:
            break
        players.append(name)
    if not players:
        sys.exit()


score = []


def starting_score():
    for name in range(0, len(players)):
        score.append(0)


def score_card():
    count = 0
    for name in range(0, len(players)):
        print(players[0 + count], ":", score[0 + count])
        count += 1


def end_count():
    global final_score
    if isinstance(final_score, int):
        if any(point >= final_score for point in score):
            print("")
            score_card()
            print("")
            print("The game has ended, thank you for playing.")
            sys.exit()
        else:
            print("")
            score_card()
            print("")
            update_score()
    else:
        print("")
        score_card()
        print("")
        update_score()


def update_score():
    count = 0
    for name in range(0, len(players)):
        add_score = input("How many points did {} score this hand? >> ".format(players[0 + count]))
        score[0 + count] += int(add_score)
        count += 1
    end_count()


# Starting the game

get_end()

print("")
add_players()

print("")
starting_score()

# Debugging Options
# print(score_to)

# print(final_score)

# print(players)

# print(score)

# print("This is the first score card")
print("")
score_card()

# print("This is the first score update")
print("")
update_score()
