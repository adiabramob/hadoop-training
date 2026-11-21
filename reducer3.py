#!/usr/bin/env python3
"""reducer3.py - Exercise 3: output only the top 3 words by count"""
from itertools import groupby
from operator import itemgetter
import heapq
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t', top_n=3):
    data = read_mapper_output(sys.stdin, separator=separator)
    top = []  # min-heap of (count, word), keeps only the top_n largest
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
        except ValueError:
            continue
        heapq.heappush(top, (total_count, current_word))
        if len(top) > top_n:
            heapq.heappop(top)
    for total_count, word in sorted(top, reverse=True):
        print("%s%s%d" % (word, separator, total_count))

if __name__ == "__main__":
    main()
