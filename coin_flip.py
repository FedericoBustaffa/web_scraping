from itertools import product


def is_heads(face):
    return face[0] == "Heads"


def is_two_heads(faces):
    return faces[0] == "Heads" and faces[1] == "Heads"


def get_matching_event(condition, sample_space):
    return set([outcome for outcome in sample_space if condition(outcome)])


def compute_event_probability(samples, sample_space):
    return len(samples) / len(sample_space)


if __name__ == "__main__":
    coin = ["Heads", "Tails"]

    print("---- 1 Flip ----")
    sample_space = set(product(coin, repeat=1))

    print("Sample space")
    for sample in sample_space:
        print(sample)

    matching_event_space = get_matching_event(is_heads, sample_space)
    prob = compute_event_probability(matching_event_space, sample_space)
    print(f"probability of \'is heads\': {prob}\n")

    print("---- 2 Flips ----")
    sample_space = set(product(coin, repeat=2))

    print("Sample space")
    for sample in sample_space:
        print(sample)

    matching_event_space = get_matching_event(is_two_heads, sample_space)
    prob = compute_event_probability(matching_event_space, sample_space)
    print(f"probability of \'is 2 heads\': {prob}")

    matching_event_space = get_matching_event(is_heads, sample_space)
    prob = compute_event_probability(matching_event_space, sample_space)
    print(f"probability of \'is heads\': {prob}")
