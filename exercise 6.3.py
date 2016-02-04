def count(word, letter):
    number = 0
    for char in word:
        if char == letter:
            number += 1
    return number

n=count('lettereee', 'e')
print(n)
