# -*- coding: utf-8 -*-
# author：albert time:2020/4/23
s = 'abcdefg'
n = 2
for y in range(len(s)):
    if y == n:
        x = s[y:] + s[0:y]
        print(x)