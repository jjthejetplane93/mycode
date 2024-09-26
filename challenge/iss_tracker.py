#!/usr/bin/python3

''' Challenge 2 task for python course '''

import requests
import time
import reverse_geocoder as rg

url = "http://api.open-notify.org/iss-now.json"

def main():
    resp = requests.get(url)

    data = resp.json()

    epoch_time = data["timestamp"]


    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epoch_time))

    lat = data["iss_position"].get("latitude")

    lon = data["iss_position"].get("longitude")

    coords_tuple= (lat, lon)

    result = rg.search(coords_tuple, verbose=False)
  
    print(data)

    print("CURRENT LOCATION OF ISS:\n")
    print(f'Timestamp: {formatted_time}')
    print(f'Lon: {lon}')
    print(f'Lat: {lat}')
    print(f'City/Country: {result[0]["name"]}, {result[0]["cc"]}')



if __name__ == "__main__" :
    main()


