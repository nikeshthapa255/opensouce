import random, math
shuffle = random.shuffle
rin = random.randint
exp = math.exp

from collections import defaultdict as dd
dc = dd(int)
# get estimate cost to goal or h(x)
def get_h(mtx):
    n = len(mtx)
    if n!=len(mtx[0]):
        raise ValueError("Invalid length of matrix")
    pt = []
    for i in range(n):
        for j in range(n):
            if mtx[i][j]==1:
                pt.append((i, j))
    if len(pt)!=n:
        raise ValueError("Invalid number of queens - {}".format(len(pt)))
    ans = -6*n
    for i, j in pt:
        for i1 in range(n):
            # row
            ans += mtx[i1][j]
            # column
            ans += mtx[i][i1]
            # diagonals
            if i-i1>=0 and j-i1>=0 :
                ans += mtx[i-i1][j-i1]
            if i-i1>=0 and j+i1<n :
                ans += mtx[i-i1][j+i1]
            if i+i1<n and j-i1>=0 :
                ans += mtx[i+i1][j-i1]
            if i+i1<n and j+i1<n :
                ans += mtx[i+i1][j+i1]
            # print(i, j, i1, ans)
    return ans

# generates random state 
def generate_state(n):
    a1 = list(range(n))
    shuffle(a1)
    mtx = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        mtx[i][a1[i]] = 1
    return mtx

# random state with some intuition of previous step
def generate_state_mtx(mtx):
    n = len(mtx)
    x1, x2 = rin(0, n-1), rin(0, n-1)
    mtx[x1] = [0]*n
    mtx[x1][x2] = 1
    return mtx


# choose next state normal
def modify(mtx, sol, ans):
    x1 = get_h(mtx)
    if x1<sol:
        sol = x1
        ans = mtx
    return sol, ans
    
# choose next state annealed
def modify_annealed(mtx, sol, ans, epoch):
    x1 = get_h(mtx)
    if x1<sol or (exp((sol-x1)/epoch) > 0.1):
        sol = x1
        ans = mtx
    return sol, ans
    

def evaluate(epoch):
    
    n = 6
    ans = generate_state(n)
    sol = get_h(ans)
    e1 = epoch
    for _ in range(e1, 0, -1):
        mtx = generate_state_mtx(ans)
        sol, ans = modify_annealed(mtx, sol, ans, e1)
        dc[sol]+=1
        if sol == 0:
            print("optimal solution found , ", epoch, " time left")
            break
    print('Your solution is - ', sol)
    for i in ans:
        print(*i)
    get_graph(epoch)

def get_graph(epoch):
    print("Graph - ")
    for i in dc:
        print('{} - {}%'.format(i, (dc[i]/epoch)*100))


evaluate(int(input("HOw many time you want to run - ")))



