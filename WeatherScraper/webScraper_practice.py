import pandas as pd
import requests
from bs4 import BeautifulSoup 



#website for weather in 07726 areea code
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.287352152038586&lon=-74.33490482130163#.Xx8AVi85TUo')
soup = BeautifulSoup(page.content, 'html.parser')
#for exact location of wanted data
week = soup.find(id='seven-day-forecast-body')


#this contains all the information
items = week.find_all(class_='tombstone-container')

#this is a test to get all information
#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())


#to get all period names, short description, temp
period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperature = [item.find(class_='temp').get_text() for item in items]

#print(period_names)
#print(short_descriptions)
#print(temperature)



#created a dictionary that will store values neatly
weather_stuff = pd.DataFrame(
	{
		'period': period_names,
		'short_descriptions': short_descriptions,
		'temperature': temperature
	})
print(weather_stuff)

weather_stuff.to_csv('weatherData.cvs')
