# Here is a function that takes list of words and returns a dictionary where keys are sorted tuples of 
# letters and values are their anagrams

def group_anagrams(words: list) -> dict:
    anagrams = {}  # Initialize an empty dictionary to store grouped anagrams
    for word in words:
        sorted_word = tuple(sorted(word))  
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)  
        else:
            anagrams[sorted_word] = [word] 
    return anagrams 


words=["listen",'silent','enlist','google',"gooleg"]
print(group_anagrams(words))




