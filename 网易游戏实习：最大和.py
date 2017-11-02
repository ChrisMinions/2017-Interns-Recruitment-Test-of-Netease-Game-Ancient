'''
[编程题] 最大和
时间限制：1秒
空间限制：32768K
在一个N*N的数组中寻找所有横，竖，左上到右下，右上到左下，四种方向的直线连续D个数字的和里面最大的值 
输入描述:
每个测试输入包含1个测试用例，第一行包括两个整数 N 和 D :
3 <= N <= 100
1 <= D <= N
接下来有N行，每行N个数字d:
0 <= d <= 100


输出描述:
输出一个整数，表示找到的和的最大值

输入例子1:
4 2
87 98 79 61
10 27 95 70
20 64 73 29
71 65 15 0

输出例子1:
193
'''

'''
解题思路：遍历所有D*D大小的区域 并超出其中的符合条件的最大值
  1、找到D*D大小的区域
  2、计算出横，竖，左上到右下，右上到左下，四种方向的直线连续D个数字的和里面最大的值返回
  3、遍历D*D大小的所有区域，在这些最大值中找出最大的值
  
  这一次又超时了，模仿神经网络中的池化，可以尝试下窗函数遍历的思路，看能不能省点内存和时间
'''

'''
代码运行结果：
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为98.00%
'''

N, D = [each for each in map(int, input().split())]

nums_array = []
for i in range(N):
    nums_array.append([each for each in map(int, input().split())])


def get_max(slice_array):
    max_horizontal = max([sum(temp) for temp in slice_array])
    max_vertical = max([sum([temp[j_] for temp in slice_array]) for j_ in range(D)])
    max_lt2rb = 0
    max_rt2lb = 0
    for x_ in range(D):
        for y_ in range(D):
            if x_ == y_:
                max_lt2rb += slice_array[x_][y_]
            if x_ + y_ == D - 1:
                max_rt2lb += slice_array[x_][y_]
    return max(max_horizontal, max_vertical, max_lt2rb, max_rt2lb)

maximum = 0
for i in range(N-D+1):
    for j in range(N-D+1):
        temp_slice = [each_row[j:j+D] for each_row in nums_array[i:i+D]]
        temp_slice_maximum = get_max(temp_slice)
        if maximum < temp_slice_maximum:
            maximum = temp_slice_maximum

print(maximum)

'''
4 2
87 98 79 61
10 27 95 70
20 64 73 29
71 65 15 0
'''