# REST APIs for Network Automation

## Introduction

### What is a REST API

2. Install Python https://www.python.org/downloads/
3. Download the code in this Git Repository.

## Meraki API

[Meraki](https://meraki.cisco.com/) is a cloud based networking solution from Cisco. You are going to use the Meraki cloud API to programmatically make changes to a Meraki sandbox network.

Meraki employs an 'API first' development strategy where any new features must have an associated API to allow easy control, modification and automation.

The Meraki API follows the [Open API specification](https://www.openapis.org/) and has extensive documentation here: https://developer.cisco.com/meraki/api/#/rest

## Using Postman for API calls

### Prerequisites

1. Install the Postman graphical API call software. https://www.getpostman.com/
2. Activate a Meraki Enterprise Sandbox from Cisco DevNet. https://devnetsandbox.cisco.com/ ![Meraki Sandbox Image](images/meraki-sandbox.png "Meraki Enterprise DevNet Sandbox")
3. TODO https://developer.cisco.com/meraki/build/meraki-postman-collection-getting-started/ GET API Key

### Get the Meraki Postman Collection

Meraki provides a Postman collection that contains pre-defined methods for integrating with the Meraki API.

1. Go to http://postman.meraki.com and click 'Run in Postman'.
2. On the 'open with...' Dialogue select your installed version of Postman.
3. The Meraki Postman Collection should now import.

If you have any issues importing and using the Postman collection you can find more information [here](https://developer.cisco.com/meraki/build/meraki-postman-collection-getting-started/).

## Using Python for API calls

### Prerequisites

1. Download the code in this Git Repository.
2. Install Python https://www.python.org/downloads/
3. Activate a Meraki Enterprise Sandbox from Cisco DevNet. https://devnetsandbox.cisco.com/ (You may have done this in the previous Postman Module) ![Meraki Sandbox Image](images/meraki-sandbox.png "Meraki Enterprise DevNet Sandbox")
