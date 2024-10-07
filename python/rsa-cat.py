#!/bin/python
import argparse
import pickle

def readfile(name):
    with open(name,'rb') as f:
        return pickle.load(f)

def main():
    parser=argparse.ArgumentParser(description="Reads a pickle formatted file and prints the contents to STDOUT.\nexample uses: rsa-cat.py pub.pk, rsa-cat.py encrypted.bin")
    parser.add_argument('input',help="input file.")

    args=parser.parse_args()

    print(readfile(args.input))

if __name__ == "__main__":
    main()
