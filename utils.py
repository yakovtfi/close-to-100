import random
def roll_two_d6() -> tuple[int, int]:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return (die1, die2)


def is_bust(score: int) -> bool:
    return score > 100



def is_exact_100(score: int) -> bool :
    return score == 100


def closer_to_target(a: int, b: int, target: int = 100) -> int | None :
    dist_a = abs(target - a)
    dist_b = abs(target - b)
    if dist_a < dist_b:
        return 1
    elif dist_b < dist_a:
        return 2
    else:
        return None


def tie_breaker(roller) -> int:
    while True:
        d1a, d2a = roller()
        d1b, d2b = roller()
        sum_a = d1a + d2a
        sum_b = d1b + d2b
        print(f"Player 1 rolled {d1a}+{d2a}={sum_a}")
        print(f"Player 2 rolled {d1b}+{d2b}={sum_b}")
        if sum_a > sum_b:
            print("Player 1 wins the tie-breaker!")
            return 1
        elif sum_b > sum_a:
            print("Player 2 wins the tie-breaker!")
            return 2
        else:
            print("Tie again! Rolling again...")





