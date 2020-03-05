#!/user/bin/python3.6
# _*_ coding=utf-8 _*_

#!/user/bin/python3.68
# _*_ coding=utf-8  _*_

# import

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
CORSE_FEES_SEC = 456789.12345
CORSE_FEES_Python = 1234.4567

# 方法1 F'{} + {} + {}
line1 = f'Department1 name:{department1:10} Manager:{depart1_m:10}   CORSE FEES:{CORSE_FEES_SEC:<10.2f} The End!'
line2 = f'Department2 name:{department2:10} Manager:{depart2_m:10}   CORSE FEES:{CORSE_FEES_Python:<10.2f} The End!'

# 方法2 F'{} + {} + {}
# line1 =
# line2 =

length = len(line1)
print('='*80)
print(line1)
print(line2)
print('='*80)
