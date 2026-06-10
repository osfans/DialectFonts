#!/usr/bin/env python3
from fontTools.subset import main as subset_main

# 通过命令行参数的方式提取子集，保留特定字符（如 "Hello"）
for i in "12":
    subset_args = [
        f'PlangothicP{i}-Regular.woff2',
        '--text-file=missing.txt',
        f'--output-file=docs/p{i}.woff2',
        '--no-subset-tables+=FFTM'
    ]
    subset_main(subset_args)
