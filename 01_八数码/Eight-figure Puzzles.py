import copy

import numpy as np

# 定义节点类

class Node:

    count = 0

    # node为八码数的list表示，parent为父节点
    # cost为节点代价
    # nd_nums为不在位数

    def __init__(self,node,parent,cost,nd_nums):
        self.node=node
        self.parent=parent
        self.cost=cost
        self.nd_nums=nd_nums
        Node.count += 1

    def get_children(self):  # 获取一层子节点
        children = []
        for i in Nodes_change(self.node):
            # 逐个元素与0交换位置,生成子节点child
            child = Node(node=get_child(self.node, i), parent=self, cost=self.cost + 1,
                         nd_nums=not_digits(self.node, end_arr))
            # 将每一个交换结果（子节点）都存入children
            children.append(child)
        return children


# 计算逆序数

def reverseOrdinalNum(numString):

    #逆序数

    num=0

    # 第一个逆序数为0，所以只要从第二个开始算就是八个

    for i in range(1, 9):

        temp=0

        for j in range(0, i):

            if numString[j] > numString[i] and numString[i] != '0':

                temp += 1

        num = num+temp

    return num

# 获取与空格0之间交换的节点

def Nodes_change(arr):

    Nodes=[]

    r, c = find_local(arr, '0')  # 寻找0的的下标

    if r > 0:

        Nodes.append(arr[r - 1][c])  # 上边的数

    if r < 2:

        Nodes.append(arr[r + 1][c])  # 下边的数

    if c > 0:

        Nodes.append(arr[r][c - 1])  # 左边的数

    if c < 2:

        Nodes.append(arr[r][c + 1])  # 右边的数

    return Nodes



# 将字符串转化为列表

def string_to_list(str):

    str_list=list(str)

    return [str_list[i:i+3] for i in range(0,len(str_list),3)]

# 计算能否通过移动空格从初始态到目的状态

def isSolution(initState,endState):

    #把输入的空格删除

    initState=initState.replace(" ", "")

    endState=endState.replace(" ", "")

    if (reverseOrdinalNum(initState)%2)==(reverseOrdinalNum(endState)%2):

        return True

    else:

        return False

# 不在位数

def not_digits(arr1, arr2):

    num = 0

    for i in range(0, 3):

        for j in range(0, 3):

            if arr1[i][j] != arr2[i][j]:

                num = num + 1

    return num

# A*算法-不在位数

def AStar_ND(initial_arr, end_arr):

    open = [initial_arr]

    close = []



    while len(open) > 0:  # OPEN表是否为空表

        open_1 = [i.node for i in open]  # 访问open节点内的node

        close_1 = [i.node for i in close]



        n = open.pop(0)  # 删除OPEN队头节点

        close.append(n)  # n注入CLOSE表



        if n.node == end_arr:

            print('最优路径如下：')

            print(np.array(n.node,dtype=object))

            best_path(n)

            break

        else:

            for i in n.get_children():  # 添加子节点进OPEN

                if i.node not in open_1:

                    if i.node not in close_1:

                        open.insert(0, i)

                        open.sort(key=lambda x: x.nd_nums + x.cost)  # 按不在位数＋cost 进行排序

    print('--' * 20)

    print('--' * 20)

    print('--' * 20)

    search_line(close)

    print('搜索步骤为：', len(close) - 1)
    print('节点数为：', n.count)

# 整一个搜索路径：

def search_line(close):

    print('搜索路径如下：')

    for i in close[:-1]:

        print(np.array(i.node,dtype=object))

        print('||')

        print('||')

        print('||')

        print('\/')

    print(np.array(close[-1].node,dtype=object))

# 交换位置,并获得子节点

def get_child(arr, e):

    arr_new = copy.deepcopy(arr)  # 深拷贝，复制一份新的节点

    r, c = find_local(arr_new, '0')  # 寻找0的位置的坐标

    r1, c1 = find_local(arr_new, e)  # 寻找可交换的位置的坐标

    # 交换位置

    arr_new[r][c], arr_new[r1][c1] = arr_new[r1][c1], arr_new[r][c]

    return arr_new

# 寻找target的位置

def find_local(arr, target):  # arr是节点的list，target是寻找的目标

    for i in arr:

        for j in i:

            if j == target:

                return arr.index(i), i.index(j)  # 返回target的下标

def best_path(n):

    if n.parent == None:

        return

    else:

        print("↑")

        print(np.array(n.parent.node,dtype=object))

        best_path(n.parent)

def demo():

    print("""

    在一个3*3的方棋盘上放置着1,2,3,4,5,6,7,8八个数码,

    每个数码占一格,且有一个空格。这些数码可以在棋盘上移动，其移动规则是：

    与空格相邻的数码方格可以移入空格。现在的问题是：对于指定的初始棋局和目标棋局，给出数码的移动序列。

    本方法使用启发式 为了达到最优解，运用A*算法

    """)

    print("-" * 50)

    print("1.本程序解决的是八数码问题(基于启发式途径解决)")

    print("2.输入的数码为按行输入换行需加空格再输入")

    print("3.例如：")

    print("         1 2 3\n         4 5 6\n         7 8 9")

    print("它的输入表示为：'123 456 789'")

    print("-" * 50)

    '''
        例子1
        输入序列为：283 104 765
        目的序列为：123 804 765
        
        例子2
        输入序列为：203 184 765
        目的序列为：123 804 765
    '''

if __name__ == '__main__':

    demo()

    initStr = input("按要求输入初始矩阵:")

    endStr = input("按要求输入目标:")

    if isSolution(initStr,endStr):

        init_arr=string_to_list(initStr)

        end_arr=string_to_list(endStr)

        inital_arr=Node(init_arr,parent=None,cost=0,nd_nums=not_digits(init_arr,end_arr))

        AStar_ND(inital_arr,end_arr)

    else:

        print("此初始序列到不了目的序列，问题无解！！！")