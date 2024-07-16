# To add words to a dictionary and values are how frequently the words are repeated
def word_frequency(words: list) -> dict:
       frequency = {}
       for word in words:
           if word in frequency:
               frequency[word] += 1
           else:
               frequency[word] = 1
       return frequency

words=["hello",'hi','how','when','hello','hi','how']    
print(word_frequency(words))


    
