def exercise_3(list, j):
    for i in range(j, len(list)):
        list[i] **= 2
    return l

l = [int(x) for x in input().split()]
i = int(input())
print(exercise_3(l, i))