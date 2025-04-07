import itertools

print("Enter the characters to use for combination and hit 'enter':", end="")
chars = input()
print("enter the length of password expected")
length = input()

for combo in itertools.product(chars, repeat=length):
    word = ''.join(combo)
    print(word)
