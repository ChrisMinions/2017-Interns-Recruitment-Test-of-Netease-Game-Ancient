'''
[编程题] 推箱子
时间限制：1秒
空间限制：32768K
大家一定玩过“推箱子”这个经典的游戏。具体规则就是在一个N*M的地图上，
有1个玩家、1个箱子、1个目的地以及若干障碍，其余是空地。玩家可以往上下左右4个方向移动，
但是不能移动出地图或者移动到障碍里去。如果往这个方向移动推到了箱子，箱子也会按这个方向移动一格，
当然，箱子也不能被推出地图或推到障碍里。当箱子被推到目的地以后，游戏目标达成。
现在告诉你游戏开始是初始的地图布局，请你求出玩家最少需要移动多少步才能够将游戏目标达成。 
输入描述:
每个测试输入包含1个测试用例
第一行输入两个数字N，M表示地图的大小。其中0<N，M<=8。
接下来有N行，每行包含M个字符表示该行地图。其中 . 表示空地、X表示玩家、*表示箱子、#表示障碍、@表示目的地。
每个地图必定包含1个玩家、1个箱子、1个目的地。


输出描述:
输出一个数字表示玩家最少需要移动多少步才能将游戏目标达成。当无论如何达成不了的时候，输出-1。

输入例子1:
4 4
....
..*@
....
.X..
6 6
...#..
......
#*##..
..##.#
..X...
.@#...

输出例子1:
3
11
'''

'''
解题思路：深度优先搜索算法（bfs）
  搜索前须知：
    用一个四元元组（br, bc, hr, hc）跟踪搜索过程中box_row, box_column, human_row, human_column
    一个集合searched{}记录已经搜索过的区域
    用explore函数来探索human在目前位置时可以到达的相邻区域：
        检测human的四个邻居，如果不是box，不是障碍，且没有超出地图，且没有被探索过，则把它加入到可以到达的相邻区域
        如果human的邻居中有box，则要在human和box的直线多探索一个位置，确定这个位置不是障碍，没有超出地图，且没有被探索过，则把她加入到可以到达的相邻区域
        检测完四个邻居后，返回可以到达的相邻区域
  开始bfs：
    使用初始box和human的位置组成的四元元组作为搜索的起点，目标点为搜索的目标点
    使用search函数进行搜索，search函数有两个参数（1、带检测的四元元组集合 2、目标点）：
        遍历四元元组集合，如果四元元组中的box位置和目标点位置重合，则返回0，
        如果不重合，则将用explore求出四元元组可以到达的相邻区域，并存储于集合wait_search_set中
        若遍历完没有发现box位置和目标点位置重合的点，对集合wait_search_set进行判断，若wait_search_set为空，则搜索失败，返回-1
        若wait_search_set不为空，则把wait_search_set和目标点再次放入search函数进行递归搜索，记录search函数的返回值为steps
        若steps为-1，表示递归执行的内层search函数没有找到合适的路径，则外层search函数也返回-1
        若steps不为-1，表示递归执行的内层search函数找到了合适的路径，则外层search函数返回steps+1,表示步数+1
  结束bfs：
    输出search函数返回的结果
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

N, M = [each for each in map(int, input().split())]

MAP = []
for i in range(N):
    MAP.append([each for each in input()])

for i in range(N):
    for j in range(M):
        if MAP[i][j] == '*':
            BOX = (i, j)
        elif MAP[i][j] == 'X':
            PLAYER = (i, j)
        elif MAP[i][j] == '@':
            TARGET = (i, j)


def explore(pos):
    reachable_neighbor = set()
    if (pos[2]-1, pos[3]) == pos[:2]:  # 如果玩家在箱子下方
        if pos[2]-2 >= 0 and MAP[pos[2]-2][pos[3]] != '#' and (pos[0]-1, pos[1], pos[2]-1, pos[3]) not in searched:
            reachable_neighbor.add((pos[0]-1, pos[1], pos[2]-1, pos[3]))
    else:
        if pos[2]-1 >= 0 and MAP[pos[2]-1][pos[3]] != '#' and (pos[0], pos[1], pos[2]-1, pos[3]) not in searched:
            reachable_neighbor.add((pos[0], pos[1], pos[2]-1, pos[3]))

    if (pos[2]+1, pos[3]) == pos[:2]:  # 如果玩家在箱子上方
        if pos[2]+2 < N and MAP[pos[2]+2][pos[3]] != '#' and (pos[0]+1, pos[1], pos[2]+1, pos[3]) not in searched:
            reachable_neighbor.add((pos[0]+1, pos[1], pos[2]+1, pos[3]))
    else:
        if pos[2]+1 < N and MAP[pos[2]+1][pos[3]] != '#' and (pos[0], pos[1], pos[2]+1, pos[3]) not in searched:
            reachable_neighbor.add((pos[0], pos[1], pos[2]+1, pos[3]))

    if (pos[2], pos[3]-1) == pos[:2]:  # 如果玩家在箱子右侧
        if pos[3]-2 >= 0 and MAP[pos[2]][pos[3]-2] != '#' and (pos[0], pos[1]-1, pos[2], pos[3]-1) not in searched:
            reachable_neighbor.add((pos[0], pos[1]-1, pos[2], pos[3]-1))
    else:
        if pos[3]-1 >= 0 and MAP[pos[2]][pos[3]-1] != '#' and (pos[0], pos[1], pos[2], pos[3]-1) not in searched:
            reachable_neighbor.add((pos[0], pos[1], pos[2], pos[3]-1))

    if (pos[2], pos[3]+1) == pos[:2]:  # 如果玩家在箱子左侧
        if pos[3]+2 < M and MAP[pos[2]][pos[3]+2] != '#' and (pos[0], pos[1]+1, pos[2], pos[3]+1) not in searched:
            reachable_neighbor.add((pos[0], pos[1]+1, pos[2], pos[3]+1))
    else:
        if pos[3]+1 < M and MAP[pos[2]][pos[3]+1] != '#' and (pos[0], pos[1], pos[2], pos[3]+1) not in searched:
            reachable_neighbor.add((pos[0], pos[1], pos[2], pos[3]+1))

    return reachable_neighbor


def search(current_pos_set, target):
    wait_search_set = set()
    for each_pos in current_pos_set:
        if each_pos[:2] == target:
            return 0
        else:
            searched.add(each_pos)
            wait_search_set.update(explore(each_pos))
    if wait_search_set:
        steps = search(wait_search_set, target)
        if steps != -1:
            return 1 + steps
        else:
            return -1
    else:
        return -1

searched = set()
current_pos = set()
current_pos.add((BOX[0], BOX[1], PLAYER[0], PLAYER[1]))  # current_pos = (br, bc, hr, hc)
print(search(current_pos, TARGET))
