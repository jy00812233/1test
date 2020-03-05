#!/user/bin/python3.6
# _*_ coding=utf-8 _*_
-------------------------------------------------------------------------------------
第一天
    表达式操作符： + - * /除法 //Floor除法 %除法余数 >> <<二进制移位 **乘方 etc
    内建数学函数： Pow乘方 abs绝对值 round四舍五入 int十进制 hex十六进制 oct八进制 bin etc
    工具模块：

-------------------------------------------------------------------------------------


>>> x=0b10
>>> print(type(x))  #打印变量类型。一种打印使用方式。

# print(1+1)
# print('1'+'a')
# x = 3+3
# print('jieshao'+str(x)+'end')  #不能转换整数对象到字符串对象，str指定x赋值的结果为字符串.用途：将一个公式的变量带入转换成字符串。

# myname = 'gaozhixiong'  #字符串特性1：序列。可实现索引和切片。
# print(myname[0:3],myname[:-5],myname[3:-5],myname[0],myname[3],myname[6])

# myname = 'gaozhixiong'  #字符串特性2：不可修改。可以通过字符串拼接修改。
# # myname[3] = Z         #运行会报错
# newname = myname[:1] + 'Z' + myname[6:7]
# print(newname)          #通过上面拼接 达到了修改字符串的目的。

#myname = 'gaozhixiong'
#'a1' in myname    #判断字符串中是否含有该字符

# myname = 'gaozhixiong'
# for x in myname: #for 一个一个取出来。字符串是序列类型，x是个变量的名字，每次顺取字符串一位赋值给x，循环打印。
#     print (x)    #默认print 一个结果后换行。

# myname = 'gaozhixiong'
# for x in myname:
#     print (x,end='')  #默认print之后自动换行。end=''修改打印后''的动作。

# a = 'ABC'
# # print (dir(a))  #打印内建函数，这里就是打印字符串有的使用方法。https://www.runoob.com/python/python-strings.html
# newa = a.lower()  #其中一个使用方法，小写。test.upper() 大写
# newa
#
# a = 'ABC'
# newa = a.replace('B','x').replace('C','')  #替换，新的变量。
# print(a)
# print(newa)

# a = '\n\tASDFASDA\n\r\t'  # 得到一段值，strip剔除两边空白，rstrip,lstrip.左右不分。
# a
# a.strip()

# #字符串转换成列表
# a = 'newa'
# newlist = list(a)
# newlist
# #列表特性1序列，特性2可修改。
# newlist[3] = 'bb'
# #列表转成字符串
# ''.join(newlist)

## ------------------------------------------------------------------
#字符串格式化表达式老方法1，效果使输出行列有对齐的效果。美观。
# 'you name %d %s %-10.2f' %  (123,'zx',1.123456)
# 'you name 123 zx 1.12      '

# 'you name %d %s %011.2f' %  (123,'zx',1.123456)
# 'you name 123 zx 00000001.12'
# %d%s -左对齐 0补零 10位 .2小数位 d s f字符串格式化类型代码， 单符号%分割，左边为公式，右边为条件。
# ------------------------------------------------------------------
#字符串格式化方法 方法2
# >>> tmp = '{0},{1}and{2}'
# 第一行模板
# >>> tmp.format('sec','python','123')
# 'sec,pythonand123'
# ------------------------------------------------------------------
#字符串格式化新方法3
# department1 = 'Python'
# depart1_m = 'cq_bomb'
# CORSE_FEES_SEC = 456789.12345
# # 方法1 F'{} + {} + {} <>^对齐方式
# line1 = f'Department1 name:{department1:10} Manager:{depart1_m:10}   CORSE FEES:{CORSE_FEES_SEC:<10.2f} The End!'
# print(line1)

# 格式2，格式更紧凑。
# '{0:f}+{1:.2f}+{2:06.2f}'.format(3.14159,3.14159,3.14159)
# '3.141590+3.14+003.14'
# ------------------------------------------------------------------

# 第二天
# 第五部分列表与字典








# 常用快捷键
# ctrl + /  快速注释
# ctrl + D  复制一行
# ctrl + Y  删除当前行
# ctrl + F  查找
# ctrl + R  替换
# ctrl + W  扩大选择范围
# ctrl + -+ 折叠展开代码块
# ctrl + 鼠标左键 放上查找更多参数  例如 socket
# Tab 批量缩进
# Shift + Tab 取消缩进
# Shift + Enter 快速换行，不必切到行尾。
# ctrl + Shift + F10 运行当前文件
# ALT + 鼠标左键 选择一列 可以替换一列
