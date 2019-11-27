""" Enable/Disable Guest Wifi on a Meraki Network """

import requests

# ****** START EDIT THIS ******

api_key = "2bf631da51c6ae66dfd1710110b2ba3b8ffbbe6f"  # Replace with your API key
network_id = "L_662029145223464938"  # Replace with your Network ID
ssid_number = "1"  # Replace with your ssid number to edit

# ****** STOP EDIT THIS  ******

url = "https://api.meraki.com/api/v0/networks/{}/ssids/{}".format(
    network_id, ssid_number
)

headers = {"X-Cisco-Meraki-API-Key": "2bf631da51c6ae66dfd1710110b2ba3b8f5bbe6f"}
payload = {
    "name": "Guest Wifi",
    "enabled": "false",
}

response = requests.request("PUT", url, data=payload, headers=headers)

print("\nAPI Response: \n{}".format(response.text))
print("\nStatus code: {}".format(response.status_code))
