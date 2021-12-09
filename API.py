import requests
response=requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")

print(response)
