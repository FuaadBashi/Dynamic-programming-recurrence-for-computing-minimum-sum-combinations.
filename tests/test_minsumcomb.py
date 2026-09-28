import itertools
import random

import pytest

from main import minsumcomb


def brute_force_min_sum(x, m):
    return min((sum(c) for c in itertools.combinations(x, m)), default=float("inf"))


def test_the_worked_example_picks_the_two_smallest_numbers():
    result = minsumcomb([11, 3, -5, 8, 2], 2)

    assert result.cnfg == {"subset size": 2, "min sum": -3}
    assert sorted(result.val) == [-5, 2]


@pytest.mark.parametrize("seed", range(200))
def test_the_min_sum_matches_brute_force_on_random_inputs(seed):
    rng = random.Random(seed)
    x = [rng.randint(-20, 20) for _ in range(rng.randint(0, 8))]
    m = rng.randint(0, len(x))

    result = minsumcomb(x, m)

    assert result.cnfg["min sum"] == brute_force_min_sum(x, m)
    assert len(result.val) == m
    assert sum(result.val) == result.cnfg["min sum"]


def test_the_chosen_elements_come_from_the_input_without_reuse():
    x = [4, 4, 1, 1, 9]

    chosen = minsumcomb(x, 3).val

    remaining = list(x)
    for value in chosen:
        remaining.remove(value)  # raises if an element was used twice or invented


def test_choosing_nothing_costs_nothing():
    result = minsumcomb([5, -1], 0)

    assert result.val == []
    assert result.cnfg["min sum"] == 0


def test_asking_for_more_elements_than_exist_has_no_solution():
    result = minsumcomb([1, 2], 3)

    assert result.cnfg["min sum"] == float("inf")
    assert result.val == []


def test_a_negative_subset_size_is_rejected():
    with pytest.raises(ValueError):
        minsumcomb([1, 2], -1)
