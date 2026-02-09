"""
Program 1: Compute statistics from multiple test cases.
Calculates mean, median, mode, variance and standard deviation.
"""

import os
from statistics import mean, median, mode, variance, stdev


def read_numbers(file_path):
    """Read numeric values from a text file, ignoring invalid entries."""
    numbers = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                numbers.append(float(line))
            except ValueError:
                continue

    return numbers


def compute_stats(numbers):
    """Compute basic statistics from a list of numbers."""
    return [
        ("Mean", mean(numbers)),
        ("Median", median(numbers)),
        ("Mode", mode(numbers)),
        ("Variance", variance(numbers)),
        ("Standard Deviation", stdev(numbers)),
    ]


def main():
    """Process all test cases for Program 1."""
    base_path = "data/A4.2 Archivos de Apoyo - 06-02-26/P1"

    for i in range(1, 8):
        input_file = os.path.join(base_path, f"TC{i}.txt")
        output_file = os.path.join(base_path, f"TC{i}.Results.txt")

        numbers = read_numbers(input_file)

        if not numbers:
            print(f"TC{i}.txt skipped (no valid numbers)")
            continue

        results = compute_stats(numbers)

        with open(output_file, "w", encoding="utf-8") as file:
            for name, value in results:
                file.write(f"{name}: {value}\n")

        print(f"TC{i} processed")


if __name__ == "__main__":
    main()
