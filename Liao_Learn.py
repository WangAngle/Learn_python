#coding = utf-8
'''
#1 输入和输出
#1.1
print('\n***************************输入和输出**********************\n')
print('Hello ,Python')
#1.2
print(300)
print(100+200)
print('100 + 200 =',100+200)
'''

'''
#2.Python基础
#2.1数据类型和变量
print('\n*****************************数据类型和变量*************************\n')
print('多行输出')
print('line1\nline2\nline3')	#多行输出
'''
#多行输出另一种方式
#print('''line4
#line5
#line6''')

'''
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

print('\n********************************变量和常量************************\n')
#变量
a = 1
print(a)
a = 'ABC'
print(a)

#常量
PI = 3.14159265359
print(PI)
print('10/3  = ',10/3)
print('9/3   = ',9/3)
print('10//3 = ',10//3)
print('10%3  = ',10%3)
'''

#2.2 字符串和编码
'''
print('\n*********************************格式化输出***********************\n')
money = 100
name = 'wang'
print('Hello %s,you have $%d.\n' % (name,money))
'''

#2.3 list和tuple
'''
print('\n*********************************list和tuple***********************\n')
classmates = ['wang', 'li_hong', 'name']
print(classmates)
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
'''
'''
print('\n*********************************list***********************\n')
classmates = ['wang', 'li_hong', 'name']
print(classmates)
classmates.append('now')
print(classmates)
classmates.insert(2,'jhon')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
classmates[2] = 'cherry'
print(classmates,)
'''

print('\n*********************************list***********************\n')
list = ['angle',100,0x13]
print(list)
list = ['angle',['cherry','black'],'crow']
print(list)
print('list_len = %d'%len(list))









'''
#3 函数
#3.1 调用函数
print('绝对值:',abs(-100))

#3.2 定义函数
def Func_sum(a,b):
	return (a + b)
	
print('Func_sum:',Func_sum(25,36))
'''
