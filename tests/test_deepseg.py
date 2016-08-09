# -*- encoding:utf-8 -*-
import unittest
from deepseg import DeepSeg


class DeepsegTest(unittest.TestCase):
    def test_cut(self):
        doc_in = u'中文詞彙網路是建立在英語詞彙網路的理論架構之上所建構的計算心理詞庫。'

        expect = [u'中文', u'詞彙', u'網路', u'是', u'建立', u'在', u'英語', u'詞彙', u'網路', u'的', u'理論', u'架構', u'之上', u'所', u'建構', u'的', u'計算', u'心理', u'詞庫', u'。', u'\n', ]

        ds = DeepSeg()
        result = ds.cut(doc_in)
        self.assertEqual(result, expect)

    def test_word_segmentation(self):
        doc_in = [u'中文詞彙網路是建立在英語詞彙網路的理論架構之上所建構的計算心理詞庫。']

        expect = [u'中文', u'詞彙', u'網路', u'是', u'建立', u'在', u'英語', u'詞彙', u'網路', u'的', u'理論', u'架構', u'之上', u'所', u'建構', u'的', u'計算', u'心理', u'詞庫', u'。', u'\n', ]

        ds = DeepSeg()
        result = ds.word_segmentation(doc_in)
        self.assertEqual(result, expect)
