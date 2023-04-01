import numpy as np
import matplotlib.pyplot as plt

def caculate_distances(axis):
    length = len(axis)
    distances = np.zeros((length,length))
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            distances[i][j] = np.ma.sqrt((axis[i][0]-axis[j][0])**2 + (axis[i][1]-axis[j][1])**2)
    return distances

def generate_partition(g):
    depots = [i for i in range(len(g.axis) - g.d, len(g.axis))]
    partition = [[ele] for ele in depots]
    for i in range(g.n):
        distance = []
        for j in range(len(depots)):
            distance.append(g.distances[i][depots[j]])
        partition[distance.index(min(distance))].append(i)
    while True:
        flag = 1
        for i in range(len(partition)):
            if len(partition[i]) == 1:
                partition.remove(partition[i])
                flag = 0
                break
        if flag:
            break
    return partition

def caculate_cost(g,queue,p):
    res = 0
    for i in range(len(queue)-1):
        res += g.distances[queue[i]][queue[i+1]]
    res += g.distances[queue[-1]][queue[0]]
    q,d = 0,0
    for ele in queue:
        if ele >= g.n:
            continue
        q += g.needs[ele]
        d += g.service_times[ele]
    depot_number = queue[0] - g.n
    if q > g.capacities[depot_number][1]:
        res += p.alpha * (q - g.capacities[depot_number][1])
    if d > g.capacities[depot_number][0]:
        res += p.beta * (d - g.capacities[depot_number][0])
    return res


def generate_routes(g, partition, p):
    value = []
    for i in range(len(partition)):
        value.append(caculate_cost(g,partition[i],p)/len(partition[i]))
    if g.m < g.d:   # 如果车辆数小于车场数，意味着缩减
        while len(partition) != g.m:
            maxindex = value.index(min(value))
            vector = partition[maxindex]
            partition.remove(partition[maxindex])
            value.remove(value[maxindex])
            while len(vector) > 1:   # 依次对比将要插入的元素
                element = vector[1]
                vector.remove(vector[0])
                insertindexs = []
                insertvalues = []
                for i in range(0,len(partition)):     # 每条路
                    insertvalue = float('inf')
                    insertindex = -1
                    for j in range(1,len(partition[i])):    # 每个插入位置
                        queue = partition[i][:]
                        queue.insert(j,element)
                        current_cost = caculate_cost(g,queue,p)
                        if current_cost < insertvalue:
                            insertvalue = current_cost
                            insertindex = j
                    insertindexs.append(insertindex)
                    insertvalues.append(insertvalue/len(queue))
                insert_partition_index = insertvalues.index(min(insertvalues))
                partition[insert_partition_index].insert(insertindexs[insert_partition_index],element)
    elif g.m > g.d: # 如果车辆数大于车场数
        for i in range(len(partition)):     # 更新value为每条路线的总距离
            value[i] = value[i] * len(partition[i])
        while g.m != len(partition):    # 找出距离最大的不断二分裂,注意不是平均距离最大的
            maxindex = value.index(max(value))
            vector = partition[maxindex]
            partition.remove(partition[maxindex])
            value.remove(value[maxindex])
            length = len(vector)
            route1 = vector[0:length//2]
            route2 = vector[length//2:]
            route2.insert(0,route1[0])
            value1 = caculate_cost(g,route1,p)
            value2 = caculate_cost(g,route2,p)
            if value2 > value1:
                route1,route2 = route2,route1
                value1,value2 = value2,value1
            while value1 > value2:
                element = route1[1]
                route1.remove(element)
                route2.insert(1,element)
                value1 = caculate_cost(g,route1,p)
                value2 = caculate_cost(g,route2,p)
            partition.append(route1)
            partition.append(route2)
            value.append(value1)
            value.append(value2)
    else:
        return partition
    return partition

def draw(answers,answers_value,g,name):
    for i in range(len(answers)):
        x,y = [],[]
        for j in range(len(answers[i])):
            x.append(g.axis[answers[i][j]][0])
            y.append(g.axis[answers[i][j]][1])
        x.append(x[0])
        y.append(y[0])
        plt.plot(x,y,'*-')
    for i in range(g.n,g.n+g.d):
        plt.plot(g.axis[i][0],g.axis[i][1],'r.')
    plt.title("No." + name + "dataset")
    plt.suptitle(str(sum(answers_value)))
    plt.savefig(name)