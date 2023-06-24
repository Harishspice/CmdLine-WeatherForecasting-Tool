# Import all the required modules
import requests,argparse,sys
from termcolor import colored
import datetime

# Set the api key
api_key = '31202685856b1c9c27eaa9897d8c15b6'

# Create a function to get the weather forecast for a city
def get_weather_forecast_city(api_key, city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        forecast_data = response.json()

        if forecast_data['cod'] == 200:
            return forecast_data

        return None
    except requests.RequestException:
        print(f"Unable to get weather forecast for {city}")
        sys.exit(1)


# Create a function to get the weather forecast for latitude and longitude
def get_weather_forecast_lat_long(api_key, latitude, longitude):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
        response = requests.get(url)
        forecast_data = response.json()
        if forecast_data['cod'] == 200:
            return forecast_data

        return None
    except requests.RequestException:
        print(f"Unable to get weather forecast for {latitude} and {longitude}")
        sys.exit(1)


# Finding public ip address
def get_public_ip():
    try:
        url = 'https://api.ipify.org?format=json'
        response = requests.get(url)
        data = response.json()
        return data['ip']
    except requests.RequestException:
        print(f"Unable to get IP address.")
        sys.exit(1)


# Find latitude and longitude from ip address
def get_lat_long(ip_address):
    try:
        url = f"https://freegeoip.app/json/{ip_address}"
        response = requests.get(url)
        data = response.json()
        return data['latitude'], data['longitude']
    except requests.RequestException:
        print(f"Unable to get latitude and longitude.")
        sys.exit(1)

# Function to print known cities and unknown cities
def print_city(forcast_json):
    city=forecast_json['name']
    country=forecast_json['sys']['country']
    print('-'*50)
    if not city:
        print('            CITY:',colored('Unknown','green'))
        print('-'*50)
        print('         COUNTRY:',colored('Unknown','green'))
    elif not country:
        print('            CITY:',colored(forecast_json['name'],'green'))
        print('-'*50)
        print('         COUNTRY:',colored('Unknown','green'))
    else:
        print('            CITY:',colored(forecast_json['name'],'green'))
        print('-'*50)
        print('         COUNTRY:',colored(forecast_json['sys']['country'],'green'))

# Create a function for formatting raw data into a readable format in verbose mode  
def print_forecast_verbose(forecast_json):
    print_city(forecast_json)
    sunrise_datetime = datetime.datetime.fromtimestamp(forecast_json['sys']['sunrise'])
    sunset_datetime = datetime.datetime.fromtimestamp(forecast_json['sys']['sunset'])

    sunrise_datetime += datetime.timedelta(seconds=forecast_json['timezone'])
    sunset_datetime += datetime.timedelta(seconds=forecast_json['timezone'])

    print('\nLATITUDE:',colored(forecast_json['coord']['lat'],'green'),'\nLONGITUDE:',colored(forecast_json['coord']['lon'],'green'))
    print('SUNRISE:',colored(sunrise_datetime,'green'),'\nSUNSET:',colored(sunset_datetime,'green'))

    f_min=kelvin_to_fahrenheit(forecast_json['main']['temp_min'])
    f_max=kelvin_to_fahrenheit(forecast_json['main']['temp_max'])
    c_min=kelvin_to_celsius(forecast_json['main']['temp_min'])
    c_max=kelvin_to_celsius(forecast_json['main']['temp_max'])
    print('\nMINIMUM TEMPERATURE:',colored(f'{c_min:.2f}°C','green'),'\n',colored(f'{f_min:.2f}°F','green'))
    print('MAXIMUM TEMPERATURE:',colored(f'{c_max:.2f}°C','green'),'\n',colored(f'{f_max:.2f}°F','green'))
    cel=kelvin_to_celsius(forecast_json['main']['temp'])
    fahrenheit=kelvin_to_fahrenheit(forecast_json['main']['temp'])
    print('TEMPERATURE:',colored(f'{cel:.2f}°C','green'),'\t',colored(f'{fahrenheit:.2f}°F','green'))
    print('HUMIDITY:',colored(forecast_json['main']['humidity'],'green'),'%')
    print('DESCRIPTION:',colored(forecast_json['weather'][0]['description'],'green'))

    print('\nPRESSURE:',colored(forecast_json['main']['pressure'],'green'),'hPa')
    print('VISIBILITY:',colored(forecast_json['visibility'],'green'),'meters')
    print('WIND SPEED:',colored(forecast_json['wind']['speed'],'green'),'m/s')
    print('WIND DIRECTION:',colored(forecast_json['wind']['deg'],'green'),'degrees')
    print('-'*50)

# Create a function for formatting raw data into a readable format in normal mode
def print_forecast(forecast_json):
    print_city(forecast_json)
    cel=kelvin_to_celsius(forecast_json['main']['temp'])
    fahrenheit=kelvin_to_fahrenheit(forecast_json['main']['temp'])
    print('\nTEMPERATURE:',colored(f'{cel:.2f}°C','green'),'\t',colored(f'{fahrenheit:.2f}°F','green'))
    print('HUMIDITY:',colored(str(forecast_json['main']['humidity'])+'%','green'))
    print('DESCRIPTION:',colored(forecast_json['weather'][0]['description'],'green'))
    print('-'*50)

# Create a function for converting kelvin to celsius
def kelvin_to_celsius(temperature):
    return temperature - 273.15

# Function for converting kelvin to fahrenheit
def kelvin_to_fahrenheit(temperature):
    return (temperature - 273.15) * 9 / 5 + 32

# Parsing arguments
parser=argparse.ArgumentParser()

parser.add_argument('city', nargs='?', help='Enter the city name')
parser.add_argument('-c', '--city_option', dest='city', help=argparse.SUPPRESS)
parser.add_argument('-lat','--latitude',type=float,help='Enter the latitude')
parser.add_argument('-long','--longitude',type=float,help='Enter the longitude')
parser.add_argument('-v','--verbose',help='Verbose mode',action='store_true')
args=parser.parse_args()

# Calling appropriate functions based on the arguments provided

if (not any(vars(args).values())) or (args.latitude and not args.longitude) or (args.longitude and not args.latitude):
    ip_address = get_public_ip()
    latitude, longitude = get_lat_long(ip_address)
    forecast_json = get_weather_forecast_lat_long(api_key, latitude, longitude)
    print(colored('!!!Not Enough Details Provided!!!','red'))
    print(colored('Using your IP address to find the forecast.','green'))
    print(colored('!!!Response may not be accurate!!!','red'))
    if forecast_json and args.verbose:
        print_forecast_verbose(forecast_json)
        sys.exit(1)
    elif forecast_json:
        print_forecast(forecast_json)
        sys.exit(1)
    else:
        print("Failed to fetch the forecast.")
        sys.exit(1)
        
if args.verbose:
    if args.city:
        forecast_json=get_weather_forecast_city(api_key,args.city)
        if forecast_json:
            print_forecast_verbose(forecast_json)
        else:
            print("Failed to fetch the forecast.")
            sys.exit(1)
    elif args.latitude and args.longitude:
            forecast_json=get_weather_forecast_lat_long(api_key,args.latitude,args.longitude)
            if forecast_json:
                print_forecast_verbose(forecast_json)
            else:
                print("Failed to fetch the forecast.")
                sys.exit(1)

    else:
        parser.print_help()
        sys.exit(1)
else:
    if args.latitude and args.longitude:
        forecast_json=get_weather_forecast_lat_long(api_key,args.latitude,args.longitude)
        if forecast_json:
            print_forecast(forecast_json)
        else:
            print("Failed to fetch the forecast.")
            sys.exit(1)
    elif args.city:
        forecast_json=get_weather_forecast_city(api_key,args.city)
        if forecast_json:
            print_forecast(forecast_json)
        else:
            print("Failed to fetch the forecast.")
            sys.exit(1)
    
    else:
        parser.print_help()
        sys.exit(1)
