#!/usr/bin/env python3
from fontTools.ttLib import TTCollection
import fileinput
from opencc import OpenCC

ttc_path = '/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc'
ttc = TTCollection(ttc_path)
# 你可以更改 fontNumber 的数字来切换不同的字体，比如斜体、粗体等
font = ttc.fonts[2] # SC
# 4. 获取支持的 Glyph 列表
# cmap 表保存着从字符码（Unicode）到 Glyph 索引 / 名称的映射关系
cmap = font.getBestCmap()

noto = set()
# 获取字符到 glyph 名的映射
for i in cmap.keys():
    noto.add(chr(i))

# opencc
configs = "hk2s hk2t s2hk s2t s2tw t2hk t2s t2tw tw2s tw2t"
ccs = list()
for i in configs.split(" "):
    ccs.append(OpenCC(i))
chars = set()
for line in fileinput.input():
    line = line.strip()
    chars.update(set(line))
    for cc in ccs:
        tmp = cc.convert(line)
        chars.update(set(tmp))
chars.remove("\ufe0f")
txt = "".join(sorted(chars-noto))
open("missing.txt", "w", encoding="U8").write(txt)
content = open("template.html").read().replace("__MISSING__", txt)
open("docs/index.html", "w", encoding="U8").write(content)
