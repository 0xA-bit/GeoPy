import pandas as pd
import requests
import json
import time

# Specify the file path
df = pd.read_excel("./FilesCsv/TEST123.xlsx") 

for i, row in df.iterrows():

#filter special char & Specify the file header of location

    df['Registered_Address'] = df['Registered_Address'].str.replace(r'\W',"")

#Getting the coordinates (Specifying the header location) note: Specify the file header of location
    containerApi = str(df.at[i, 'Registered_Address'])

#Data in xlsx & Specify the file header of location to print out along with the location and coordinates 
    list = (str(df.at[i,'Company_name'])) + "\n" + (str(df.at[i,'product']))

    parameters = {
        "key" : "t0apq29knAwoZjceW7sUGco1rIj6kupy",
        "location" : containerApi
    }
    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params = parameters)

#error markings (optional)
    errorLat1 = 6.48812 
    errorLng1 = 2.6138

    data = json.loads(response.text)['results']
    lat = data[0]['locations'][0]['latLng']['lat']
    lng = data[0]['locations'][0]['latLng']['lng']

    df.at[i, 'lat'] = lat
    df.at[i, 'lng'] = lng

    time.sleep(1.5)
    print(list)
    print(containerApi)
    time.sleep(1.5)
    print(lat, lng)

#Condition to error markings (optional)
    if lat == errorLat1:
        if lng == errorLng1:
            try:
                print("NA")
            except:
                pass
        try:
            print("NA")
        except:
                pass
    print('\n')

#Saving the result output note: Specify the file path
    df.to_excel('./Output/TEST123.xlsx')





