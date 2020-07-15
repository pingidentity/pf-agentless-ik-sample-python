import requests

from sample_applications.AgentlessSpSample.Configuration.ConfigurationManager import ConfigurationManager
from sample_applications.AgentlessSpSample.Utils import UrlUtil
from sample_applications.AgentlessSpSample.Utils.SpConstants import SpConstants


def pickup_attributes(reference_value):
    # Pickup the attributes from PingFederate
    pickup_location = UrlUtil.pickup_url(reference_value)
    username = ConfigurationManager.get_configuration(SpConstants.ADAPTER_USERNAME)
    password = ConfigurationManager.get_configuration(SpConstants.ADAPTER_PASSWORD)

    headers = {
        SpConstants.PING_ADAPTER_HEADER: ConfigurationManager.get_configuration(SpConstants.ADAPTER_ID)
    }

    # For simplicity, trust any certificate. Do not use in production.
    return requests.get(pickup_location, headers=headers, auth=(username, password), verify=False)

