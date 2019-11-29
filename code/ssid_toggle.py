""" Enable/Disable Wifi on a Meraki Network """

import requests

# ****** START EDIT THIS ******

api_key = "24faa954e9ae4c856fb4c96798e177aa1816d760"  # Replace with your API key
network_id = "L_646829496481104046"  # Replace with your Network ID
ssid_number = "1"  # Replace with your ssid number to edit

# ****** STOP EDIT THIS  ******

url = "https://api.meraki.com/api/v0/networks/{}/ssids/{}".format(
    network_id, ssid_number
)

headers = {"X-Cisco-Meraki-API-Key": api_key}
payload = {
    "name": "Wifi Name Here",
    "enabled": "true",
}

response = requests.request("PUT", url, data=payload, headers=headers)

print("\nAPI Response: \n{}".format(response.text))
print("\nStatus code: {}".format(response.status_code))
