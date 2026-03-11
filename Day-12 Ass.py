#Day-12 Ass


#1.Revome Duplicates words

string =input("Enter a sentence :")
result = ""

for ch in string:
    if ch not in result:
        result = result+ch
print("String after removing duplicates:", result)




#2.Remove duplicate words from string

sentence = input("Enter a sentence :")

words = sentence.split()
result = []

for word in words:
    if word not in result:
        result.append(word)

print(" ".join(result))


#3.Sort Letters in a word

word = input("Enter a word :")

letter = list(word)
letter.sort()

sorted_word ="".join(letter)
print("Sorted word :", sorted_word)
