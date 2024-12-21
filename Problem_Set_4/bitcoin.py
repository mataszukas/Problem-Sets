import requests
import sys
import json

if len(sys.argv) != 2 or not sys.argv[1].replace(".", "").isnumeric():
    sys.exit(1)

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
result = response.json()
value = result['bpi']['USD']['rate_float'] * float(sys.argv[1])
print(f"{value:,.2f}")
