def shift_cipher(plaintext,shift):
    indexes=[]
    shifted=""
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for char in plaintext:
        indice=alphabet.index(char)
        indexes.append(indice)
    print(indexes)
    for ind in indexes:
        ind=ind+shift%len(alphabet)
        shifted+=alphabet[ind]
    print(shifted)



