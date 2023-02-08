from itertools import product


def get_weigthed_sample_space(sample_space):
    sums = [sum(s) for s in sample_space if True]
    weigthed_sample_space = dict()
    for s in sums:
        weigthed_sample_space[s] += 1

    return weigthed_sample_space


def get_matching_event(condition, sample_space):
    return set([outcome for outcome in sample_space if condition(outcome)])


def compute_event_probability(samples, sample_space):
    return len(samples) / len(sample_space)


if __name__ == "__main__":
    dado = list(range(1, 7))

    sample_space = get_weigthed_sample_space(set(product(dado, repeat=6)))
    samples = get_matching_event(lambda x: sum(x) == 21, sample_space)
    probability = compute_event_probability(samples, sample_space)

    print(f"Probability of getting 21: {probability}")
