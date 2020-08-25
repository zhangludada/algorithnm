import time
# 地图
class Maze:
    def __init__(self):
        m = []
        for col in range(10):
            tmp = []
            for row in range(14):
                if col == 0 or col == 9 or row == 0 or row == 13:
                    tmp.append('#')  # 数字1是墙壁
                elif [col, row] in self.noway():
                    tmp.append('#')  # 数字8为不通
                else:
                    tmp.append(' ')  # 数字0是可以走的路
            m.append(tmp)

        self.start = [1, 1]
        self.end = [8, 12]
        self.plan = m

    # 不通的点,用于构建地图
    def noway(self):
        #     1             2                        3      4                  5             6                           8
        ls = [[2, 4], [2, 4, 5, 6, 7, 9, 10, 11], [7, 9], [2, 4, 7, 9, 11], [2, 4, 7, 11], [4, 10, 11],
              [2, 4, 5, 6, 8, 9, 10, 11], [2, 11]]
        #               7                           8
        xy = []
        for col in range(1, 9):
            for i in ls[col - 1]:
                xy.append([col, i])
        return xy

    # 行走迷宫,返回四个方向的坐标
    def go(self, coordinates):
        col = coordinates[0]
        row = coordinates[1]
        up = [col - 1, row]
        left = [col, row - 1]
        down = [col + 1, row]
        right = [col, row + 1]
        return [up, right, down, left]

    def action(self):
        route = [self.start]
        plan = self.plan

        while route != []:
            flag = False  # 假设路不通
            now = route[-1]
            plan[now[0]][now[1]] = '8'  # 走过的路为8

            for i in self.go(now):
                col, row = i[0], i[1]
                val = plan[col][row]
                # 有路走
                if val == ' ':
                    route.append([col, row])  # 新坐标加入route
                    flag = True  # 路通
                    if col == self.end[0] and row == self.end[1]:
                        # count=0
                        # print(count,[str(x) for x in range(14)])
                        # for i in plan:
                        #     print(count,i)
                        #     count+=1
                        print('走到出口啦')
                        return route
                    break

            if flag == False:  # 无路可走
                route.pop(-1)  # 退一步（删除当前坐标，继续循环）
        return '无法走到出口'

    def print_maze(self, plan):
        for i in plan:
            print(i)


m = Maze()
print(m.action())
