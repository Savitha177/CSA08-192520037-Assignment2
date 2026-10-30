# Task 4: Building Long Text
# Compare repeated +=, join(), and repeated f-string building.

import time


def build_plus(parts):
    text = ""

    for part in parts:
        text += part + ";"

    return text


def build_join(parts):
    # Builds the same output, including the final semicolon.
    return ";".join(parts) + (";" if parts else "")


def build_f_string(parts):
    text = ""

    for part in parts:
        text = f"{text}{part};"

    return text


def measure(function, parts):
    start = time.perf_counter()
    result = function(parts)
    elapsed = time.perf_counter() - start

    return result, elapsed


def main():
    print("STRING BUILDING PERFORMANCE COMPARISON")
    print("=" * 55)

    sizes = [1_000, 10_000, 20_000]

    methods = [
        ("Repeated +=", build_plus),
        ("join()", build_join),
        ("Repeated f-string", build_f_string),
    ]

    for size in sizes:
        items = [f"Item{i}:Rs{i % 50}" for i in range(size)]

        print(f"\nNumber of lines: {size:,}")
        print("-" * 55)

        outputs = {}
        averages = {}

        for name, function in methods:
            timings = []
            result = None

            for _ in range(3):
                result, elapsed = measure(function, items)
                timings.append(elapsed)

            outputs[name] = result
            averages[name] = sum(timings) / len(timings)

            print(name)
            print(
                "  Run times (s):",
                ", ".join(f"{t:.6f}" for t in timings)
            )
            print(f"  Average time: {averages[name]:.6f} s")
            print(f"  Output length: {len(result):,}")

        same = (
            outputs["Repeated +="]
            == outputs["join()"]
            == outputs["Repeated f-string"]
        )

        print(
            "Same text from all methods:",
            "PASS" if same else "FAIL"
        )

        if size == 200_000:
            print(
                "Expected output length for 200,000 lines: 3,048,890"
            )
            print(
                "Actual output length matches expected:",
                len(outputs["join()"]) == 3_048_890
            )

    print("\nCOMPLEXITY ANALYSIS")
    print("-------------------")
    print(
        "Repeated +=: up to O(total output size squared) "
        "in the general case."
    )
    print(
        "join(): O(total output size), with a list of parts "
        "already available."
    )
    print(
        "Repeated f-string: repeated rebuilding can also "
        "take quadratic time."
    )
    print(
        "Note: CPython may optimize some += cases; "
        "actual timings vary by system."
    )


if __name__ == "__main__":
    main()