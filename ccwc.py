import sys
import os
from typing import List, Optional

def count_bytes(content: bytes) -> int:
    """Counts the number of bytes in the provided content."""

    return len(content)

def count_lines(content: str) -> int:
    """Counts the number of lines in the provided content."""

    return content.count('\n')

def count_words(content: str) -> int:
    """Counts the number of words in the provided content."""

    words: List[str] = content.split()
    return len(words)

def count_characters(content: str) -> int:
    """Counts the number of characters in the provided content."""
    
    return len(content)


def read_file_content(file_path: Optional[str] = None) -> int:
    """Reads content from a file or from standard input if no file is specified."""
   
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            sys.exit(1)
    else:
        return sys.stdin.read()


def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and call the appropriate counting function."""

    if  len(args) > 3:
        print("Usage ccwc [-c/-l/-w/-m] <filename>")
        sys.exit(1)

    
    option: Optional[str] = None
    file_path: Optional[str] = None

    if len(args) == 2:
        if args[1].startswith("-"):
            option = args[1]
        else:
            file_path  = args[1]
    elif len(args) == 3:
        option = args[1]
        file_path = args[2]
    
    content: str = read_file_content(file_path)
    byte_content: bytes = content.encode('utf-8')

    if option == "-c":
        byte_count: int = count_bytes(byte_content)
        print(f" {byte_count}")
    elif option == "-l":
        line_count: int = count_lines(content)
        print(f" {line_count}")
    elif option == "-w":
        word_count: int = count_words(content)
        print(f" {word_count}")
    elif option == "-m":
        character_count: int = count_characters(content)
        print(f" {character_count}")
    elif option is None:
        line_count: int = count_lines(content)
        word_count: int = count_words(content)
        byte_count: int = count_bytes(byte_content)
        print(f" {line_count} {word_count} {byte_count}")
    else:
        print("Error: Unsupported option. Use -c for byte count, -l for line count, -w for word count or -m for character count.")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)