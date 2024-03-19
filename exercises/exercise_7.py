# Exercise 7
# Your solution comes here
i = int(input())
total = i % 1000
total = total +(i%1000) //100
total = total +(i%100) //10
print(total)