def exercise_5(list, i):
    return list[:i]


l = [int(x) for x in input().split()]
i = int(input())
print(exercise_5(l, i))