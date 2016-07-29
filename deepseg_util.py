# -*- encoding:utf-8 -*-
import json
import re
import logging


NUM_LIST = [
    u"０", u"１", u"２", u"３", u"４", u"５", u"６", u"７", u"８", u"９"
]

ENG_LIST = [
    u"Ａ", u"Ｂ", u"Ｃ", u"Ｄ", u"Ｅ", u"Ｆ", u"Ｇ", u"Ｈ", u"Ｉ", u"Ｊ",
    u"Ｋ", u"Ｌ", u"Ｍ", u"Ｎ", u"Ｏ", u"Ｐ", u"Ｑ", u"Ｒ", u"Ｓ", u"Ｔ",
    u"Ｕ", u"Ｖ", u"Ｗ", u"Ｘ", u"Ｙ", u"Ｚ", u"ａ", u"ｂ", u"ｃ", u"ｄ",
    u"ｅ", u"ｆ", u"ｇ", u"ｈ", u"ｉ", u"ｊ", u"ｋ", u"ｌ", u"ｍ", u"ｎ",
    u"ｏ", u"ｐ", u"ｑ", u"ｒ", u"ｓ", u"ｔ", u"ｕ", u"ｖ", u"ｗ", u"ｘ",
    u"ｙ", u"ｚ"
]


def read_file_line(fname, toprint=False):
    f = open(fname, "r")
    i = 0
    while True:
        line = f.readline()
        i += 1
        if toprint:
            print(i)
        if len(line) == 0:
            break
        yield line
    f.close()


def read_json(json_fname):
    f = open(json_fname, "r")
    json_item = json.loads("".join(f.readlines()))
    f.close()
    return json_item


def tagDigitEn(w):
    if w.isdigit() or w in NUM_LIST:
        return u"$NUM$"
    elif len(re.findall(r"[A-Za-z]", w)) > 0 or w in ENG_LIST:
        return u"$EN$"
    else:
        return w


def get_widx(w, word_dict):
    w_idx = word_dict.get(tagDigitEn(w), -1)
    if w_idx != -1:
        return w_idx
    else:
        return word_dict.get("OOV")
