import http.client

conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "2f8a103f4emshe6452ebdc159a90p156155jsn9cd2567b8e5c",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

conn.request("GET", "/onecall/timemachine?lat=52.29958465640118&lon=20.927704121901673&dt=1617843600", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))