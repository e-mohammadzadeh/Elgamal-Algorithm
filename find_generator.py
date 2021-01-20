##################################################################
#############       Erfan Mohammadzadeh          #################
#############          9622473147                #################
#############     Generator number of prime      #################
##################################################################


def get_data(prime_number, generator_number):
	f_star_prime = {index for index in range(1, prime_number)}
	if is_generator(prime_number, generator_number, f_star_prime):
		return True
	return False


def is_generator(prime_number, generator_number, f_star_prime):
	return {pow(generator_number, index, prime_number) for index in range(0, prime_number - 1)} == f_star_prime


if __name__ == "__main__":
	get_data()
