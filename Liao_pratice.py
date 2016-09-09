# -*- coding: utf-8 -*-
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


#2.2字符串和编码
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
'''
s1 = 72
s2 = 85
r = (s2 - s1)/s1*100
print('%5.2f'%r)
print('add =',r)
'''

'''
#2.3 list和tuple
#请用索引取出下面list的指定元素：
# -*- coding: utf-8 -*-
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

#参考代码
classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
'''
'''
#2.3条件判断

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''

height = 1.75
weight = 80.5

bmi = weight/(height*height)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
	print('正常')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')
	
#2.4循环






print('\n************************************************************************')
