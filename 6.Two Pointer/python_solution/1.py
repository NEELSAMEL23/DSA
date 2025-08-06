def reversed_vowels(s):

    vowels = "aeiouAEIOU"
    arr = list(s)
    i=0
    j = len(arr)-1

    while i < j:

        if arr[i] in vowels and arr[j] in vowels:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
            
        if arr[i] not in vowels:
            i+=1
        else:
            j-=1

    return "".join(arr)


s = "Hello World"
res = reversed_vowels(s)
print(res)



