# -*- encoding:utf-8 -*-
import unittest
import os
import json
import deepseg_util


class DeepsegUtilTest(unittest.TestCase):
    def test_read_file_line(self):
        filename = 'tests/_test_read_file_line'
        with open(filename, 'w') as fh:
            for i in range(5):
                fh.write(str(i) + '\n')
            fh.close()

        line_no = 0
        for result in deepseg_util.read_file_line(filename):
            expect = str(line_no) + '\n'
            self.assertEqual(result, expect)

            line_no += 1

        os.remove(filename)

    def test_read_json(self):
        filename = 'tests/_test_read_json'
        expect = {'test': [1, 2, 3, 4, 5]}
        with open(filename, 'w') as fh:
            json.dump(expect, fh)

        result = deepseg_util.read_json(filename)
        self.assertEqual(result, expect)

        os.remove(filename)

    def test_tagDigitEn_digit(self):
        for w in deepseg_util.NUM_LIST:
            expect = u'$NUM$'
            result = deepseg_util.tagDigitEn(w)
            self.assertEqual(result, expect)
        for w in u'0123456789':
            expect = u'$NUM$'
            result = deepseg_util.tagDigitEn(w)
            self.assertEqual(result, expect)

    def test_tagDigitEn_alphabet(self):
        for w in deepseg_util.ENG_LIST:
            expect = u'$EN$'
            result = deepseg_util.tagDigitEn(w)
            self.assertEqual(result, expect)

        for w in u'abcdefghijklmnopqrstuvwxyz':
            expect = u'$EN$'
            result = deepseg_util.tagDigitEn(w)
            self.assertEqual(result, expect)

    def test_tagDigitEn_chinese(self):
        for w in u'功許蓋閱餐擺珮豹枯淚穀愧碁銹裏墻恒粧嫺兙兛兝兞':
            expect = w
            result = w
            self.assertEqual(expect, result)

    def test_get_widx(self):
        dict_ = {
            u'OOV': 0,
            u'$NUM$': 1,
            u'$EN$': 2,
            u'三': 3,
        }

        data = [(u'。', 0), (u'1', 1), (u'b', 2), (u'三', 3)]

        for w, expect in data:
            result = deepseg_util.get_widx(w, dict_)
            self.assertEqual(expect, result)
