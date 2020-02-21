l = [int(x) for x in input().split()]
d = dict()

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

odd = 0
for ind in d:
    if d[ind] % 2 == 1:
        odd += 1

if odd > 1: print('No')
else: print('Yes')