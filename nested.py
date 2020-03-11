#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Patrick Buzzo(Assistance from Jake Hershey and Piero's Demo)"

import sys

tokens_dict = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '*)': '(*'
}

token_list = sorted(tokens_dict.keys() +
                    tokens_dict.values(), key=len, reverse=True)


def is_nested(line):
    stack = []
    token_counter = 0
    while line:
        token = line[0]
        for t in token_list:
            if line.startswith(t):
                token = t
                break
        token_counter += 1
        line = line[len(token):]

        if token in tokens_dict.values():
            stack.append(token)
        elif token in tokens_dict.keys():
            expected_opener = tokens_dict[token]
            if stack.pop() != expected_opener:
                return 'NO ' + str(token_counter)
    if stack:
        return 'NO ' + str(token_counter)
    return 'YES'


def main(args):
    print('Testing for Nesting: {}'.format(args[0]))
    with open(args[0]) as ifile:
        with open('output.txt', 'w') as ofile:
            for line in ifile:
                result = is_nested(line)
                print(result)
                ofile.write(result + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
