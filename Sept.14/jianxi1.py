dp=[0,1,2,3]
dpl=[[0],[1],[2],[3]]

for i in range(4,2002):
    maxlist=[]
    curmax=i
    for j in range(1,i):
        #
        if curmax<dp[j]*dp[i-j]:
            curmax=dp[j]*dp[i-j]
            maxlist=dpl[j]+dpl[i-j]
    dp.append(curmax)
    dpl.append(maxlist.copy())
print(dpl[2001])
