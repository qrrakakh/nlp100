#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import os
import subprocess
import unittest
import chap02


class TestChap02(unittest.TestCase):
    data = "./data/hightemp.txt"

    @staticmethod
    def getMD5sum(infile):
        try:
            with open(infile, 'rb') as rh:
                return hashlib.md5(rh.read()).hexdigest()
        except Exception as e:
            return None


    def test_10(self):
        self.assertEqual(chap02.chap02_10(self.data),
                         int(subprocess.check_output(["wc","-l", self.data]).decode('utf-8').split(' ')[0]))


    def test_11(self):
        self.assertEqual(chap02.chap02_11(self.data),
                         subprocess.check_output(["expand", "-t", "1", self.data]).decode('utf-8'))


    def test_12(self):
        col1_ans = "./temp/col1.txt"
        col2_ans = "./temp/col2.txt"
        col1_expect = "./temp/_col1.txt"
        col2_expect = "./temp/_col2.txt"
        
        chap02.chap02_12(self.data, col1_ans, 1)
        self.assertTrue(os.path.exists(col1_ans))

        chap02.chap02_12(self.data, col2_ans, 2)
        self.assertTrue(os.path.exists(col2_ans))

        with open(col1_expect, 'wb') as wh:
            wh.write(subprocess.check_output(["cut", "-f", "1", self.data]))
        self.assertTrue(os.path.exists(col1_expect))
        with open(col2_expect, 'wb') as wh:
            wh.write(subprocess.check_output(["cut", "-f", "2", self.data]))
        self.assertTrue(os.path.exists(col2_expect))

        self.assertEqual(self.getMD5sum(col1_ans), self.getMD5sum(col1_expect))
        self.assertEqual(self.getMD5sum(col2_ans), self.getMD5sum(col2_expect))

        if os.path.exists(col1_ans):
            os.remove(col1_ans)
        if os.path.exists(col2_ans):
            os.remove(col2_ans)
        if os.path.exists(col1_expect):
            os.remove(col1_expect)
        if os.path.exists(col2_expect):
            os.remove(col2_expect)
        

    def test_13(self):
        col1_infile = "./temp/col1.txt"
        col2_infile = "./temp/col2.txt"
        ansfile = "./temp/merged.txt"
        expectfile = "./temp/_merged.txt"
        
        chap02.chap02_12(self.data, col1_infile, 1)
        self.assertTrue(os.path.exists(col1_infile))

        chap02.chap02_12(self.data, col2_infile, 2)
        self.assertTrue(os.path.exists(col2_infile))

        chap02.chap02_13(col1_infile, col2_infile, ansfile)
        self.assertTrue(os.path.exists(ansfile))

        with open(expectfile, 'wb') as wh:
            wh.write(subprocess.check_output(["paste", col1_infile, col2_infile]))
        self.assertTrue(os.path.exists(expectfile))

        self.assertEqual(self.getMD5sum(ansfile), self.getMD5sum(expectfile))
        
        if os.path.exists(col1_infile):
            os.remove(col1_infile)
        if os.path.exists(col2_infile):
            os.remove(col2_infile)
        if os.path.exists(ansfile):
            os.remove(ansfile)
        if os.path.exists(expectfile):
            os.remove(expectfile)


    def test_14(self):
        self.assertEqual(chap02.chap02_14(None), "")


    def test_15(self):
        self.assertEqual(chap02.chap02_15(None), "")


    def test_16(self):
        self.assertEqual(chap02.chap02_16(None), "")


    def test_17(self):
        self.assertEqual(chap02.chap02_17(None), "")


    def test_18(self):
        self.assertEqual(chap02.chap02_18(None), "")


    def test_19(self):
        self.assertEqual(chap02.chap02_19(None), "")
