#13. Reverse each word in a sentence while keeping the word order the same

sentence = "Hello world from Python"
reversed_words = " ".join(word[::-1] for word in sentence.split())
print(reversed_words)  # "olleH dlrow morf nohtyP"