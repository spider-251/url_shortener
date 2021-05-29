
import requests
api_key = "61547d4f437acea09687a3a2083df6adedc19"

url = input("Enter the url to shorten: ")

name = input("Enter unique name if any else leave blank: ")

api_url = "https://cutt.ly/api/api.php?key={0}&short={1}&name={2}".format(api_key, url, name)

data = requests.get(api_url).json()["url"]
if data["status"] == 7:
	shortened_url = data["shortLink"]
	print("Shortened Url:", shortened_url)
else:
	print("[!] Error Shortening URL:", data)
