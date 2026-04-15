import sys
#the request package allows for talking to the internet using API 
import requests

# Check command-line arguments
if len(sys.argv) != 2:
#this sys.exit help to print error messages and stop a program
    sys.exit("Missing command-line argument")

# Convert argument to float
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# API URL 
url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=4d0894b7494f69eb8b65a7c021cb0bd600194319fff79dc46efef51e90ad66a1"

try:
    response = requests.get(url)
    data = response.json()

    price = float(data["data"]["priceUsd"])

except requests.RequestException:
    sys.exit("Error fetching data")

# Calculate total cost
total = price * n

# Print formatted result
print(f"${total:,.4f}")
