""" Turns port 3 on Greg's home Meraki MS Switch on/off """
import requests

# ****** START EDIT THIS ******

api_key = "2bf631da51c6ae66dfd1710110b2ba3b8ffbbe6f"  # Replace with your API key
device_serial = "L_662029145223464938"  # Replace with your Device ID
port_number = "3"  # Replace with your port number to edit

# ****** STOP EDIT THIS  ******

url = "https://api.meraki.com/api/v0/devices/{}/switchPorts/{}".format(
    device_serial, port_number
)

headers = {"X-Cisco-Meraki-API-Key": "2bf631da51c6ae66dfd1710110b2ba3b8f5bbe6f"}
payload = {"enabled": "true"}

response = requests.request("PUT", url, data=payload, headers=headers)

print("\nAPI Response: \n{}".format(response.text))
print("\nStatus code: {}".format(response.status_code))
