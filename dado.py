from itertools import product


def get_weighted_sample_space(sample_space):
    weighted_sample_space = {sum(outcome): 0 for outcome in sample_space}

    for outcome in sample_space:
        total = sum(outcome)
        weighted_sample_space[total] += 1

    return weighted_sample_space


def get_matching_event(condition, sample_space):
    return set([outcome for outcome in sample_space if condition(outcome)])


def compute_event_probability(samples, sample_space):
    return len(samples) / len(sample_space)


if __name__ == "__main__":
    dado = list(range(1, 7))

    sample_space = set(product(dado, repeat=6))
    samples = get_matching_event(lambda x: sum(x) == 21, sample_space)
    probability = compute_event_probability(samples, sample_space)
    print(f"Probability of getting 21: {probability}")

    weighted_sample_space = get_weighted_sample_space(
        set(product(dado, repeat=6)))
    probability = weighted_sample_space[21] / len(sample_space)
    print(f"Probability of getting 21: {probability}")
