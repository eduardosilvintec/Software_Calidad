"""
Program 2: Convert decimal numbers to binary and hexadecimal.
Reads integer values from input files and writes conversion results.
"""

import os


def read_numbers(file_path):
    """Read integer values from a text file, ignoring invalid entries."""
    numbers = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                numbers.append(int(line))
            except ValueError:
                continue

    return numbers


def main():
    """Process all test cases for Program 2."""
    base_path = "data/A4.2 Archivos de Apoyo - 06-02-26/P2"

    for i in range(1, 8):
        input_file = os.path.join(base_path, f"TC{i}.txt")

        if not os.path.exists(input_file):
            print(f"TC{i}.txt not found, skipped")
            continue

        output_file = os.path.join(base_path, f"TC{i}.Results.txt")
        numbers = read_numbers(input_file)

        if not numbers:
            print(f"TC{i}.txt skipped (no valid numbers)")
            continue

        with open(output_file, "w", encoding="utf-8") as file:
            for number in numbers:
                binary_value = bin(number)
                hex_value = hex(number)
                file.write(f"{number} -> {binary_value} , {hex_value}\n")

        print(f"TC{i} processed")


if __name__ == "__main__":
    main()
