old = ['a','b','a','c','b','a']

sort = sorted(set(old))
new = []

for letter in sort:
    new.append(letter)

print(new)