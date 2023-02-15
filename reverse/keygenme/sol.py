import hashlib

def main():
	index = [4, 5, 3, 6, 2, 7, 1, 8]
	username = b'GOUGH'
	flag_1 = "picoCTF{1n_7h3_|<3y_of_"

	dynamic = ""

	for i in index:
		dynamic += hashlib.sha256(username).hexdigest()[i]
	flag = flag_1 + dynamic + '}'

	print(flag)

if __name__ == "__main__":

	main()