from flask import Flask, request, jsonify
from azure.cosmos import CosmosClient
import os
import time

app = Flask(__name__)

# Configurações do Azure Cosmos DB
endpoint = os.getenv("COSMOS_ENDPOINT")
key = os.getenv("COSMOS_KEY")
client = CosmosClient(endpoint, key)
database_name = 'HealthMonitoring'
container_name = 'SensorData'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    pressure = data.get('pressure')
    glucose = data.get('glucose')
    
    item = {
        'id': str(time.time()),  # ID único
        'pressure': pressure,
        'glucose': glucose,
        'timestamp': time.time()
    }
    container.create_item(item)
    
    return jsonify({'status': 'success'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
