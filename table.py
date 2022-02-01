import sys

print("this program prints out a relative frequency of characters in a string")

word = input()
def getFrequency(word):
    print("given input: " + word)

    charDict = {}
    for char in word:
        if char not in charDict:
            charDict[char] = 1
        else:
            charDict[char] += 1
    return charDict
# for printing pretty, accepts a relative frequency data type
def print_row(relativeFreqency):
    for key in relativeFreqency:
        print( 'character: ',key ,'| ',
                'frequency: ', relativeFreqency[key],
                '| ', 'ascii: ', ord(key))

    
print_row(getFrequency(word))
