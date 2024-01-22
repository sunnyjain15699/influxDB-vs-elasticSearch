import datetime
import random
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

INFLUXDB_URL = 'http://localhost:8086'  
INFLUXDB_TOKEN = 'avtoj6qkz1e_JjFn7SRHWDRPy-7TWoIa6Rah7PW7OVhsjxkIFHgT0t1izp4l-C2e0jKmfnCdDH1AkP-BN0mXbQ=='
INFLUXDB_BUCKET = 'self'

def generate_data(start_date, end_date, interval_minutes=1):
    current_date = start_date
    data = []

    while current_date <= end_date:
        data.append({
            'measurement': 'timeseries_data',
            'time': current_date.isoformat(),
            'fields': {
                'value': random.uniform(1, 100) 
            }
        })
        current_date += datetime.timedelta(minutes=interval_minutes)

    return data

def main():
    try:
        client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
        write_api = client.write_api(write_options=SYNCHRONOUS)

        start_date = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end_date = datetime.datetime(2023, 1, 1, 23, 59, 0)
        interval_minutes = 5

        test_data = generate_data(start_date, end_date, interval_minutes)

        write_api.write(INFLUXDB_BUCKET, INFLUXDB_ORG, test_data)

        print(f'Successfully inserted {len(test_data)} points into InfluxDB.')
    
    except Exception as e:
        print(f"Error creating InfluxDB client: {e}")

if __name__ == "__main__":
    main()
