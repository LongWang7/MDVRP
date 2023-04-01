import random
import numpy
from operator import itemgetter

a = [1,2,3,4,5]
b = a[:]
b[0] = 100
print(a,b)

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(0, 4, 0.05)
# y = np.sin(x*np.pi)
# plt.plot([1,3,2,4,2,1],[1,2,3,4,7,1],'rs-')
# plt.plot([5,3,2],[4,2,8])

# fig, ax = plt.subplots(figsize=(7,6), constrained_layout=False)
# ax.plot(x, y)
# ax.set_xlabel('t [s]')
# ax.set_ylabel('S [V]')
# ax.set_title('Sine wave')
# fig.set_facecolor('lightsteelblue')
# plt.show()

# a = [[5,1],[7,2],[1,3],[100,4],[70,5]]
# sorted(a,itemgetter[0][0])

# insertindexs = []
# insertindexs.append(123)
# length = 51
# print(length//2)
# a = [0,1,2,3,4,5]
# b = [6,7,8]
# a,b = b,a
# print(a,b)
# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# a.remove(a[1])
# print(10000 < float('inf'))
#
# import numpy.ma
# import torch
# a = torch.randperm(5).tolist()
# # print(torch.randperm(5),type(torch.randperm(5)))
# x = []
# print(a,a.index(min(a)))

# def change_str_to_int(current):    # 字符串转整形
#     length = len(current)
#     res,base = 0,1
#     for i in range(length-1,-1,-1):
#         res += base * (ord(current[i])-48)
#         base *= 10
#     return res
#
name = "cordeau-al-1997-mdvrp\p01.txt"
#
# with open(file = "cordeau-al-1997-mdvrp\p01.txt",mode="r",encoding="utf-8") as fb:
#     lines = fb.readlines()
#     dataFlow = []
#     for line in lines:
#         data = line.rstrip('\n').split(' ')
#         while '' in data:  data.remove('')
#         elements = []
#         for i in range(len(data)):
#             ele = change_str_to_int(data[i])
#             elements.append(ele)
#         dataFlow.append(elements)
#     m,n,d = dataFlow[0][1],dataFlow[0][2],dataFlow[0][3]   # 赋值车辆数、顾客数、车厂数
#     capacities = []     # 总服务的最大容忍时间 和 当前车场车辆中每辆车的最大容量
#     for i in range(1,d+1):
#         minc = dataFlow[i][0]
#         maxc = dataFlow[i][1]
#         capacity = [minc,maxc]
#         capacities.append(capacity)
#     needs = []  # 客户需求
#     # visit_combinations = [] # 每个客户允许被服务的车场组合
#     service_times = []  # 每个客户的服务时间
#     axis = []   # 各个城市的坐标
#     time_windows = [] # 时间窗
#     for i in range(d+1,d+n+1):
#         needs.append(dataFlow[i][4])
#         service_times.append(dataFlow[i][3])
#         axis.append([dataFlow[i][1],dataFlow[i][2]])
#         time_windows.append(dataFlow[i][-1]-dataFlow[i][-2])
#         # visit_combinations.append(dataFlow[i][7:-2])
#     for i in range(d+n+1,len(dataFlow)):
#         axis.append([dataFlow[i][1],dataFlow[i][2]])