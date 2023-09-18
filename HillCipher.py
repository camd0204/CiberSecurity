def hill_cipher_encrypt(plaintext, key):
    # Ensure the length of the plaintext is a multiple of 2
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    # Define a helper function to convert a letter to its numeric value (A=0, B=1, ..., Z=25)
    def letter_to_numeric(letter):
        return ord(letter) - ord('A')

    # Define a helper function to convert a numeric value to a letter
    def numeric_to_letter(numeric):
        return chr(numeric + ord('A'))

    # Initialize the ciphertext
    ciphertext = ''

    # Iterate through the plaintext in pairs
    for i in range(0, len(plaintext), 2):
        # Extract the current pair of letters
        pair = plaintext[i:i+2]

        # Convert the pair of letters to numeric values
        numeric_pair = [letter_to_numeric(pair[0]), letter_to_numeric(pair[1])]

        # Multiply the numeric pair by the key matrix
        result = [0, 0]
        for j in range(2):
            for k in range(2):
                result[j] += numeric_pair[k] * key[k][j]
            result[j] %= 26

        # Convert the resulting numeric pair back to letters and append to the ciphertext
        ciphertext += numeric_to_letter(result[0]) + numeric_to_letter(result[1])

    return ciphertext

# Example usage:
plaintext = "HELLOWORLD"
key = [[2, 3], [1, 4]]
ciphertext = hill_cipher_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
