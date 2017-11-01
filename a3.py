import math
D={}

def Graph():
    s = list()
    a = int(input())
    for i in range(a):
        x = int(input())
        u = list()
        for c in range(x):
            v = list(input().split(' '))
            u.append(v)
            s.append(u)
    return s

def dist(v):
    global D
    return D[v]

def mini(Q):
    global D
    temp={}
    for i in Q:
        temp[i]=D[i]
    hey=list(temp.values())
    hey.sort()
    for i in temp:
        if temp[i]==hey[0]:
            return i

def Dijkstra(source,graph):
    #Q = [0, 1, 2, 3, 4]
    Q=[]
    for i in range(len(graph)):
        Q.append(i)
    global D
    #plot=[[[1,5],[2,3]],[[3,3]],[[1,2],[3,5],[4,6]],[],[[3,1]]]
    print(Q)
    plot=list(graph)
    for v in Q:
        D[v]=math.inf
        D[source]=0
    while Q != []:
        u=mini(Q)
        Q.remove(u)
        for s in plot[u]:
            alt = dist(u) + s[1]
            if alt < dist(s[0]):
                D[s[0]]=alt
    return D       

def BFS(source,graph):
    #plot=[[[1,5],[2,3]],[[3,3]],[[1,2],[3,5],[4,6]],[],[[3,1]]]
    Q=[0,1,2,3,4,5]
    plot=graph
    for v in Q:
        D[v]=math.inf
        D[source]=0
    N=[]
    N.append(source)
    k=source
    i=0
    while i!=len(plot):
        a=plot[N[i]]
        for j in a:
            if j[0] not in N:
                N.append(j[0])
        i+=1  
    visit=[]
    done={}
    
    for i in N:
        if i not in visit:
            done[source]=0
            visit.append(i)
            b=plot[i]
            for j in b:
                if j[0] not in done:
                    done[j[0]]=j[1]+done[i]
    return done


if __name__ == '__main__':
    BFS(0,[[[1,7],[2,11],[3,2]],[[3,10]],[[5,8]],[[2,6],[4,18],[5,17]],[],[[4,1]]])  
