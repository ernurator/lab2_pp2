def exercise_15(l):
    res = 0
    for i in l[1::2]:
        if i % 2 == 1:
            res += 1
    return res

l = [int(x) for x in input().split()]
print(exercise_15(l))