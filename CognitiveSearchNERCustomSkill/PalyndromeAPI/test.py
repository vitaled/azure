def extract_palyndromes(text:str):

    palyndromes = []

    for token in text.split():
        token = token.lower()
        token = ''.join(filter(str.isalnum,token))
        if is_palyndrome(token):
            palyndromes.append(token)

    return list(set(palyndromes))


def is_palyndrome(token:str) -> bool:
    if token is None or len(token) <=1:
        return False

    i = 0
    j = len(token)-1

    while(i<j):
        if token[i] != token[j]:
            return False
        i+=1
        j-=1

    return True

print(is_palyndrome("anna"))
print(is_palyndrome("bob"))
print(is_palyndrome("anne"))
print(is_palyndrome("lucy"))

print(extract_palyndromes("Bob has a problem. He's a palindrome. In fact, once he learns what a palindrome is, he starts finding palindromes everywhere: his little sis, Nan; his pup, Otto; even his Mom and Dad! It's making Bobfeel like a kook. Is there no escape? Mark Shulman and Adam McCauley have joined forces to create a wonderfully visual, ridiculously clever book of wordplay. Join the hilarity. . . do your civic deed, don't let your pupils slip up, and find the over 101 palindromes hiding in the words and pictures of this zany book."))