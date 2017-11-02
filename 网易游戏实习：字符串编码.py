'''
[编程题] 字符串编码
时间限制：1秒
空间限制：32768K
给定一个字符串，请你将字符串重新编码，将连续的字符替换成“连续出现的个数+字符”。
比如字符串AAAABCCDAA会被编码成4A1B2C1D2A。 
输入描述:
每个测试输入包含1个测试用例
每个测试用例输入只有一行字符串，字符串只包括大写英文字母，长度不超过10000。


输出描述:
输出编码后的字符串

输入例子1:
AAAABCCDAA

输出例子1:
4A1B2C1D2A
'''

'''
解题思路：仔细小心
  这道题思路不难，看代码应该可以理解我的思路，但在解题的时候不要马虎，一不小心就会错
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

string = input().strip()

length = len(string)
temp = -1
results = ''
for i in range(0, length-1):
    if string[i] == string[i+1]:
        continue
    else:
        results += str(i-temp) + string[i]
        temp = i
results += str(length-1-temp) + string[length-1]

print(results)
