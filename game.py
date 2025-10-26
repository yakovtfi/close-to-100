from utils import roll_two_d6,is_bust,is_exact_100,closer_to_target,tie_breaker
def turn_decision(input_fn=input) -> str:
    while True:
        choice = input_fn("Choose action (r = roll, p = pass): ").strip().lower()
        if choice in ("r", "p"):
            return choice
        print("Invalid input, please enter 'r' or 'p'.")

def play_game():
    print(" Welcome to the race to 100 points!")
    scores = [0, 0]
    passes = [False, False]
    current_player = 0
    while True:
        print(f"\n Player {current_player + 1}is turn")
        print(f"Scores  Player 1: {scores[0]}, Player 2: {scores[1]}")
        choice = turn_decision()
        if choice == "r":
            d1, d2 = roll_two_d6()
            roll_sum = d1 + d2
            scores[current_player] += roll_sum
            print(f"Player {current_player + 1} rolled {d1} + {d2} = {roll_sum} → total {scores[current_player]}")

            if is_bust(scores[current_player]):
                print(f" Player {current_player + 1} busted! Player {2 - current_player} wins immediately!")
                break

            if is_exact_100(scores[current_player]):
                print(f" Player {current_player + 1} hit exactly 100 and wins!")
                break
            passes[current_player] = False
        elif choice == "p":
            passes[current_player] = True
            print(f"Player {current_player + 1} passes.")
            if passes == [True, True]:
                print("\n Both players passed")
                winner = closer_to_target(scores[0], scores[1])
                if winner is not None:
                    print(f" Player {winner} wins with {scores[winner - 1]} points!")
                    break
                else:
                    print("It's a tie! Rolling tie-breaker")
                    winner = tie_breaker()
                    print(f" Player {winner} wins after tie-breaker!")
                    break
        current_player = 1 - current_player
