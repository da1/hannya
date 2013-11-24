# -*- coding: utf-8 -*-
import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")

from modules import hannya

class HannyaTests(unittest.TestCase):
    def testHasHannya(self):
        test_case = [
                { "text" : u'ほげ'  , "resultBool" : False , "resultWord" : "" },
                { "text" : u'般若'  , "resultBool" : False , "resultWord" : "" },
                { "text" : u'空あり' , "resultBool" : True , "resultWord" : u"空" },
                { "text" : u"経典"  , "resultBool" : True  , "resultWord" : u"経" },
                ]
        for case in test_case:
            word, result = hannya.hasHannya(case["text"])
            self.assertEqual(result, case["resultBool"])
            self.assertEqual(word, case["resultWord"])

    def testHannyaFilter(self):
        result = hannya.hannyaFilter([u'ほげ', u'般若', u'空あり', u"経典"])
        self.assertEqual(len(result), 2)

        self.assertEqual(result[0][0], u"空")
        self.assertEqual(result[0][1], u"空あり")

        self.assertEqual(result[1][0], u"経")
        self.assertEqual(result[1][1], u"経典")

if __name__ == '__main__':
    unittest.main()
