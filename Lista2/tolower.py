import os, sys

def to_lower(directory):
    """Changes all names in directory to lowercase"""
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            os.rename(dirpath+"/"+filename, dirpath+"/"+filename.lower())
        for dirname in dirnames:
            os.rename(dirpath+"/"+dirname, dirpath+"/"+dirname.lower())

def to_upper(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        print(dirpath, dirnames, filenames)
        for filename in filenames:
            os.rename(dirpath+"/"+filename, dirpath+"/"+filename.upper())
        for dirname in dirnames:
            os.rename(dirpath+"/"+dirname, dirpath+"/"+dirname.upper())


if __name__ == "__main__":
    to_lower(sys.argv[1])