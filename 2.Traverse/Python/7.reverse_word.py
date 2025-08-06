
def reverse_words(sentence):
    words = sentence.split() 
    reversed_words = [word[::-1] for word in words]  
    return " ".join(reversed_words)  

n = 11
sentence = "hello world"
res = reverse_words(sentence)
print(res)