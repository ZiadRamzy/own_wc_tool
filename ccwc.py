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



def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and call the byte-counting function."""

    if len(sys.argv) != 3:
        print("Usage ccwc -c <filename>")
        sys.exit(1)

    option = sys.argv[1]
    file_path = sys.argv[2]

    if option == "-c":
        byte_count = count_bytes(file_path)
        print(f" {byte_count}  {os.path.basename(file_path)}")
    else:
        print("Error: Unsupported option. Only -c is supported.")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)