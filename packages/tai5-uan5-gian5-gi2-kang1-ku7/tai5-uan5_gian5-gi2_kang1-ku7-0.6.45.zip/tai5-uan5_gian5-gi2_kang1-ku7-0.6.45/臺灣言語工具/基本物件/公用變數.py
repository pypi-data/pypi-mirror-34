# -*- coding: utf-8 -*-
# 瀏覽器希望無音愛有空白，但是處理標音時希望是佮好認的
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音調類對照表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組 import 臺灣閩南語羅馬字拼音對照吳守禮方音聲調表
import unicodedata


無音 = ''  # '　'
# sui1 koo1-niu5 =>　媠　姑娘
分字符號 = '-'
分詞符號 = ' '
分型音符號 = '｜'
# a2-bing5 # bo5 tsiah8 png7 代表 bing5 無變調
本調符號 = '#'
輕聲符號 = '--'
# 句中是為著加速標音
句中標點符號 = {
    '、', '﹑', '､', '-', '—', '~', '～',
    '·', '‧',  # 外國人名中間
    '＇', '"', '‘', '’', '“', '”', '〝', '〞', '′', '‵',
    '「', '」', '｢', '｣', '『', '』',
    '【', '】', '〈', '〉', '《', '》', '（', '）', '＜', '＞', '(', ')',
    '+', '*', '/', '=', '^', '＋', '－', '＊', '／', '＝', '$', '#', '#',
    ':', '：', '﹕', '–', '—', '―', '─', '｜', '︱',
    '•',
}

# 斷句是考慮著翻譯，閣有語音合成愛做的正規化
斷句標點符號 = (
    {'\n', } |
    {'，', '。', '．', '！', '？', '…', '……', '...', } |
    {',', '.', '!', '?', } |
    {'﹐', '﹒', '﹗', '﹖', } |
    {';', '；', '﹔', }
)

聲調符號 = (
    臺灣客家話拼音調類對照表 |
    set(臺灣閩南語羅馬字拼音對照吳守禮方音聲調表.values())
) - {''}


標點符號 = 句中標點符號 | 斷句標點符號

組字式符號 = '⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻⿿'

# Ll　小寫， Lu　大寫， Md　數字， Mn　有調號英文，Lo　其他, So 組字式符號…
_統一碼羅馬字類 = {'Ll', 'Lu', 'Mn'}


def 敢是拼音字元(字元):
    try:
        種類 = unicodedata.category(字元)
    except TypeError:
        return False
    return 種類 in _統一碼羅馬字類 or 字元 in ['ⁿ', "'", '_', ]


def 敢是注音符號(字元):
    return unicodedata.name(字元, '').startswith('BOPOMOFO LETTER')
