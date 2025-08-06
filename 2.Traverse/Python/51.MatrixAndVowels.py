def find_vowels(arr,N,M):
    vowels = "aeiou"
    for col in range(M):
        vowels_present = False
        for row in range(N):
            if arr[row][col] in vowels:
                vowels_present = True
                break

        if vowels_present:
            print("Yes")
        else:
            print("No")




arr = [
    ["l","m","n"],
    ["o","p","q"],
    ["r","s","t"]
]

N = 3
M = 3

find_vowels(arr,N,M)
