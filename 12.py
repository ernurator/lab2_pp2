def exercise_12(l):
    s = set()
    for i in l:
        n = i
        while n in s:
            n *= i
        s.add(n)
    return s

l = [int(x) for x in input().split()]
print(exercise_12(l)) 

    