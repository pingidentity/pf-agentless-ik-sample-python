from sample_applications.AgentlessIdpSample.Configuration.ConfigurationManager import ConfigurationManager
from sample_applications.AgentlessIdpSample.Utils.IdpConstants import IdpConstants
import urllib.parse as url


def configure_url(request):
    return request.url_root + IdpConstants.AGENTLESS_BASE + "/configure"


def login_url(request):
    return request.url_root + IdpConstants.AGENTLESS_BASE + "/login"


def resume_url(request):
    return request.url_root + IdpConstants.AGENTLESS_BASE + "/resume"


def resume_to_pf_url(request):
    return ConfigurationManager.get_configuration(IdpConstants.BASE_PF_URL) + request.form[IdpConstants.RESUME_PATH] \
           + "?REF=" + request.form[IdpConstants.REF] + "&TargetResource=" \
           + url.quote_plus(ConfigurationManager.get_configuration(IdpConstants.TARGET_URL))


def resume_logout_url(request, reference_id):
    return ConfigurationManager.get_configuration(IdpConstants.BASE_PF_URL) + request.form[IdpConstants.RESUME_PATH] \
           + "?REF=" + reference_id


def sso_url():
    return ConfigurationManager.get_configuration(IdpConstants.BASE_PF_URL) + IdpConstants.START_SP_SSO \
           + "?PartnerIdpId=" + ConfigurationManager.get_configuration(IdpConstants.PARTNER_ENTITY_ID)


def pickup_url(reference_id):
    return ConfigurationManager.get_configuration(IdpConstants.BASE_PF_URL) \
           + IdpConstants.PICKUP_ENDPOINT \
           + "?REF=" + reference_id


def dropoff_url():
    return ConfigurationManager.get_configuration(IdpConstants.BASE_PF_URL) \
           + IdpConstants.DROPOFF_ENDPOINT
