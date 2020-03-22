import os, sys
import hashlib


def find_similar(directory):
    files = {}
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = dirpath+"/"+filename
            size = os.stat(file_path).st_size
            file_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                data = f.read(65536)
                while len(data) > 0:
                    file_hash.update(data)
                    data = f.read(65536)
            if files.get((size, file_hash.hexdigest())):
                files[(size, file_hash.hexdigest())].append(file_path)
            else:
                files[(size, file_hash.hexdigest())] = [file_path]
    for _, item in files.items():
        if len(item) > 1:
            for el in item:
                print(el)
            print("~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    find_similar(sys.argv[1])