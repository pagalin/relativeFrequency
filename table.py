import sys

print("this program prints out a relative frequency of characters in a string")

word = input()

print("given input: " + word)

charDict = {}
for char in word:
    if char not in charDict:
        charDict[char] = 1
    else:
        charDict[char] += 1
print(charDict)

