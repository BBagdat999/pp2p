def reversed_words(string): # words
    # for i in range(len(string)-1, -1, -1):
    #     print(string[i], end=' ')
         
    print(*[string[ch] for ch in range(len(string)-1, -1, -1)], end=' ')
        
reversed_words(input('enter a some words: ').split())