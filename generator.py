import numpy as np

class Generator():

    ''':parameter declaration
    m               车辆数
    n               顾客数
    d               车场数
    capacities      当前车场服务的最大时间 和 当前车场中车辆的最大容量
    needs           客户需求
    service_times   服务时间
    axis            坐标
    time_windows    时间窗口
    '''

    def __init__(self,name):
        self.m,self.n,self.d,self.capacities,self.needs,self.service_times,self.axis,self.time_windows,self.distances\
            = self.getData(name)

    def change_str_to_int(self,current):  # 字符串转整形
        length = len(current)
        res, base = 0, 1
        for i in range(length - 1, -1, -1):
            res += base * (ord(current[i]) - 48)
            base *= 10
        return res

    def caculate_distances(self,axis):
        length = len(axis)
        distances = np.zeros((length, length))
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                distances[i][j] = np.ma.sqrt((axis[i][0] - axis[j][0]) ** 2 + (axis[i][1] - axis[j][1]) ** 2)
        return distances

    def getData(self,name):
        with open(file=name, mode="r", encoding="utf-8") as fb:
            lines = fb.readlines()
            dataFlow = []
            for line in lines:  # 字符串矩阵处理成整形矩阵
                data = line.rstrip('\n').split(' ')
                while '' in data:  data.remove('')
                elements = []
                for i in range(len(data)):
                    ele = self.change_str_to_int(current=data[i])
                    elements.append(ele)
                dataFlow.append(elements)
            m, n, d = dataFlow[0][1], dataFlow[0][2], dataFlow[0][3]  # 赋值车辆数、顾客数、车厂数
            capacities = []  # 总服务的最大容忍时间 和 当前车场车辆中每辆车的最大容量
            for i in range(1, d + 1):
                minc = dataFlow[i][0]
                maxc = dataFlow[i][1]
                capacity = [minc, maxc]
                capacities.append(capacity)
            needs = []  # 客户需求
            # visit_combinations = [] # 每个客户允许被服务的车场组合
            service_times = []  # 每个客户的服务时间
            axis = []  # 各个城市的坐标
            time_windows = []  # 时间窗
            for i in range(d + 1, d + n + 1):
                needs.append(dataFlow[i][4])
                service_times.append(dataFlow[i][3])
                axis.append([dataFlow[i][1], dataFlow[i][2]])
                time_windows.append([dataFlow[i][-1],dataFlow[i][-2]])
                # visit_combinations.append(dataFlow[i][7:-2])
            for i in range(d + n + 1, len(dataFlow)):
                axis.append([dataFlow[i][1], dataFlow[i][2]])
            distances = self.caculate_distances(axis)
            return m,n,d,capacities,needs,service_times,axis,time_windows,distances