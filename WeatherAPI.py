import requests
import sys
import pandas as pd
sys.stdout=open("output.out","w")
"593656324a7c8d128d351b91a0609d24"
URL="https://api.openweathermap.org/data/2.5/weather"
Parameter={"appid":"593656324a7c8d128d351b91a0609d24",'id':"1273865"}
Coimbatore=requests.get(URL,params=Parameter)
Parameter={"appid":"593656324a7c8d128d351b91a0609d24",'id':"1273294"}
Delhi=requests.get(URL,params=Parameter)
Parameter={"appid":"593656324a7c8d128d351b91a0609d24",'id':"1273874"}
Cochin=requests.get(URL,params=Parameter)
def kelvinTocelciusconverter(response):
	json=response.json()
	temp_max1=json['main']['temp_max']
	temp_min1=json['main']['temp_min']
	temp_max1=temp_max1-273
	temp_min1=temp_min1-273
	json["main"]["temp_max"]=round(temp_max1,2)
	json["main"]["temp_min"]=round(temp_min1,2)
	return json
Coimbatore=kelvinTocelciusconverter(Coimbatore)
Delhi=kelvinTocelciusconverter(Delhi)
Cochin=kelvinTocelciusconverter(Cochin)
wind=[]
wind.append(Coimbatore['wind']['speed'])
wind.append(Cochin['wind']['speed'])
wind.append(Delhi['wind']['speed'])
minTemps=[]
minTemps.append(Coimbatore['main']['temp_min'])
minTemps.append(Delhi['main']['temp_min'])
minTemps.append(Cochin['main']['temp_min'])
maxTemps=[]
maxTemps.append(Coimbatore['main']['temp_max'])
maxTemps.append(Delhi['main']['temp_max'])
maxTemps.append(Cochin['main']['temp_max'])
cities=[]
cities.append(Coimbatore['name'])
cities.append(Delhi['name'])
cities.append(Cochin['name'])
DataSet={"Cities":cities,"Min-Temp":minTemps,"Max-Temp":maxTemps,"WindSpeed":wind}
DF=pd.DataFrame(DataSet)
import matplotlib.pyplot as plt 
DF.plot(kind='bar',x='Cities',y="WindSpeed")
plt.show()
