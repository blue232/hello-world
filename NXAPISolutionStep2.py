#!/usr/bin/env python

import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

	auth = HTTPBasicAuth('cisco', 'cisco')
	headers = {
		'Content-Type': 'application/json'
	}
payload = {
	"ins_api": {
		"version": "1.0",
		"type": "cli_show",
		"chunk": "0",
		"sid": "1",
		"input": "show interface Mgmt0",
		"output_format": "json"
	}
}
url = 'http://nxosv/ins'

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
rx_object = json.loads(response.text)

interface = rx_object['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']

print "Management Interface Information:"
print "IP Address: " + interface['eth_ip_addr'] + '/' + str(interface['eth_ip_mask'])
print "Speed: ", interface['eth_speed']
print "State: ", interface['state']
print "MTU: ", interface['eth_mtu']

#  The following allows you to see the json fields

print json.dumps(rx_object,indent=4)