#
#
#
# dadJokes.py

# Notes:    A program that will serach https://icanhazdadjoke.com for jokes on a topic of your choice
#
#		This program requires the Module 'requests' in order to work
#		requests can be imported using pip in your terminal ( or everyone's favorite, Powershell... the joke hurts me on the inside )
#		with the command 'python -m pip install requests'
#
#		Please keep in mind that this is just something i was messing around with in order to use python on the web
#		It does not handle all types of error checking, thanks


print("")
import requests
from random import choice

url = "https://icanhazdadjoke.com/search"

msg = input("What category of jokes are you looking for? ")

response = requests.get(
	url,
	headers = {"Accept": "application/json"},
	params = {"term": msg}
)

data = response.json()
num_jokes = data['total_jokes']
# print("\n", f"found {len(data['results'])} results", "\n")
if num_jokes == 1:
	print("\nFound 1 joke, here it is: \n")
	print(data['results'][0]['joke'])
elif num_jokes > 1:
	print("\n" + f"Found {num_jokes} results, here they are: \n")
	for d in data['results']:
		print(d['joke'], "\n")
else:
	print("\nNo jokes were found, sorry")

print("")
