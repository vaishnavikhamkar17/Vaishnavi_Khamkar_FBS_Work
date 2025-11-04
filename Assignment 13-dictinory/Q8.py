##Python program to count the frequency of words appearing in a string using a dictionary.

def words_frequency(sentence):
    words = sentence.split()   #split the sentence into word
    freq = {}

    for word in words :
        word = word.lower()
        
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

sentence = input("Enter a sentence:")
result = words_frequency(sentence)

print("Word frequency:")
for word, count in result.items():
    print(word, ":", count)

