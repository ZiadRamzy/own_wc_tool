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


def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and call the appropriate counting function."""

    if len(sys.argv) != 3:
        print("Usage ccwc -c/-l <filename>")
        sys.exit(1)

    option = sys.argv[1]
    file_path = sys.argv[2]

    if option == "-c":
        byte_count: int = count_bytes(file_path)
        print(f" {byte_count}  {os.path.basename(file_path)}")
    elif option == "-l":
        line_count: int = count_lines(file_path)
        print(f" {line_count} {os.path.basename(file_path)}")
    else:
        print("Error: Unsupported option. Use -c for byte count or -l for line count.")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)