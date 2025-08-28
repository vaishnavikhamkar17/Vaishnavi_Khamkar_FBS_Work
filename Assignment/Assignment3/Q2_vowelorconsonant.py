##WAP to input any alphabet and check wheather it is vowel or consonant.

alphabet = input("Enter the alphabet:")

if(alphabet in "aeiouAEIOU"):
    print(f"{alphabet}  is vowel.")   # Use membership operator
else:
    print(f"{alphabet}  is consonant.")

          #OR

alphabet = input("Enter the alphabet:")

if(alphabet == 'a' or alphabet == 'e'or alphabet == 'i' or alphabet ==  'o' or alphabet == 'u'): # comparision operator- equals to
    print(f"{alphabet}  is vowel.")
else:
    print(f"{alphabet}  is consonant.")