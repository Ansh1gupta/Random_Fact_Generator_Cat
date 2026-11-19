
import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

# Extract only the fact
fact = data["fact"]

print("\n🐱 Random Animal Fact:")
print(fact)
