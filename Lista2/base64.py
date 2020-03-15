import sys, argparse

TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
N=6


def decode(from_file, to_file):
    with open(from_file, "br") as f1:
        bytes_list = f1.read()
    
    new_bytes = ''
    for letter in bytes_list:
        new_bytes += bin(TABLE.index(chr(letter)))[2:].zfill(6)

    with open(to_file, "w") as f2:
        for i in range(0, len(new_bytes), 8):
            f2.write(chr(int(new_bytes[i:i+8],2)))


def encode(from_file, to_file):
    with open(from_file, "br") as f1:
        bytes_list = ["{:08b}".format(word) for word in f1.read()]
    byte_string = ''.join(bytes_list)
    divided_string = [byte_string[i:i+N] for i in range(0, len(byte_string), N)]
    
    with open(to_file, "w") as f2:
        for c in divided_string:
            f2.write(TABLE[int(c,2)])


if __name__ == "__main__":
    if sys.argv[1] == "--encode":
        encode(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "--decode":
        decode(sys.argv[2], sys.argv[3])
    else:
        print("Input: [--decode/--encode] from_file to_file")
