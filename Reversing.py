word = input("Enter a word : ")
count = 0
pos = 0
while pos < len(word):
    count = count + 1
    pos = pos + 1
print("The word ", word, "has", count, "letters.")