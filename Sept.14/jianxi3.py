import queue

# (人，狼，羊，菜)状态：1-未过河，0-过河
v=[(1,1,1,1),(1,1,1,0),(1,1,0,1),(1,0,1,1,),(1,0,1,0),\
       (0,1,0,0),(0,0,1,0),(0,0,0,1),(0,1,0,1),(0,0,0,0)]
p=[[(-1,100)]]*10 # 先前的状态

# 判定点的连通性
def connectivity(start,end):
    if v[start][0]==v[end][0]:
        return False
    cnt=0
    for i in range(1,4):
        if v[start][i]!=v[end][i]: 
            cnt+=1
    if cnt>=2: 
        return False
    else:
        return True

q=queue.Queue()
q.put((0,0))
while not q.empty():
    cur_tuple=q.get()
    cur=cur_tuple[0]
    dis=cur_tuple[1]+1
    for i in range(10):
        if connectivity(cur,i):
            # 当前比之前的路径短
            if dis<p[i][0][1]:
                # 清空之前的记录
                p[i]=[(cur,dis)]
                q.put((i,dis))
            # 和之前一样短
            elif dis==p[i][0][1]:
                # 追加一条记录：
                p[i].append((cur,dis))
                q.put((i,dis))

# for i in range(10):
#     p[i]=list(set(p[i]))

print(p)
