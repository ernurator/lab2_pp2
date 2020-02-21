def exercise_1(list, i):
    return list[i]

l = [int(x) for x in input().split()]
i = int(input())
print(exercise_1(l, i))