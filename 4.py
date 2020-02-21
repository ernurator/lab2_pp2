def exercise_4(l):
    return l[::-1]

l = [int(x) for x in input().split()]
print(exercise_4(l))