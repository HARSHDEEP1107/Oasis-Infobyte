import requests
api_key='e5ee298c20a1f388dd9f751428599b6c'
user_input=input("Enter city:")
weather_data=requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q=(user_input)&units=imperial&APPID={api_key}"
)
if weather_data.json()['cod']=='404':
    print("No City Found")
else:    
     weather=weather_data.json()['weather'][0]['main']
     temp=weather_data.json()['main']['temp']
     print("The weather in {user_input} is:{weather}")
     print("The temperature in {user_input} is:{temp} F")