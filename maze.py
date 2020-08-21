import numpy as np


# 地图
class Map:
    def m(self):
        m = []
        for col in range(10):
            tmp = []
            for row in range(14):
                if col == 0 or col == 9 or row == 0 or row == 13:
                    tmp.append(1)  # 数字1是墙壁
                elif [col, row] in self.noway():
                    tmp.append(2)  # 数字8为不通
                else:
                    tmp.append(0)  # 数字0是可以走的路
            print(tmp)
            m.append(tmp)
        return m

    # 不通的点
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


a = Map()
b = a.m()
