score1 = 75
score2 = 90
print(score1 >= 80 and score2 >= 80)
# false

score1 = 85
score2 = 95
print(score1 >= 80 and score2 >= 80)
# true

x = 10
print(x % 2 == 0 or x % 6 == 0)
# true

x = 16
print(x % 3 == 0 or x % 5 == 0)
# false

x = 25
print(not x % 2 == 0)
# true

print(not x > 10)
# false