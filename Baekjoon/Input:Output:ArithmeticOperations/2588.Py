A = int(input())
B = int(input())

print(A * (B % 10)) # (3)
print(A * ((B // 10) % 10)) # (4)
print(A * ((B // 10) // 10)) #(5)
print(A * B)