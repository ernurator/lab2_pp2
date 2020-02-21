def exercise_14(l, n):
    s = set()
    for i in l:
        if i > n:
            s.add(i)
    return s

l = [int(x) for x in input().split()]
n = int(input())
print(exercise_14(l, n))