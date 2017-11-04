for num in range(1,21):
    print(num)
num_1 = list(range(1,101))
for num in num_1:
    print(num)
print(min(num_1))
print(max(num_1))
print(sum(num_1))
odd_num = list(range(1,21,2))
for num in odd_num:
    print(num)
multiples_of_three = list(range(3,31,3))
for num in multiples_of_three:
    print(num)
cubes = []
for num in range(1,11):
    num = num**3
    cubes.append(num)
print(cubes)
cubes_1 = [num**3 for num in range(1,11)]
print(cubes_1)