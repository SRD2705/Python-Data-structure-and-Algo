n = int(input())
x = int(input())
result = 0
for i in range(4,n+1,3):
    result += pow(i,i-1)
print(result)

# while i <= n:
#     result += pow(i,i-1)
#     i += 3
# print(result)