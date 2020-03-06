from listm import *
from pinyin import *
import numpy as np
import  networkx as nx
import matplotlib.pyplot as plt
def generateGraph():
    mat = np.zeros((len(vName), len(vName)))
    flag = np.zeros((len(vName), len(vName)))
    for item in listma:
        mat[yunToID(item[3])][yunToID(item[4])] += 1
        flag[yunToID(item[3])][yunToID(item[4])] = 1
    for row in range(0, len(vName)):
        mat[row] /= sum(mat[row])
    return [len(vName), len(vName)], mat, flag

# plt.figure(figsize=(19.2,10.8))
# shape, _, s_g = generateGraph()
# G = nx.MultiDiGraph()
# for i in range(0, shape[0]):
#     for j in range(0, shape[0]):
#         if s_g[i][j] == 1:
#             G.add_edge(IDtopin(i), IDtopin(j))
#
# nx.draw_networkx(G, arrows=True, with_labels=True)
# plt.savefig('./result.png')
# plt.show()

#Input: 起始韵母, 目标韵母
def choiceEval(src: str, dst: str) -> list:
    res = {}
    shape, K, flag = generateGraph()
    src = yunToID(src)
    dst = yunToID(dst)
    #假设vb储存着本轮移动到某点的价值, 初值为随机移动至目标韵母的概率
    vb = np.transpose(K[:, dst])
    vw = np.zeros(shape[0])
    #迭代数次获取较稳定的值,次数过大后会收敛至1
    for loop in range(0, 2):
        #选择最大概率的移动
        for i in range(0, shape[0]):
            vw[i] = max(flag[i] * vb) if i != dst else 1
        #NPC随机选择一个点移动
        for i in range(0, shape[0]):
            vb[i] = sum(flag[i] * vw) / sum(flag[i])
    #输出结果
    return vb * flag[src]

def toSame():
    return {x :[tup for tup in yuntoicron[x] if yuntopin(tup[4]) == 'same'] for x in yuntoicron.keys()}