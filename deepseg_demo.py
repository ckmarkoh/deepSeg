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
