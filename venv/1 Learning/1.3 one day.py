#!/user/bin/python3.68
# _*_ coding=utf-8  _*_

import re

str1 = 'Port-channel1.189    192.168.1.100    YES    CONFIG  UP UP'
a1 = 'interface:'
a2 = 'IP:'
a3 = 'admin state:'
a4 = 'Physical state:'

result = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s+(\w*).*',str1).groups()
# result = re.match('\s*[0-9a-zA-Z\-\.]+\s\d+[0-9\-\.]+\s+\（d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}）\s+(YES|NO)\s+(CONFIG|DHCP).*',str1)

# str1 = 'Port-channel1.189--192.168.1.100--YES--CONFIG--UP--UP==192.168.1.1'
# result = str1.split('--')   #默认（）分隔符为空格,对于有规律的 可以用（）识别出分隔符来提取数据。
# result = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',str1) #找到这个字符串中的所有可以匹配的。
# result = re.sub('--','??',str1) #替换
l1 = f'{a1:>15} {result[0]}'
l2 = f'{a2:>15} {result[1]}'
l3 = f'{a3:>15} {result[4]}'
l4 = f'{a4:>15} {result[5]}'

print('='*80)
print(result)
print('='*80)
# 方法1
print(l1)
print(l2)
print(l3)
print(l4)
print('='*80)
# 方法2
# print('%-6s : %s' % ('接口', result[0]))
# print('%-6s : %s' % ('IP地址', result[1]))
# print('%-6s : %s' % ('管理状态', result[4]))