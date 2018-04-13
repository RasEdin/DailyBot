# Project: DailyBot
# FileName: WeatherApiController
# Current User: Rasmus laptop
# Date Created: 09/03/2018
# Developed in PyCharm

# import requests to use the openweathermap.org api
import requests

class WeatherApiController():

    # Change app_id value to be a folder on the raspberry pi once the file has been transfered.
    file = open('C:\\Users\\Rasmus laptop\\Keys and IDs for education purposes\\DailyBotWeatherAPI_Key.txt','r')
    api_adress = 'http://api.openweathermap.org/data/2.5/weather?appid='+file.read()+'&q='
    city = input("City Name :")

    url = api_adress + city

    json_data = requests.get(url).json()
    formatted_data_weather = json_data['weather'][0]['main']
    formatted_data_main = json_data['main']['temp']

    # Kelvin to Celsius conversion
    formatted_data_main = formatted_data_main - 273.15

    def getTemp(self):

        weather_temp = self.formatted_data_main
        return format(weather_temp, '0.1f')+" degrees celsius"

    def getWeather(self):

        the_weather= self.formatted_data_weather
        return the_weather

#print('*****************************************')
#x = WeatherApiController()
#print(x.getTemp())
#print(x.getWeather())