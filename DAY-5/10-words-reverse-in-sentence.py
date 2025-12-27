# Q10 Reverse words in a sentence

#input
sentance = list(input("Input: ").split())

#reversed words
reversed_words = []

#reversing the words from sentence
for i in sentance:
    reversed_words.append(i[::-1])

#joining the words and making a sentance with proper seperator
print(" ".join(reversed_words))