#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy.random


def chap01_00(s):
    return s[::-1]


def chap01_01(s):
    return "".join([s[i-1] for i in [1, 3, 5, 7]])


def chap01_02(s1, s2):
    return "".join(list(map(lambda x: x[0]+x[1], zip(s1, s2))))


def chap01_03(s):
    return [len(z) for z in s.replace(',', '').replace('.', '').split(' ')]


def chap01_04(s):
    return {(x[0:1] if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19] else x[0:2]): i+1
            for i, x in enumerate(s.replace(',', '').replace('.', '').split(' '))}


def getCharBigram(s):
    return [x[0]+x[1] for x in zip(list(s)[:-1], list(s)[1:])]

def chap01_05(s):
    w_list = s.replace(',', '').replace('.', '').split(' ')
    w_bigram = [tuple(x) for x in zip(w_list[:-1], w_list[1:])]
    c_bigram = getCharBigram(s)
    return w_bigram, c_bigram


def chap01_06(s1, s2, s3):
    X = set(getCharBigram(s1))
    Y = set(getCharBigram(s2))
    return (X, Y, X.union(Y), X.intersection(Y), X.difference(Y), s3 in X, s3 in Y)


def chap01_07(s1, s2, s3):
    return "%s時の%sは%s" % (s1, s2, s3)


def cipher(s):
    return "".join([chr(219-ord(c)) if c.islower() else c
                    for c in s])


def chap01_08(s):
    return cipher(s)


def typoglycemia(w):
    if len(w) < 4:
        return w
    wsub = list(w[1:-1])
    numpy.random.shuffle(wsub)
    return "".join([w[0]] + wsub + [w[-1]])


def chap01_09(s):
    return " ".join([typoglycemia(w) for w in s.split(' ')])
