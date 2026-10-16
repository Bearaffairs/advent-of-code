#!/usr/bin/env python3

import argparse
import datetime as dt

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

    def search(self, word):

        # First check if the entire word is valid
        if self.isValid(word):
            return True

        for i in range(len(word) - 1, 0, -1):
            # Try validate earlier sections of the word
            if self.isValid(word[:i]):
                # If the earlier prefix is valid, search the remainder for validity.
                if self.search(word[i:]):
                    return True
        return False

def linen(file):

    with open(file) as fIO:
        patterns = fIO.readline().strip().split(', ')
        fIO.readline() # Skip blank from input

        towels = Trie()

        for pattern in patterns:
            towels.insert(pattern)

        valid_designs = 0

        start = dt.datetime.now()

        for line in fIO.readlines():
            design = line.strip()

            valid = towels.search(design)
            print(f'{design=} {valid=}')

            if valid:
                valid_designs += 1

        end = dt.datetime.now()
        print(f'{valid_designs=}, {end-start}')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str, required=True)
    args = parser.parse_args()

    linen(args.filename)
