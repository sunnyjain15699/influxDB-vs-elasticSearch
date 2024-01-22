# TRYING TO INSERT 45million record.

from datetime import datetime, timedelta
from elasticsearch import Elasticsearch, helpers
import uuid
import random

# Elasticsearch settings
ELASTICSEARCH_HOST = 'localhost'
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_INDEX = 'time_45milli'
USER = 'elastic'
PASS = '3VYJpGDUc_GAAHCjSs-Q'


# Function to generate test data
def generate_data(number_of_entries):
    data = []

    for _ in range(number_of_entries):
        timestamp = datetime.utcnow() - timedelta(days=random.randint(1, 7), hours=random.randint(0, 23))
        project_uuid = str(uuid.uuid4())
        status_code = random.choice([200, 404, 500])  # Adjust status codes as needed
        status_code_type = str(status_code // 100) + 'xx'
        user_agent = 'Chrome Mobile'
        user_agent_type = 'mobile'

        entry = {
            'time': timestamp,
            'value': random.uniform(1, 100),  # Replace with your own data generation logic
            'project': project_uuid,
            'statusCode': status_code,
            'statusCodeType': status_code_type,
            'userAgent': user_agent,
            'userAgentType': user_agent_type
        }

        data.append(entry)

    return data

# Function to bulk insert data into Elasticsearch
def bulk_insert(es, data):
    actions = [
        {
            '_op_type': 'index',
            '_index': ELASTICSEARCH_INDEX,
            '_source': entry
        }
        for entry in data
    ]

    helpers.bulk(es, actions)

# Main function
def main():
    try:
        es = Elasticsearch([
            {'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT ,'scheme':'https'}
            ],  basic_auth=(USER, PASS), verify_certs=False)

        # Create Elasticsearch index (you may want to customize the index settings)
        es.indices.create(index=ELASTICSEARCH_INDEX, ignore=400)

        # Generate test data
        number_of_entries = 45000000
        test_data = generate_data(number_of_entries)

        # Bulk insert data into Elasticsearch
        bulk_insert(es, test_data)

        print(f'Successfully inserted {number_of_entries} documents into Elasticsearch.')

    except Exception as e:
        print(f"Error inserting data into Elasticsearch: {e}")

if __name__ == "__main__":
    main()
