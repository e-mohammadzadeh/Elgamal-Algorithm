##################################################################
#############       Erfan Mohammadzadeh          #################
#############          9622473147                #################
#############         Prime Numbers              #################
##################################################################

def is_prime(num):
	if num > 1:
		for index in range(2, num + 1 // 2):
			if num % index == 0:
				return False
		return True
	else:
		return False


def get_data():
	prime_number = int(input("Enter a prime number as p ? "))
	while not is_prime(prime_number):
		prime_number = int(input("ERROR : your entered number is NOT prime, Please Enter again a prime number : "))
	return prime_number


if __name__ == "__main__":
	get_data()
