def exercise_11(s1, s2):
    return s1.difference(s2)

s1 = set(int(x) for x in input().split())
s2 = set(int(x) for x in input().split())
print(exercise_11(s1, s2)) 