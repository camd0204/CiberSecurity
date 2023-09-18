import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def b16_decode(ciphered):
	enc=""
	for i in range(0,len(ciphered),2):
		binary="{0:04b}".format(ALPHABET.index(ciphered[i]))+"{0:04b}".format(ALPHABET.index(ciphered[i+1]))
		enc+=chr(int(binary,2))
	return enc


def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

for key in ALPHABET:
	dec=""
	for c in flag:
		dec+=shift(c,key)
	b16=b16_decode(dec)
	print(key,b16)
