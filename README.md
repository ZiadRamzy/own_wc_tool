# CCWC - Custom Word Count Tool

CCWC (Coding Challenges Word Count) is a custom-built version of the Unix wc tool. This command-line utility provides counts for lines, words, bytes, and characters in a file, with support for multiple options and standard input. CCWC was developed as part of a coding challenge to recreate the functionality of the Unix wc command following the Unix Philosophy of simplicity and modularity.

## Features

- **Byte Count (`-c`)**: Counts the number of bytes in a file.
- **Line Count (`-l`)**: Counts the number of lines in a file.
- **Word Count (`-w`)**: Counts the number of words in a file.
- **Character Count (`-m`)**: Counts the number of characters in a file.
- **Default Mode (No Flags)**: Outputs line, word, and byte counts in the format: `lines words bytes filename`.
- **Standard Input Support**: Reads from `stdin` if no filename is provided, making it compatible with Unix pipelines.

## Usage

To use CCWC, run the `ccwc.py` script with one of the options and a filename (or standard input). Below are usage examples for each mode:

### Examples:

**Count Bytes(`-c`)**

```bash
python3 ccwc.py -c test.txt
```

Example Output:

```bash
 342190 test.txt
```

**Count Lines (`-l`)**

```bash
python3 ccwc.py -l test.txt
```

Example Output:

```bash
   7145 test.txt
```

**Count Words (`-w`)**

```bash
python3 ccwc.py -w test.txt
```

Example Output:

```bash
  58164 test.txt
```

**Count Characters (`-m`)**

```bash
python3 ccwc.py -m test.txt
```

Example Output:

```bash
 339292 test.txt
```

**Default Mode (Lines, Words, and Bytes)**

If no options are provided, CCWC outputs line, word, and byte counts by default:

```bash
python3 ccwc.py test.txt
```

Example Output:

```bash
   7145   58164  342190 test.txt
```

**Reading from Standard Input**

CCWC can read from standard input when no filename is specified. For example:

```bash
cat test.txt | python3 ccwc.py -l
```

Example Output:

```bash
   7145
```

Or, to get line, word, and byte counts from standard input:

```bash
cat test.txt | python3 ccwc.py
```

Example Output:

```bash
   7145   58164  342190
```

## Installation

- Clone the repository:

```bash
git clone https://github.com/yourusername/ccwc.git
cd ccwc
```

- Ensure you have Python 3 installed. You can verify by running:

```bash
python3 --version
```

- Run `ccwc.py` using the examples above.

## About the Challenge

This project was developed as part of a coding challenge to recreate the Unix `wc` tool. If additional information about the challenge is needed, please refer to the [original challenge post](https://codingchallenges.fyi/challenges/challenge-wc).
