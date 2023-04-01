import copy
import random
import tools

class Ts():

    def __init__(self,route,g,p):
        self.taboo_list = []
        self.best_routes = []
        self.ts_process(route,g,p)
        self.best_route,self.best_route_value = self.deal_best_routes(g)

    def generate_neighbers(self,route,p):   # 通过交换产生领域解
        neighbers = []
        for i in range(p.neighberhood_size):
            neighber = [ele for ele in route]
            length = len(neighber)
            position1,position2 = random.randrange(1,length),random.randrange(1,length)
            neighber[position1],neighber[position2] = neighber[position2],neighber[position1]
            neighbers.append(neighber)
        return neighbers

    def soulution_update(self,g,p,neighbers):  # 禁忌表解的更新,taboo_list可以直接引用，不用作为参数
        values = []
        for i in range(len(neighbers)):
            queue = neighbers[i]
            values.append(tools.caculate_cost(g,queue,p))
        sorted_values = sorted(list(enumerate(values)),key=lambda dimension:dimension[1])
        # sorted_values[i]有两个元素，第一个是下标，第二个是values
        # 每次记录当前taboo_list中的最好解
        if len(self.taboo_list):
            taboo_list_values = [tools.caculate_cost(g,queue,p) for queue in self.taboo_list]
            minimum_taboo_list_value = min(taboo_list_values)
            minimum_index = -1
            for i in range(len(taboo_list_values)):
                if taboo_list_values[i] == minimum_taboo_list_value:
                    minimum_index = i
                    break
            self.best_routes.append(self.taboo_list[minimum_index])
        flag = 0
        next_route = neighbers[sorted_values[0][0]]
        for i in range(len(sorted_values)):
            if sorted_values[i] in self.taboo_list:
                continue
            if len(self.taboo_list) < p.taboo_size:     # taboo_list还未满
                self.taboo_list.append(neighbers[sorted_values[i][0]])
                next_route = neighbers[sorted_values[i][0]]
                flag = 1
                break
            else:   # taboo_list已满
                self.taboo_list.remove(self.taboo_list[0])
                self.taboo_list.append(neighbers[sorted_values[i][0]])
                next_route = neighbers[sorted_values[i][0]]
                flag = 1
                break
        if not flag:    # 特赦
            if len(self.taboo_list) < p.taboo_size:
                self.taboo_list.append(neighbers[sorted_values[0][0]])
                next_route = neighbers[sorted_values[0][0]]
            else:
                self.taboo_list.remove(self.taboo_list[0])
                self.taboo_list.append(neighbers[sorted_values[0][0]])
                next_route = neighbers[sorted_values[0][0]]
        # 更新α与β参数
        q, d = 0, 0
        for ele in next_route:
            if ele >= g.n:
                continue
            q += g.needs[ele]
            d += g.service_times[ele]
        depot_number = next_route[0] - g.n
        if q > g.capacities[depot_number][1]:
            p.alpha *= (1 + p.delta)
        else:
            p.alpha /= (1 + p.delta)
        if d > g.capacities[depot_number][0]:
            p.beta *= (1 + p.delta)
        else:
            p.beta /= (1 + p.delta)
        return next_route

    def deal_best_routes(self,g):
        best_routes_values = []
        for i in range(len(self.best_routes)):
            current_value = 0
            for j in range(len(self.best_routes[i])-1):
                current_value += g.distances[self.best_routes[i][j]][self.best_routes[i][j+1]]
            current_value += g.distances[self.best_routes[i][-1]][self.best_routes[i][0]]
            best_routes_values.append(current_value)
        best = self.best_routes[best_routes_values.index(min(best_routes_values))]
        return best,min(best_routes_values)

    def ts_process(self,route,g,p):     # 禁忌搜索全过程
        iteration,iterations = 1,p.iterations
        while iteration < iterations:
            neighbers = self.generate_neighbers(route,p)
            route = self.soulution_update(g,p,neighbers)
            iteration += 1