# deepSeg

[![Build Status](https://travis-ci.org/ckmarkoh/deepSeg.svg?branch=master)](https://travis-ci.org/ckmarkoh/deepSeg)
[![codecov](https://codecov.io/gh/ckmarkoh/deepSeg/branch/master/graph/badge.svg)](https://codecov.io/gh/ckmarkoh/deepSeg)

A deep learning Chinese Word Segmentation toolkit

# Usage

code example:

```
# -*- encoding:utf-8 -*-
from deepseg import DeepSeg


doc_in = u"""
中文詞彙網路是建立在英語詞彙網路的理論架構之上所建構的計算心理詞庫。
詞彙依其同義行為聚集成「同義詞集」，
而同義詞集在依不同的語義關係彼此連接成為一個複雜的詞彙網路。
"""

ds = DeepSeg()
deep_seg_list = ds.cut(doc_in)
print("  ".join(deep_seg_list))

```

output:

```

  中文  詞彙  網路  是  建立  在  英語  詞彙  網路  的  理論  架構  之上  所  建構  的  計算  心理  詞庫  。
  詞彙  依  其  同義  行為  聚集成  「  同義詞集  」  ，
  而  同義詞集  在  依  不同  的  語義  關係  彼此  連接  成為  一  個  複雜  的  詞彙  網路  。


```

# Run Tests

```
python -m unittest tests.test_deepseg.DeepsegTest
python -m unittest tests.test_deepseg_util.DeepsegUtilTest
```

# Check PEP8

```
pep8 *.py --ignore=E501
pep8 tests/*.py --ignore=E501
```
