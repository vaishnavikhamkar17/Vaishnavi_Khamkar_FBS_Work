for i in range(5):
    print(' ' *(5-i-1)*2, end=' ')
        
    for j in range(2*i+1):
        print(chr(65+j), end=' ')
    print()