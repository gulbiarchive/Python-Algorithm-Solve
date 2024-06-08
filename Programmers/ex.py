# # 입력 받기
# T = int(input("테스트 케이스의 개수: "))

# # 각 테스트 케이스를 저장할 리스트
# test_cases = []

# # 테스트 케이스 입력 받기
# for _ in range(T):
#     A, B = map(int, input().split())
#     test_cases.append((A, B))

# # 각 테스트 케이스를 처리하여 결과 출력
# for index, (A, B) in enumerate(test_cases, start=1):
#     result = A + B
#     print(f"Case #{index}: {result}")

# 문자열의 개수 입력
N = int(input("문자열의 개수: "))

# 문자열을 저장할 리스트
strings = []

# 문자열 입력받기
for _ in range(N):
    string = input()
    strings.append(string)

# 각 문자열을 인덱스와 함께 출력
for index, string in enumerate(strings, start=1):
    print(f"String #{index}: {string}")