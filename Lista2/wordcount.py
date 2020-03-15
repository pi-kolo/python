import sys

def file_stats(filename):
    """Prints number of bytes, lines, words and length of the longest line in a file"""
    with open(filename,"br") as f:
        file_bytes = f.read()
    with open(filename, "r", encoding="utf8") as f:
        file_lines = f.readlines()

    byte_amount = len(file_bytes)
    word_amount = sum([len(line.split()) for line in file_lines])
    line_amount = len(file_lines)
    longest_line = max([len(line) for line in file_lines])

    print(f"Bytes: {byte_amount}")
    print(f"Lines: {line_amount}")
    print(f"Words: {word_amount}")
    print(f"Longest line: {longest_line}")

if __name__ == "__main__":
    file_stats(sys.argv[1])