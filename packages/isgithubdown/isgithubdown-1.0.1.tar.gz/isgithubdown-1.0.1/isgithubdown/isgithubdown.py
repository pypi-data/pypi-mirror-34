import requests

def main():
	endpoint = 'https://isitup.org/github.com.json'
	response = requests.get(endpoint, verify = True)

	data = response.json()

	if data['status_code'] == 1: # Up
		print('\n 🐈  It\'s up. Go back to work!')

	if data['status_code'] == 2: # Down
		print('\n 🦄  It\'s down. Go outside!')
