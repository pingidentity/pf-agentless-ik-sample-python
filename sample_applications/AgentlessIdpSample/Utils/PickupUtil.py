import requests

from sample_applications.AgentlessIdpSample.Configuration.ConfigurationManager import ConfigurationManager
from sample_applications.AgentlessIdpSample.Utils import UrlUtil
from sample_applications.AgentlessIdpSample.Utils.IdpConstants import IdpConstants


def pickup_attributes(reference_value):
    # Pickup the attributes from PingFederate
    pickup_location = UrlUtil.pickup_url(reference_value)
    username = ConfigurationManager.get_configuration(IdpConstants.ADAPTER_USERNAME)
    password = ConfigurationManager.get_configuration(IdpConstants.ADAPTER_PASSWORD)

    headers = {
        IdpConstants.PING_ADAPTER_HEADER: ConfigurationManager.get_configuration(IdpConstants.ADAPTER_ID)
    }

    # For simplicity, trust any certificate. Do not use in production.
    return requests.get(pickup_location, headers=headers, auth=(username, password), verify=False)
