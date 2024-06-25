# test script for the probability function we define in dsum_probability scripy

from dsum_probability import probability  

def test_probability():
    test_cases = [
        (1, 4, 1/6),     # Probability of getting sum 4 with 1 dice (one way (4))
        (1, 7, 0),       # Probability of getting sum 7 with 1 dice (no way)
        (2, 1, 0),       # Probability of getting sum 1 with 2 dices (no way)
        (2, 2, 1/36),    # Probability of getting sum 2 with 2 dices (only 1 way: (1,1))
        (2, 3, 2/36),    # Probability of getting sum 3 with 2 dices (two ways: (1,2), (2,1))
        (2, 7, 6/36),    # Probability of getting sum 7 with 2 dices (six ways: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1))
        (3, 5, 6/(6**3)),# Probability of getting sum 5 with 3 dices (six ways: (2,2,1), (2,1,2), (1,2,2), (3,1,1), (1,3,1), (1,1,3))
    ]

    for n, m, expected in test_cases:
        result = probability(m, n)
        print(f"Testing n={n}, m={m}: got {result}, expected {expected}")
        assert abs(result - expected) < 1e-9, f"Test failed for n={n}, m={m}: got {result}, expected {expected}"

if __name__ == "__main__":
    test_probability()
