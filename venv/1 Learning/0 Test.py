#!/user/bin/python3.6
# _*_ coding=utf-8 _*_

# import pymongo
import random
# import socket

x = (1 + 1, 1 * 6, 2 ** 9, 10 / 4, 10 // 4, -10 // 4, 10 % 3, 10 % 4, pow(2, 6), abs(11 - 21), sum((1, 2, 3, 4)),
     min(1, 2, -1), max(1, 2, -1), bin(16), int(0b100000), oct(12), int(0o16), int(12), hex(255), int(0x1000), float(1),
     int(10.111), 1 > 1, 1 == 1, 1 != 1, 1 or 0 or 2, 1 and 0 and 3, not 1, not 0, 666 if 123 else 888,
     666 if 0 else 888, random.random(), random.randint(1, 99), random.choice((1, 'gzx', 16, 'cisco')))

print(x)
for y in x:
    print(y)
# print(dir(x))


