import sample_applications.AgentlessSpSample.Utils.UrlUtil as UrlUtil
from sample_applications.AgentlessSpSample.Configuration.ConfigurationManager import ConfigurationManager
from sample_applications.AgentlessSpSample.Utils.SpConstants import SpConstants
import base64


def pickup_request(reference_id):
    username = ConfigurationManager.get_configuration(SpConstants.ADAPTER_USERNAME)
    password = ConfigurationManager.get_configuration(SpConstants.ADAPTER_PASSWORD)

    return "GET " + UrlUtil.pickup_url(reference_id) + "\n" \
           + SpConstants.PING_ADAPTER_HEADER + ": " \
           + ConfigurationManager.get_configuration(SpConstants.ADAPTER_ID) + "\n" \
           + "Authentication: " + base64.b64encode((username + ":" + password).encode('ascii')).decode('ascii')


def session_response(headers, response):
    output = ''
    for header_key in headers:
        output += header_key + ": " + headers[header_key] + "\n"
    output += "\n"
    output += response
    return output


def http_status(status_code):
    if status_code == 200:
        return "HTTP Status: 200 OK"
    else:
        return "HTTP Status: " + str(status_code)
