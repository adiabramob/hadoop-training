#!/usr/bin/env python3
"""mapper2.py - Exercise 2: strip trailing commas/dots, case-insensitive word count"""
import sys

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            word = word.rstrip('.,').lower()
            if word:
                print('%s%s%d' % (word, separator, 1))

if __name__ == "__main__":
    main()
