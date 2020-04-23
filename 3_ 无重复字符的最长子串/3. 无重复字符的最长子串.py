# -*- coding: utf-8 -*-
# author：albert time:2020/4/23

s = "pwwkewd"
x = []
z = []
for y in s:
    if y in z:
        p = z.index(y)
        x.append(len(z))
        z = z[p+1:]
    z.append(y)
    # print(y)
    # print(z)
    # print(z.index(y))
    x.append(len(z))
if len(x) == 0:
    print(0)
else:
    l = max(x)
    print(l)

