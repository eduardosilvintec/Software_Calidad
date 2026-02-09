"""
Program 3: Word count.
Counts distinct words and their frequency across multiple test cases.
"""

import os
import string


def clean_word(word):
    """Normalize a word by lowering case and stripping punctuation."""
    return word.strip(string.punctuation).lower()


def process_file(input_file, output_file):
    """Process a text file and write word count results."""
    word_count = {}

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            for raw_word in line.split():
                word = clean_word(raw_word)
                if word:
                    word_count[word] = word_count.get(word, 0) + 1

    with open(output_file, "w", encoding="utf-8") as file:
        for word, count in word_count.items():
            file.write(f"{word}: {count}\n")


def main():
    """Process all test cases for Program 3."""
    base_path = "data/A4.2 Archivos de Apoyo - 06-02-26/P3"

    for i in range(1, 8):
        input_file = os.path.join(base_path, f"TC{i}.txt")

        if not os.path.exists(input_file):
            print(f"TC{i}.txt not found, skipped")
            continue

        output_file = os.path.join(base_path, f"TC{i}.Results.txt")
        process_file(input_file, output_file)
        print(f"TC{i} processed")


if __name__ == "__main__":
    main()
