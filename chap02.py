#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def chap02_10(infile):
    with open(infile, 'r') as rh:
        return len([s for s in rh])


def chap02_11(infile):
    with open(infile, 'r') as rh:
        return "".join([str(re.sub(r"\t", " ", s)) for s in rh])


def chap02_12(infile, outfile, rnum):
    with open(infile, 'r') as rh, open(outfile, 'w') as wh:
        for line in rh:
            try:
                wh.write(line.split('\t')[rnum-1] + "\n")
            except Exception as e:
                return None
    return


def chap02_13(infile1, infile2, outfile):
    with open(infile1, 'r') as rh1, open(infile2, 'r') as rh2, open(outfile, 'w') as wh:
        line1, line2 = rh1.readline(), rh2.readline()
        while line1 and line2:
            wh.write("\t".join([line1.rstrip(), line2.rstrip()]) + "\n")
            line1, line2 = rh1.readline(), rh2.readline()
    return


def chap02_14(infile, n):
    with open(infile, 'r') as rh:
        return "".join([rh.readline() for i in range(n)])


def chap02_15(infile, n):
    with open(infile, 'r') as rh:
        return "".join(rh.readlines()[-n:])


def chap02_16(s):
    pass


def chap02_17(s):
    pass


def chap02_18(s):
    pass


def chap02_19(s):
    pass
