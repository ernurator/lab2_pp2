def exercise_6(list, i, d, numb):
    list = list[:i] + numb + list[i:]
    return list[:d]

l = [int(x) for x in input().split()]
i = int(input())
d = int(input())
numb = [int(x) for x in input().split()]
print(exercise_6(l, i, d, numb))