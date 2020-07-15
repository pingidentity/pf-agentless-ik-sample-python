# install requests (i.e. `pip3 install requests`)
import requests

# create dictionary containing user attributes
idp_user_attributes = {"attribute1": "value1"}

# Drop the attributes into PingFederate
dropoff_location = "https://localhost:9031/ext/ref/dropoff"
headers = {"Content-type": "application/json",
           "ping.uname": "changeme",
           "ping.pwd": "please change me before you go into production!",
           "ping.instanceId": "idpadapter"}

# For simplicity, trust any certificate. Do not use in production.
response = requests.post(dropoff_location, json=idp_user_attributes, headers=headers, verify=False).json()

print(response['REF'])
