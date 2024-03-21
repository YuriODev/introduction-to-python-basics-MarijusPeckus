# Exercise 3
# Your solution comes here
i = int(input())


hours = (i // 3600) % 24
minutes = (i // 60) % 60
seconds = i % 60
print(f'{hours}:{minutes:02d}:{seconds:02d}' )
