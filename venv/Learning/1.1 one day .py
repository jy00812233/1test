#!/user/bin/python3.6
# _*_ coding=utf-8 _*_

import random #导入数学模块

#随机生成四组数值
a1=random.randint(1,255)
a2=random.randint(1,255)
a3=random.randint(1,255)
a4=random.randint(1,255)

#数字转换成字符串，拼接在一起。
random_ip = str(a1)+'.'+str(a2)+'.'+str(a3)+'.'+str(a4)

#打印结果
print(random_ip)
