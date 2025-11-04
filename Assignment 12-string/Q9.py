##python program to calculate number of words and number of characters present in astring.

def count_Words_and_characters(s):
    total_characters = len(s) #Excluding spaces
    total_words = len(s.split())
    
    return total_words,total_characters

user_input = input("Enter a string:")
words,characters = count_Words_and_characters(user_input)

print("Number of words:",words)
print("Number of characters:",characters)
