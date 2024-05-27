#Count vowels in a given word.

word = str(input("Enter a word:"))
vow = ['a','e','i','o','u']
count = 0
for i in range(len(word)):
    if word[i] in vow:
        count = count+1
print("The word: {} has {} vowels.".format(word, count))        
        