import datetime
import random
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

ELASTICSEARCH_HOST = 'localhost'
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_INDEX = 'timeseries_data'
USER = 'elastic'
PASS = '3VYJpGDUc_GAAHCjSs-Q'

def generate_data(start_date, end_date, interval_minutes=1):
    current_date = start_date
    data = []

    while current_date <= end_date:
        data.append({
            '_index': ELASTICSEARCH_INDEX,
            '_source': {
                'timestamp': current_date,
                'value': random.uniform(1, 100)  
            }
        })
        current_date += datetime.timedelta(minutes=interval_minutes)

    return data

def create_index(es):
    index_settings = {
        'mappings': {
            'properties': {
                'timestamp': {'type': 'date'},
                'value': {'type': 'float'}
            }
        }
    }

    es.indices.create(index=ELASTICSEARCH_INDEX, body=index_settings, ignore=400)

def main():
    try:
        es = Elasticsearch([
            {'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT ,'scheme':'https'}
            ],  basic_auth=(USER, PASS), verify_certs=False)
        
       
        create_index(es)

        start_date = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end_date = datetime.datetime(2023, 1, 1, 23, 59, 0)
        interval_minutes = 5

        test_data = generate_data(start_date, end_date, interval_minutes)

        success, failed = bulk(es, test_data)

        print(f'Successfully inserted {success} documents. Failed to insert {failed} documents.')
    
    except Exception as e:
        print(f"Error creating Elasticsearch client: {e}")

if __name__ == "__main__":
    main()
