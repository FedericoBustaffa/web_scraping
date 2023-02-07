
def fair_coin():
    sample_space = {"heads", "tails"}
    probability_heads = 1 / len(sample_space)
    print(f"Probability of chosen heads is {probability_heads}")


def is_heads(face):
    return face == "Heads"


def match_event(condition, sample_space):
    p = len([sample for sample in sample_space if condition(sample)])
    return p / len(sample_space)


if __name__ == "__main__":
    fair_coin()
    coin = {"Heads", "Tails"}
    print(match_event(is_heads, coin))

    l = [x for x in {1, 2, 3, 4, 5} if x % 2 != 0]
    print(l)
