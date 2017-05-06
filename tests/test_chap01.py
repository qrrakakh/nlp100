#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import chap01


class TestChap01(unittest.TestCase):


    def test_00(self):
        self.assertEqual(chap01.chap01_00("stressed"), "desserts")


    def test_01(self):
        self.assertEqual(chap01.chap01_01("パタトクカシーー"), "パトカー")
    

    def test_02(self):
        self.assertEqual(chap01.chap01_02("パトカー", "タクシー"), "パタトクカシーー")


    def test_03(self):
        test_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        self.assertListEqual(chap01.chap01_03(test_str),
                             [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8 ,9, 7, 9])

    def test_04(self):
        test_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
        expected = {a: i+1
                    for i, a in enumerate(["H", "He",
                                           "Li", "Be", "B", "C", "N", "O", "F", "Ne",
                                           "Na", "Mi", "Al", "Si", "P", "S", "Cl", "Ar",
                                           "K", "Ca"])}
        self.assertDictEqual(chap01.chap01_04(test_str), expected)

    def test_05(self):
        test_str = "I am an NLPer"
        w_bigram, c_bigram = chap01.chap01_05(test_str)
        self.assertListEqual(w_bigram, [("I", "am"), ("am", "an"), ("an", "NLPer")])
        self.assertListEqual(c_bigram, ["I ", " a", "am", "m ", " a", "an", "n ", " N", "NL","LP", "Pe", "er"])

    def test_06(self):
        X = set(["pa", "ar", "ra", "ap", "ad", "di", "is", "se"])
        Y = set(["pa", "ar", "ra", "ag", "gr", "ap", "ph"])
        XuY = X.union(Y)
        XiY = X.intersection(Y)
        XdY = X.difference(Y)
        flg1 = "se" in X
        flg2 = "se" in Y
        ans = chap01.chap01_06("paraparaparadise", "paragraph", "se")
        self.assertSetEqual(ans[0], X)
        self.assertSetEqual(ans[1], Y)
        self.assertSetEqual(ans[2], XuY)
        self.assertSetEqual(ans[3], XiY)
        self.assertSetEqual(ans[4], XdY)
        self.assertEqual(ans[5], flg1)
        self.assertEqual(ans[6], flg2)


    def test_07(self):
        self.assertEqual(chap01.chap01_07(12, "気温", 22.4), "12時の気温は22.4")



    def test_08(self):
        test_str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
        expected = "I xlfowm'g yvorvev gszg I xlfow zxgfzoob fmwvihgzmw dszg I dzh ivzwrmt : gsv ksvmlnvmzo kldvi lu gsv sfnzm nrmw ."
        self.assertEqual(chap01.chap01_08(test_str), expected)

    def test_09(self):
        test_str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
        ans = chap01.chap01_09(test_str)
        self.assertNotEqual(test_str, ans)
        self.assertListEqual(list(map(lambda x: sorted(x), test_str.split(' '))),
                             list(map(lambda x: sorted(x), ans.split(' '))))
