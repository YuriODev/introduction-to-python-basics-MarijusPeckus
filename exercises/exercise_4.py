# Exercise 4
# Your solution comes here
i = int(input())


d1 = i // 1000
d2 = (i % 1000) // 100
d3 = (i % 100) // 10
d4 = i % 10

first_part = d1+ d3 + d4
print(first_part)
second_part = d2 + d3

print(str(first_part) + str(second_part))