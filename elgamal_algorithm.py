##################################################################
#############       Erfan Mohammadzadeh          #################
#############          9622473147                #################
#############         Elgamal Algorithm          #################
##################################################################

import Prime_number
import find_generator
import inverse
import random


def get_data():
	prime = Prime_number.get_data()
	num_g = int(input("Enter a number as g ? "))
	while not find_generator.get_data(prime, num_g):
		num_g = int(input(
				'Error: your Entered number is NOT generator of {}, Please Enter again a number as g ? '.format(prime)))
	num_a = int(input("Enter a secret number as a ? "))
	while prime - 1 < num_a < 1:
		num_a = int(input(
				"Error: your Entered number should be between 1 until {}. Please Enter again a number a s a ? ".format(
						prime - 1)))
	message = int(input("Write your message that want to encrypted ? "))
	return prime, num_g, num_a, message


def compute_first_public_key(prime, num_g, a):
	return pow(num_g, a, prime)


def compute_c_one(prime, num_g, random_num):
	return pow(num_g, random_num, prime)


def compute_c_two(message, a, random_num, prime):
	return (message * a ** random_num) % prime


def decryption(c_1, c_2, a, prime):
	return (inverse.check_conditions(c_1 ** a, prime) * c_2) % prime


if __name__ == "__main__":
	prime_number, number_g, private_number, plain_text = get_data()
	# random_number = random.randint(1, 10000)
	random_number = int(input("Enter K ? "))
	print("\nRandom number (K) is : ", random_number)

	num_A = compute_first_public_key(prime_number, number_g, private_number)
	print("Public key (A) is : ", num_A)

	c_one = compute_c_one(prime_number, number_g, random_number)
	print("c1 is {} ^ {} = {} mod {}  -> c1 = {} ".format(number_g, random_number, c_one, prime_number, c_one))

	c_two = compute_c_two(plain_text, num_A, random_number, prime_number)
	print("c2 is {} * {} ^ {} = {} mod {}  -> c2 = {} ".format(plain_text, number_g, random_number, c_two, prime_number,
	                                                           c_two))
	print("Decrypted message is : ", decryption(c_one, c_two, private_number, prime_number))