import requests as req

def cv(country):
	res = req.get(https://api.covid19.api.com/summary/)
	
	if res.status_code != 200:
		return f"Request Failed - {res}"
	
	found = list(filter(lambda entry: entry["Country"] == country, res.json()["Countries"]))
	
	if len(found) == 0:
		return f"Invalid Country - {country}"
	
	data = found[0]
	
    return f"""
{country} COVID-19 Informations
Total Confirmed : {data["TotalConfirmed"]}
Total Deaths    : {data["TotalDeaths"]}
New Confirmed   : {data["NewConfirmed"]}
New Deaths      : {data["NewDeaths"]}
"""

print(cv(input("Enter country name : ")))
