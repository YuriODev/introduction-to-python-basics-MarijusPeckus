# Exercise 1
# Your solution comes here




n = int(input("Enter a five-digit number: "))


part1 = (n // 10000) + ((n // 100) % 10) + (n % 10)
print(part1)
part2 = ((n // 1000) % 10) + ((n // 10) % 10)

print(str(part1) + str(part2))