##Python program to count the occurances of each word in a string.

def count_word_occurances(string):
    words = string.split()  #split string into words

    word_count = {}
    for word in words:
        word = word.lower()

        if word in word_count:
            word_count[word] += 1
        else:

            word_count[word] = 1

    return word_count

text = input("Enter a string:")
result = count_word_occurances(text)

print("\nWord occurances:")
for word,freq in result.items():
    print(f"{word}: {freq}")



