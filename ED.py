from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import base64
import os

def encryption(privateInfo, key):
	BLOCK_SIZE = 16
	PADDING = '{'

	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

	cipher = AES.new(key)

	encoded = EncodeAES(cipher, privateInfo)
	return str(encoded)

def decryption(encryptedString, key):
	PADDING = '{'
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	cipher = AES.new(key)
	decoded = DecodeAES(cipher, encryptedString)
	return str(decoded)






def getKey(password):
	hasher = SHA256.new(password)
	return str(hasher.digest())
