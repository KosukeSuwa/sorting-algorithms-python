from selection_sort import selection_sort
from merge_sort import merge_sort

TEST_CASES = [
    ([5, 2, 4, 1, 3], [1, 2, 3, 4, 5]),
    ([], []),
    ([1], [1]),
    ([3, 1, 3, 2], [1, 2, 3, 3]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, -1, 0], [-1, 0, 3]),
]

def test_selection_sort():
    for values, expected in TEST_CASES:
        result = selection_sort(values.copy())
        print(f"selection: {values} -> {result}")
        assert result == expected

def test_merge_sort():
    for values, expected in TEST_CASES:
        result = merge_sort(values.copy())
        print(f"merge:     {values} -> {result}")
        assert result == expected

if __name__ == "__main__":
    test_selection_sort()
    test_merge_sort()
    print("All tests passed.")