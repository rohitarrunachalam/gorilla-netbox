#Example Code for API Usage - Netbox
import requests

# NetBox API endpoint and authentication details 
NETBOX_URL = "https://your-netbox-instance/api/"
NETBOX_TOKEN = "your-api-token"
HEADERS = {
    "Authorization": f"Token {NETBOX_TOKEN}",
    "Content-Type": "application/json",
}

# Function to make a GET request to NetBox API
def get_data(endpoint):
    url = f"{NETBOX_URL}{endpoint}/"
    response = requests.get(url, headers=HEADERS)
    return response.json()

# Function to make a POST request to NetBox API
def create_data(endpoint, data):
    url = f"{NETBOX_URL}{endpoint}/"
    response = requests.post(url, headers=HEADERS, json=data)
    return response.json()

# Function to make a PATCH request to NetBox API (for updating)
def update_data(endpoint, object_id, data):
    url = f"{NETBOX_URL}{endpoint}/{object_id}/"
    response = requests.patch(url, headers=HEADERS, json=data)
    return response.json()

# Function to make a DELETE request to NetBox API
def delete_data(endpoint, object_id):
    url = f"{NETBOX_URL}{endpoint}/{object_id}/"
    response = requests.delete(url, headers=HEADERS)
    return response.status_code


# Get data
devices = get_data("dcim/devices")
print("Devices:", devices)

# Create data
new_device_data = {
    "name": "NewDevice",
    "device_type": 1, 
}
created_device = create_data("dcim/devices", new_device_data)
print("Created Device:", created_device)

# Update data
device_id_to_update = 1  
update_device_data = {
    "name": "UpdatedDevice",
}
updated_device = update_data("dcim/devices", device_id_to_update, update_device_data)
print("Updated Device:", updated_device)

# Delete data
device_id_to_delete = 2  
status_code = delete_data("dcim/devices", device_id_to_delete)
print("Delete Status Code:", status_code)
