import configparser
import requests

from datetime import datetime

from flask import Flask, request, jsonify

# from elasticsearch import Elasticsearch, helpers


app = Flask(__name__)

#elastic search configuration
config = configparser.ConfigParser()
config.read('example.ini')
# es = Elasticsearch(
#     cloud_id=config['ELASTIC']['cloud_id'],
#     http_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
# )
elastic_search_url = config['ELASTIC']['host']
AUTH = (config['ELASTIC']['user'], config['ELASTIC']['password'])
VERIFY = False

# Get today's date and format it as YYYY-MM-DD
TODAY_DATE = datetime.today().strftime('%Y-%m-%d')


#post method for adding the service status into the elastic search
@app.route('/add', methods=['POST'])
def add_to_elasticsearch():
    INDEX_NAME = f'healthcheck/_doc/{TODAY_DATE}' #INDEXING BASED ON THE DATE, SO WE CAN SPECIFICALLY QUERY THE STATUS CONDITION BASED ON THE DATE
    URL = elastic_search_url + INDEX_NAME
    BODY = request.get_json()
    response = requests.post(url=URL, auth=AUTH, verify=False, json=BODY)
    return jsonify(response.json())

#get the status of all the health check in elastic search
@app.route('/healthcheck', methods=['GET'])
def get_all_application_status():
    INDEX_NAME = f'healthcheck/_search'
    URL = elastic_search_url + INDEX_NAME
    response = requests.get(url=URL, auth=AUTH, verify=False)
    if response.status_code == 200:
        hits = response.json().get('hits', {}).get('hits', [])
        application_statuses = [{"service_name": hit['_source']['service_name'], "service_status": hit['_source']['service_status']} for hit in hits]
        return jsonify(application_statuses)
    return jsonify(response.json())

# #providing a service name get all the status files of that service using elastic search
@app.route('/healthcheck/<service_name>', methods=['GET'])
def get_specific_application_status(service_name):
    INDEX_NAME = f'healthcheck/_search'
    URL = elastic_search_url + INDEX_NAME
    BODY = {
        "query" : {
            "match": { "service_name": service_name }
        }
    }
    response = requests.post(url=URL, auth=AUTH, verify=False, json=BODY)
    if response.status_code == 200:
        hits = response.json().get('hits', {}).get('hits', [])
        application_statuses = [{"service_name": hit['_source']['service_name'], "service_status": hit['_source']['service_status']} for hit in hits]
        return jsonify(application_statuses)
    return jsonify(response.json())


#running the web service
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)