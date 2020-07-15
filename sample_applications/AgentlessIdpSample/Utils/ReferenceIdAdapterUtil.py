from sample_applications.AgentlessIdpSample.Utils.IdpConstants import IdpConstants
import sample_applications.AgentlessIdpSample.Utils.UrlUtil as UrlUtil
from sample_applications.AgentlessIdpSample.Configuration.ConfigurationManager import ConfigurationManager
import base64;


def session_response(headers, response):
    output = ''
    for header_key in headers:
        output += header_key + ": " + headers[header_key] + "\n"
    output += "\n"
    output += response
    return output


def pickup_request(reference_id):
    username = ConfigurationManager.get_configuration(IdpConstants.ADAPTER_USERNAME)
    password = ConfigurationManager.get_configuration(IdpConstants.ADAPTER_PASSWORD)

    return "GET " + UrlUtil.pickup_url(reference_id) + "\n" \
           + IdpConstants.PING_ADAPTER_HEADER + ": " \
           + ConfigurationManager.get_configuration(IdpConstants.ADAPTER_ID) + "\n" \
           + "Authentication: " + base64.b64encode((username + ":" + password).encode('ascii')).decode('ascii')


def http_status(status_code):
    if status_code == 200:
        return "HTTP Status: 200 OK"
    else:
        return "HTTP Status: " + str(status_code)


def dropoff_post(user_attributes):
    username = ConfigurationManager.get_configuration(IdpConstants.ADAPTER_USERNAME)
    password = ConfigurationManager.get_configuration(IdpConstants.ADAPTER_PASSWORD)

    return "POST " + UrlUtil.dropoff_url() + "\n" \
           + "Content-Type: application/json\n" \
           + "Content-Length: " + str(len(user_attributes)) + "\n" \
           + IdpConstants.PING_ADAPTER_HEADER + ": " \
           + ConfigurationManager.get_configuration(IdpConstants.ADAPTER_ID) + "\n" \
           + "Authentication: " + base64.b64encode((username + ":" + password).encode('ascii')).decode('ascii') + "\n" \
           + "\n" \
           + user_attributes
