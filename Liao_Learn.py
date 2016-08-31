#coding = utf-8
'''
#1 输入和输出
#1.1
print('hello ,world')
#1.2
print(300)
print(100+200)
print('100 + 200 =',100+200)
'''

#2.Python基础
#2.1数据类型和变量
print('\n多行输出')
print('line1\nline2\nline3')	#多行输出
#多行输出另一种方式
print('''line4
line5
line6''')

#布尔值，只有True和False
print('\n布尔值')
print(3>2)
print(3>5)

#与运算 and
print('\n与运算')
print(True and True)
print(True and False)
print(False and False)
print(3>2 and 3>5)

#或运算 or
print('\n或运算')
print(True or True)
print(True or False)
print(3>5 or 3>8)

#非运算
print('\n非运算')
print(not True)
print(not False)
print(not 6==7)



'''
#3 函数
#3.1 调用函数
print('绝对值:',abs(-100))

#3.2 定义函数
def Func_sum(a,b):
	return (a + b)
	
print('Func_sum:',Func_sum(25,36))
'''