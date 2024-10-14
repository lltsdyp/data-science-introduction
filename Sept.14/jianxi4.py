c=2
i=0
g=0
eps=0.0001
step=0.00001
for j in range(0,c+1):
    if j**2<c and (j+1)**2>c:
        g=j
        break
while abs(g**2-c)>eps:
    g+=step

print(g)
