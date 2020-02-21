def exercise_8(l):
    return (min(l), max(l))

l = [int(x) for x in input().split()]
print(exercise_8(l))