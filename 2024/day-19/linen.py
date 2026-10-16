#!/usr/bin/env python3

import argparse
import datetime as dt

from functools import cache

class Node:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.children = {}

    def display(self, level=0):
        print(f'{level=}: {self.children.keys()=}, {self.leaf=}')

        for _, child in self.children.items():
            child.display(level + 1)

class Trie:
    def __init__(self):
        self.root = Node(True)

    def display(self):
        self.root.display()

    def insert(self, word):
        root = self.root

        for component in word:
            if component not in root.children:
                root.children[component] = Node(False)

            root = root.children[component]

        # Mark node as a valid end point
        root.leaf = True

    def isValid(self, prefix):
        root = self.root

        for c in prefix:
            if c not in root.children:
                return False

            root = root.children[c]

        return root.leaf

    @cache
    def search(self, word):

        length = len(word)

        # Base case
        if length == 0:
            return 1

        combinations = 0

        for i in range(1, length+1):
            if self.isValid(word[:i]):
                # If the prefix is valid get all suffix
                combinations += self.search(word[i:])

        return combinations

def linen(file):

    with open(file) as fIO:
        patterns = fIO.readline().strip().split(', ')
        fIO.readline() # Skip blank from input

        towels = Trie()

        print(f'{patterns=}')

        for pattern in patterns:
            towels.insert(pattern)

        valid_designs = 0
        valid_combinations = 0

        start = dt.datetime.now()

        for line in fIO.readlines():
            design = line.strip()

            combos = towels.search(design)
            print(f'{design=} {combos=}')

            if combos:
                valid_combinations += combos
                valid_designs += 1

        end = dt.datetime.now()
        print(f'{valid_designs=}, {valid_combinations=}, {end-start}')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str, required=True)
    args = parser.parse_args()

    linen(args.filename)
