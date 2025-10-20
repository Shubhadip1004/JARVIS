import urllib.request
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city_name, is_online):
    
    if not is_online:
        return ["Offline mode: Cannot retrieve weather data.", False]
    
    else:
        weather_api_key = os.getenv("weather_api_key")
        try:
            base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
            url = f"{base_url}{urllib.parse.quote(city_name)}?key={weather_api_key}&unitGroup=metric&contentType=json&include=days,alerts,current,events"
            report = []
            with urllib.request.urlopen(url) as response:
            # Parse the JSON response
                data = json.loads(response.read().decode("utf-8"))
                
                # Print a brief summary of the weather data
                report += [f"Weather for {data['resolvedAddress']}"]
                report += ["Current Temperature: {}°C".format(data['currentConditions']['temp'])]

                report += ["Upcoming Days:"]
                for day in data['days']:
                    report += ["{}: {}, High: {}°C, Low: {}°C".format(day['datetime'], day['description'], day['tempmax'], day['tempmin'])]

                if 'alerts' in data and data['alerts']:
                    report += ["Alerts:"]
                    for alert in data['alerts']:
                        report += ["Alert: {}, Description: {}".format(alert['event'], alert['description'])]
                return [report , True]
        except Exception as e:
            return ["Error retrieving weather data: {}".format(e), False]
        
