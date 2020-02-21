def exercise_10(s):
    s1 = set()
    for i in s:
        s1.add(i - 1)
        s1.add(i + 1)
    return s1

s = set(int(x) for x in input().split())
print(exercise_10(s)) 