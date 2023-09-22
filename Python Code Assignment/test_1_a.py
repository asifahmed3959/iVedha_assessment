import os
import json
from datetime import datetime

def check_service_status(service_name):
    command = f"systemctl is-active {service_name}.service"
    result = os.system(command)
    return result == 0

def create_json(service_name, service_status, host_name):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    json_data = {
        "service_name": service_name,
        "service_status": service_status,
        "host_name": host_name
    }
    file_name = f"{service_name}-status-{timestamp}.json"

    with open(file_name, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    services = {
        "httpd": "host1",
        "rabbitmqctl": "host1",
        "postgresql": "host1"
    }

    for service_name, host_name in services.items():
        service_status = "UP" if check_service_status(service_name) else "DOWN"
        create_json(service_name, service_status, host_name)