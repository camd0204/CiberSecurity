def substitution_cipher(plaintext,clave):
    indexes=[]
    shifted=""
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for char in plaintext:
        indice=alphabet.index(char)
        indexes.append(indice)
    print(indexes)
    for key in clave:
        if key in alphabet:
            numero=alphabet.index(key)
            alphabet[numero]=clave[key]
    for ind in indexes:
        shifted+=alphabet[ind]
    print(shifted)





substitution_cipher("WORLD",{'W': 'Q', 'O': 'P', 'R': 'S', 'L': 'T', 'D': 'U'})