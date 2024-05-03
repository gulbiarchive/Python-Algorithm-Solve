hour, score = map(int, input().split())

# 3분마다 골 넣으면서 1점씩 득점
for _ in range(hour, 80, 3):
    score += 1

print(score)