def calculate_average(scores): 
    return sum(scores) / len(scores)
assert calculate_average ([6,8,10]) == 8 
assert calculate_average ([4,6]) == 5 
assert calculate_average ([1,2,3]) == 2