import requests
from pprint import pprint
import sys

city=input("city name : ")

api_address="http://api.openweathermap.org/data/2.5/weather?appid=3d66914bcc86db27bb63a5ca22a25910&q="      #API 1 for forecasting
url=api_address+city
jsn1 = requests.get(url).json()     #json data for forecasting

lat=str(jsn1['coord']['lat'])
lon=str(jsn1['coord']['lon'])
pred_url="https://api.darksky.net/forecast/6e835c027c0d20f4017c090a434081e7/"+lat+","+lon      #API 2 for weather prediction url
jsn2 = requests.get(pred_url).json()       #json data for prediction

def o():
    x=input('\nDo you wanna continue (y/n) : ')       
    if(x=='y'):
        print("\n")
        
    elif(x=='n'):
        print("Thank You")
        sys.exit()
    else:
        print("Invalid Input")
        o()

while True:
    print("\n******************MENU******************")
    print("1. Weather")
    print("2. Pressure")
    print("3. Wind speed")
    print("4. Humidity")
    print("5. Minimum and Maximum Temperatures")
    print("6. UV Index")
    print("7. 2 Day Forecast ")
    print("8. Whole week summary")
    print("9. Quit")

    choice=input("Enter your choice : ")

    if choice=='1':
        formatted_data=jsn1['weather'][0]['main']
        data1=jsn2['currently']['summary']        
        print("\nCurrent weather : "+formatted_data)
        print("Summary : "+data1)

    elif choice=='2':
        formatted_data=str(jsn1['main']['pressure'])
        print("\nPressure : "+formatted_data+" hpa")

    elif choice=='3':
        formatted_data=str(jsn1['wind']['speed'])
        print("\nWind Speed : "+formatted_data+" m/s")

    elif choice=='4':
        formatted_data=str(jsn1['main']['humidity'])
        print("\nHumidity : "+formatted_data+" %")

    elif choice=='5':
        data1=jsn1['main']['temp_max']
        data2=jsn1['main']['temp_min']
        data3=jsn1['main']['temp']
        maxm=str(data1-273.15)
        minm=str(data2-273.15)
        curr=str(data3-273.15)
        print("\nMaximum Temperature "+maxm+" degree celsius")
        print("Minimum Temperature "+minm+" degree celcius")
        print("Currently feels "+curr+" degree celcius")

    elif choice=='6':
        formatted_data = str(jsn2['currently']['uvIndex'])
        print("\nUV Index : "+formatted_data)

    elif choice=='7':
        for i in range(1,3):
            print("\n{} day(s) from today".format(i))
            data1=jsn2['daily']['data'][i]['temperatureHigh']
            s=(data1-32)*(5/9)
            s=str(s)            
            print("\nHigh Temperature : "+s+" degree celcius")
            data2=jsn2['daily']['data'][i]['temperatureLow']
            q=(data2-32)*(5/9)
            q=str(q)
            print("Low Temperature : "+q+" degree celcius")
            data3=jsn2['daily']['data'][i]['summary']
            print(data3+"\n")


    elif choice=='8':
        data1=jsn2['daily']['summary']
        print("\nWhole week summary : "+data1)        

    elif choice=='9':
        break
    
    else:
        print("Invalid Choice.")        
    
    o()

