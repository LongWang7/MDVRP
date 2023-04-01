import generator
import tools
import parameters
import ts
import random

random.seed(2022)
for i in range(1,7):
    # 对每个文件进行处理
    name = "p"
    if i >= 1 and i <= 9:
        implement = "0"
        name += implement
    name += str(i) + ".txt"
    g = generator.Generator(name)   # 寻优对象
    p = parameters.Parameters()                # 参数

    # 初始化
    partition = tools.generate_partition(g)
    routes = tools.generate_routes(g,partition,p)
    answers = []
    answers_value = []
    for route in routes:
        p = parameters.Parameters()
        t = ts.Ts(route,g,p)
        answers.append(t.best_route)
        answers_value.append(t.best_route_value)
    print(answers,'\n',sum(answers_value))
    tools.draw(answers,answers_value,g,str(i))