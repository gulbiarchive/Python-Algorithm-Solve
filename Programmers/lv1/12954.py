# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    a = x
    
    for _ in range(n):
        answer.append(x)
        x += a
    return answer

print(solution(x=2, n=5))