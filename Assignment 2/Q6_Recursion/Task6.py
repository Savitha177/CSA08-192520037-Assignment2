# Task 6: Recursion and Its Limits
# Count ways to climb n steps when each move is 1 or 2 steps.

import sys
import time
from functools import lru_cache

naive_calls = 0
memo_calls = 0


def ways_naive(n):
    """Plain recursive solution for staircase counting."""
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    """Memoized recursive staircase solution."""
    global memo_calls
    memo_calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_iterative(n):
    """Iterative solution using only the last two values."""
    if n <= 1:
        return 1

    previous_two = 1
    previous_one = 1

    for _ in range(2, n + 1):
        previous_two, previous_one = (
            previous_one,
            previous_two + previous_one,
        )

    return previous_one


def print_call_tree():
    print("\nILLUSTRATIVE CALL TREE FOR ways_naive(5)")
    print("----------------------------------------")
    print("ways(5)")
    print("|-- ways(4)")
    print("|   |-- ways(3)")
    print("|   |   |-- ways(2)")
    print("|   |   |   |-- ways(1)")
    print("|   |   |   |-- ways(0)")
    print("|   |   |-- ways(1)")
    print("|   |-- ways(2)")
    print("|       |-- ways(1)")
    print("|       |-- ways(0)")
    print("|-- ways(3)")
    print("    |-- ways(2)  [repeated work]")
    print("    |-- ways(1)")


def main():
    global naive_calls, memo_calls

    print("STAIRCASE RECURSION PERFORMANCE ANALYSIS")
    print("=" * 55)

    print("\nCORRECTNESS CHECK: n = 1 TO 6")
    print("------------------------------")
    print("n\tNaive\tMemoized\tIterative")

    for n in range(1, 7):
        naive_calls = 0
        naive_result = ways_naive(n)

        ways_memo.cache_clear()
        memo_calls = 0
        memo_result = ways_memo(n)

        iterative_result = ways_iterative(n)

        assert naive_result == memo_result == iterative_result

        print(
            f"{n}\t{naive_result}\t{memo_result}"
            f"\t\t{iterative_result}"
        )

    print_call_tree()

    print("\nCALL COUNTS AND TIMINGS")
    print("----------------------")
    print(
        "n\tNaive calls\tNaive time (s)"
        "\tMemo calls\tMemo time (s)"
    )

    for n in [10, 20, 25, 30]:
        naive_calls = 0

        start = time.perf_counter()
        naive_result = ways_naive(n)
        naive_time = time.perf_counter() - start
        calls_naive = naive_calls

        ways_memo.cache_clear()
        memo_calls = 0

        start = time.perf_counter()
        memo_result = ways_memo(n)
        memo_time = time.perf_counter() - start
        calls_memo = memo_calls

        assert naive_result == memo_result

        print(
            f"{n}\t{calls_naive}\t\t{naive_time:.6f}"
            f"\t\t{calls_memo}\t\t{memo_time:.6f}"
        )

    print("\nRECURSION LIMIT INVESTIGATION")
    print("-----------------------------")
    print("Python recursion limit:", sys.getrecursionlimit())

    ways_memo.cache_clear()

    try:
        result_1000 = ways_memo(1000)
        print("Memoized n=1000 completed:", True)
        print("Result digit count:", len(str(result_1000)))

    except RecursionError:
        print(
            "Memoized n=1000: RecursionError "
            "(expected on a typical default limit)."
        )
        print(
            "Memoization avoids repeated work but still "
            "creates recursive calls."
        )

    ways_memo.cache_clear()

    start = time.perf_counter()
    iterative_1000 = ways_iterative(1000)
    iterative_time = time.perf_counter() - start

    print("Iterative n=1000: PASS")
    print("Result digit count:", len(str(iterative_1000)))
    print(f"Iterative time: {iterative_time:.6f} s")

    print("\nCOMPLEXITY")
    print("----------")
    print("Naive recursion: O(2^n) time; O(n) call-stack space.")
    print("Memoization: O(n) time; O(n) cache and call-stack space.")
    print("Iteration: O(n) time; O(1) auxiliary space.")
    print(
        "Decision: use recursion to demonstrate the concept "
        "and iteration for n=1000."
    )


if __name__ == "__main__":
    main()