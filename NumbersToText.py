def numbers_cipher(plaintext):
    alphabet = ['.','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    word=""
    for number in plaintext:
        word+=alphabet[number]
    print(word)

numbers_cipher([16,9,3,15,3,20,6])
numbers_cipher([20,8,5,14,21,13,2,5,18,19,13,1,19,15,14])

