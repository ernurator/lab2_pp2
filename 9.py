def exercise_9(t):
    for i in t:
        if type(i) == list or type(i) == set or type(i) == dict:
            return True
    return False

print(exercise_9((10, 2, 5, [4, 8, 2], 3, 5)))
print(exercise_9((5, 2.5, 8, 4, 'Hi', -5, True, 6)))