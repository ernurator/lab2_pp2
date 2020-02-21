def exercise_2(list):
    return list[::2]

l = [int(x) for x in input().split()]
print(exercise_2(l))