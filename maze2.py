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
        start = self.start
        now = start
        plan = self.plan
        count = 0
        old_count = -1
        all_step = [[-1] + start]
        st = 0
        while True:
            n = 0  # count 增加了几次
            for i in range(st, len(all_step)):  # 遍历所有原始点
                col_old, row_old = all_step[i][1], all_step[i][2]
                previous_count = all_step[i][0]
                plan[col_old][row_old] = '#'
                for j in self.go(all_step[i]):  # 遍历所有点的可前进方向
                    col, row = j[0], j[1]
                    val = plan[col][row]
                    if val == ' ':  # 如果路通
                        all_step.append([previous_count, col, row])
                        n += 1
            st = len(all_step) - n

    def print_maze(self, plan):
        for i in plan:
            print(i)


m = Maze()
print(m.action())
