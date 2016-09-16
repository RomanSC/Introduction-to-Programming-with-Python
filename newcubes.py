# sum cubes

n = input("\nWhat is n? \n")

sum_cubes = 0
sum_cubes = float(sum_cubes)

for i in range(1, n + 1):
    sum_cubes = sum_cubes + i ** 3

print(sum_cubes)
