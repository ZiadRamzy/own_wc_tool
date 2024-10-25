import sys
import os
from typing import List

def count_bytes(file_path: str) -> int:
    """Counts the number of bytes in the specified file."""

    try:
        with open(file_path, "rb") as file:
            content: bytes = file.read()
            return len(content)
    except FileNotFoundError:
        print(f" Error: File {file_path} not found.")
        sys.exit(1)

def count_lines(file_path: str) -> int:
    """Counts the number of lines in the specified file."""

    try:
        with open(file_path, "r") as file:
            lines: List[str] = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

def count_words(file_path: str) -> int:
    """Counts the number of words in the specified file."""

    try:
        with open(file_path, "r") as file:
            content: str = file.read()
            words: List[str] = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

def count_characters(file_path: str) -> int:
    """Counts the number of characters in the specified file."""

    try:
        with open(file_path, "rb") as file:
            content: bytes = file.read()
            decoded_content = content.decode('utf-8-sig')
            if decoded_content and decoded_content[-1] == '\n':
                return len(decoded_content) + 1
            return len(decoded_content)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)


def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and call the appropriate counting function."""

    if len(args) < 2 or len(args) > 3:
        print("Usage ccwc [-c/-l/-w/-m] <filename>")
        sys.exit(1)

    if len(args) == 2: # No option provided
        file_path: str = args[1]
        line_count: int = count_lines(file_path)
        word_count: int = count_words(file_path)
        byte_count: int = count_bytes(file_path)
        print(f" {line_count} {word_count} {byte_count} {os.path.basename(file_path)}")

    else:
        option = args[1]
        file_path = args[2]

        if option == "-c":
            byte_count: int = count_bytes(file_path)
            print(f" {byte_count}  {os.path.basename(file_path)}")
        elif option == "-l":
            line_count: int = count_lines(file_path)
            print(f" {line_count} {os.path.basename(file_path)}")
        elif option == "-w":
            word_count: int = count_words(file_path)
            print(f" {word_count} {os.path.basename(file_path)}")
        elif option == "-m":
            character_count: int = count_characters(file_path)
            print(f" {character_count} {os.path.basename(file_path)}")
        else:
            print("Error: Unsupported option. Use -c for byte count, -l for line count, -w for word count or -m for character count.")
            sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)