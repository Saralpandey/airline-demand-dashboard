import requests
import pandas as pd

# Replace with your API key
API_KEY = '347227faf957c76b70388c2560108a9f'
BASE_URL = 'http://api.aviationstack.com/v1/flights'

def fetch_flight_data(limit=50):
    params = {
        'access_key': API_KEY,
        'limit': limit
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if 'data' not in data:
        print("❌ Error: No data found.")
        return None

    flights = []
    for flight in data['data']:
        flights.append({
            'airline': flight.get('airline', {}).get('name', 'N/A'),
            'flight_number': flight.get('flight', {}).get('iata', 'N/A'),
            'departure_airport': flight.get('departure', {}).get('airport', 'N/A'),
            'arrival_airport': flight.get('arrival', {}).get('airport', 'N/A'),
            'departure_city': flight.get('departure', {}).get('city', 'N/A'),
            'arrival_city': flight.get('arrival', {}).get('city', 'N/A'),
            'scheduled_departure': flight.get('departure', {}).get('scheduled', 'N/A'),
            'scheduled_arrival': flight.get('arrival', {}).get('scheduled', 'N/A'),
            'status': flight.get('flight_status', 'N/A')
        })

    df = pd.DataFrame(flights)
    df.to_csv('flights_data.csv', index=False)
    print("✅ Flight data saved to flights_data.csv")

if __name__ == "__main__":
    fetch_flight_data()
