import requests
from bs4 import BeautifulSoup

url = "https://www.imperva.com/learn/application-security/web-scraping-attack/"

response = requests.get(url)

if response.status_code == 200:
	soup = BeautifulSoup(response.text, "html.parser")

	title = soup.title.text if soup.title else "no title"
	print(f"page title: {title}")

	links = soup.find_all("a")
	for link in links:
		href = link.get("href")
		if href:
			print(f"link: {href}")

else:
	print(f"error: {response.status_code}")
