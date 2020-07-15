from sample_applications.AgentlessSpSample.Configuration.ConfigurationManager import ConfigurationManager
from sample_applications.AgentlessSpSample.Utils.SpConstants import SpConstants
import urllib.parse as url


def configure_url(request):
    return request.url_root + SpConstants.AGENTLESS_BASE + "/configure"


def resume_logout_url(response, reference_id):
    return ConfigurationManager.get_configuration(SpConstants.BASE_PF_URL) + response[SpConstants.RESUME_PATH] \
           + "?REF=" + reference_id


def sso_url():
    return ConfigurationManager.get_configuration(SpConstants.BASE_PF_URL) \
           + SpConstants.SP_SSO_ENDPOINT + "?PartnerIdpId=" \
           + ConfigurationManager.get_configuration(SpConstants.PARTNER_ENTITY_ID)


def application_sso_url(request):
    return request.url_root + SpConstants.AGENTLESS_BASE


def slo_url(request):
    return ConfigurationManager.get_configuration(SpConstants.BASE_PF_URL) \
           + SpConstants.SP_SLO_ENDPOINT + "?TargetResource=" \
           + url.quote_plus(request.url_root + SpConstants.AGENTLESS_BASE + "/loggedout")


def pickup_url(reference_id):
    return ConfigurationManager.get_configuration(SpConstants.BASE_PF_URL) \
           + SpConstants.PICKUP_ENDPOINT \
           + "?REF=" + reference_id
