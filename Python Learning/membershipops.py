#test if a value is included in a sequence, icludes vars

word = "apple"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print("Correct!")

phrase = "The cat sat on the mat"

w = input("Guess a word in that phrase: ")

if w in phrase:
    print("Yes!!!")

if "sat" in phrase:
    print("True")

name = "Max"

sentence = f"hello, {name}"

if "Max" in sentence:
    print("True!")