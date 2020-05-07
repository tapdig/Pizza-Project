import hashlib, binascii, os

class Hash:
	def __init__(self):
		pass

	def hash_password(password):
		salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
		pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
		pwdhash = binascii.hexlify(pwdhash)
		return (salt + pwdhash).decode('ascii')

	def verify_password(stored_password, provided_password):
		copypwd = stored_password
		salt = stored_password[:64]
		stored_password = stored_password[64:]
		pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
		pwdhash = binascii.hexlify(pwdhash).decode('ascii')
		if pwdhash == stored_password:
			return copypwd
		else:
			return False
			