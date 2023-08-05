# -*- coding: utf-8 -*-
from 臺灣言語工具.語音合成.決策樹仔問題.公家決策樹仔 import 公家決策樹仔
from 臺灣言語工具.語音合成.生決策樹仔問題 import 生決策樹仔問題
import itertools
import os
from 臺灣言語工具.音標系統.SaySiyat.賽夏 import 賽夏


class 賽夏決策樹仔(公家決策樹仔):
    聲韻符號 = ('', '-', '+', '/調:')
    調符號 = ('/調:', '<', '>', '/詞:')
    詞符號 = ('/詞:', '!', '@', '/句:')
    句符號 = ('/句:', '^', '_', '')

    @classmethod
    def 生(cls, 輸出目的=open(os.devnull, 'w')):
        問題 = set()
        問題 |= cls.孤聲韻()
        print(len(問題), file=輸出目的)
        問題 |= cls.組合()
        print(len(問題), file=輸出目的)
        問題 |= cls.詞句長度(10, 20)
        print(len(問題), file=輸出目的)
        問題 |= cls.孤雙數音節()
        print(len(問題), file=輸出目的)

        生決策樹仔問題.檢查(問題)
        return 問題

    @classmethod
    def 孤聲韻(cls):
        聲韻 = []
        for 實際音 in itertools.chain(
                ['sil', 'sp'],
                賽夏.國際音標對照表.values(),
        ):
            聲韻.append(('{0}'.format(實際音), [實際音]))
        return 生決策樹仔問題.問題集(聲韻, cls.聲韻符號, '孤條')

    @classmethod
    def 組合(cls):
        仝元音題目 = [
            ('a音', ['a', 'aː', ]),
            ('i音', ['i', 'iː', ]),
            ('u音', ['u', 'uː', ]),
            ('o音', ['o', 'oː', ]),
            ('œ音', ['œ', 'œː', ]),
            ('æ音', ['æ', 'æː', ]),
        ]
        長短元音題目 = [
            ('短音', ['a', 'i', 'u', 'o', 'œ', 'æ', ]),
            ('長音', ['aː', 'iː', 'uː', 'oː', 'əː', 'œ:', 'æ:', ]),
        ]
        滑音題目 = [
            ('ji音', ['j', 'i', 'iː', ]),
            ('wu音', ['w', 'u', 'uː', ]),
        ]
        發音方法 = [
            ('鼻音', ['m', 'n', 'ŋ', ]),
            ('塞音', ['p', 't', 'k', 'ʔ', ]),
            ('擦音', ['β', 's', 'z', 'x', 'ʃ', ]),
        ]
        發音所在 = [
            ('唇輔音', ['p', 'm', 'β']),
            ('舌尖輔音', ['t', 'n', 'l', 'r', 's', 'z', 'ʃ', ]),
            ('舌根輔音', ['k', 'ŋ', 'h', ]),
            # ('喉輔音', ['ʔ', ]),
        ]
        return (
            生決策樹仔問題.問題集(仝元音題目, cls.聲韻符號, '孤條') |
            生決策樹仔問題.問題集(長短元音題目, cls.聲韻符號, '孤條') |
            生決策樹仔問題.問題集(滑音題目, cls.聲韻符號, '孤條') |
            生決策樹仔問題.問題集(發音方法, cls.聲韻符號, '孤條') |
            生決策樹仔問題.問題集(發音所在, cls.聲韻符號, '孤條')
        )
