#coding = utf-8
print('\n***************************** Hello Python *****************************\n')

#print('1024 * 768 =',1024*768)
#2.Python基础
#2.1数据类型和变量
#请打印出以下变量的值：

'''
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'

'''

'''
n = 123
print('n =', n)
f = 456.789
print('f =', f)
s1 = 'Hello,world'
print('s1 =', s1)
s2 = 'Hello,\\\'Adam\\\''
print('s2 =',s2)
s3 = 'Hello, "Bart"'
print('s3 =', 'Hello，"Bart"')
print(r'Hello,"Bart"')
'''
#print(r'''Hello,
#Lisa!''')
#print('\'\'\'Hello,\nLisa!\'\'\'')


#字符串和编码
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

s1 = 72
s2 = 85

r = (s2 - s1)/s1*100

print('%5.2f\n'%r)










print('\n************************************************************************')
