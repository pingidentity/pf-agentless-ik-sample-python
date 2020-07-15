# install requests (i.e. `pip3 install requests`)
import requests

reference_value = "<INSERT REFERENCE VALUE HERE>"

# Pickup the attributes from PingFederate
pickup_location = "https://localhost:9031/ext/ref/pickup?REF=" + reference_value
headers = {"ping.uname": "changeme",
           "ping.pwd": "please change me before you go into production!",
           "ping.instanceId": "spadapter"}

# For simplicity, trust any certificate. Do not use in production.
response = requests.get(pickup_location, headers=headers, verify=False).json()

print(response)
