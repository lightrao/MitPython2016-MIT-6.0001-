s = "abcdefghijklmnopqrstuvwxyz"
# print(len(s))
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u.")

print()

for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u.")