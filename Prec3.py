# Find runner-up from given list
# 20CS003
# Amit Amrutiya

n = int(input())
score = map(int, input().split())
print(sorted(list(set(score)))[-2])
