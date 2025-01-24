import argparse
import ast
import json

from FetchClass import SWAPIClient
from SWAPIDataManager import SWAPIDataManager

client = SWAPIClient(base_url="https://swapi.dev/api/")
manager = SWAPIDataManager(client)

parser = argparse.ArgumentParser(description='My simple echo')
parser.add_argument('--endpoint', '-e', help='Text before', default='people,planets')
parser.add_argument('--filters', '-f', help='Text after', default='{"people": ["films", "species"], "planets": ["films", "residents"]}')
parser.add_argument('--output', '-o', help='Text after', default='swapi_data.xlsx')

args = parser.parse_args()
endpoints = args.endpoint.split(',')

try:
    some_dict = ast.literal_eval(args.filters)
    print("Parsed dictionary:", some_dict)
    for endpoint in endpoints:
        manager.fetch_entity(endpoint)
        manager.apply_filter(endpoint, some_dict[endpoint])
    manager.save_to_excel(args.output)
except json.JSONDecodeError as e:
    print("Invalid JSON format:", e)

