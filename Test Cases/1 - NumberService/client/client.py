import requests
from functools import reduce
import sys
import ipaddress

def request(ip_port, lower_bound, upper_bound):
	query_params = {
		'l': lower_bound,
		'u': upper_bound
	}

	return requests.get('http://{}/random'.format(ip_port), params=query_params)

def _str_is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def _main():
	if len(sys.argv) != 2:
		print('The client should be given exactly 1 argument: the IP and port to contact (in the form IP:port).')
		return

	ip_port = sys.argv[1].split(':')

	try:
		ipaddress.ip_address(ip_port[0])
	except ValueError:
		print('IP address is not valid.')
		return

	if not _str_is_int(ip_port[1]):
		print('Port is not valid.')
		return

	ip_port = sys.argv[1]

	while True:
		answer = input('Send Request?\n')
		print()

		if answer in ['no', 'n', 'exit']:
			break

		nums = input('Lower and upper bounds: ')
		print()

		nums = nums.strip().split(' ')
		valid = len(nums) == 2 and reduce(lambda acc, n: acc and _str_is_int(n), nums, True)

		if not valid:
			print('Input not valid.')
			continue

		lower_bound, upper_bound = nums[0], nums[1]

		if lower_bound > upper_bound:
			print('Lower bound must be < than upper bound.')

		response = request(ip_port, nums[0], nums[1])

		if response.status_code == 500:
			print('The server had an internal error, and its content is: {}'.format(response.content))
		else:
			print('Status code: {}\nContent:\n{}\n'.format(response.status_code, response.json()))

if __name__ == '__main__':
	_main()
