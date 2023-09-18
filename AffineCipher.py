def affine_cipher_encrypt(plaintext,a,b):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    indexes=[]
    affined=""
    for char in plaintext:
        indice=alphabet.index(char)
        new_index=((a*indice)+b)%len(alphabet)
        indexes.append(new_index)
    for ind in indexes:
        affined+=alphabet[ind]
    print(affined)

affine_cipher_encrypt("WORLD",5,8)
    