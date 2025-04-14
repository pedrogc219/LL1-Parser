from sys import argv

def read1(file):
    print(file.read(1))

def read2(file):
    print(file.read(1))

def read3(file):
    read2(file)
    print(file.read(1))