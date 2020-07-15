from sample_applications.AgentlessIdpSample.Controller.RequestController import RequestController
from flask import render_template, redirect
import sample_applications.AgentlessIdpSample.Utils.UrlUtil as UrlUtil
from sample_applications.AgentlessIdpSample.Utils.IdpConstants import IdpConstants
from sample_applications.AgentlessIdpSample.Configuration.ConfigurationManager import ConfigurationManager


class ConfigurationController(RequestController):

    def handle(self, request):
        if request.method == 'GET':
            return render_template('Configuration.html',
                                   configurationError=None,
                                   configureUrl=UrlUtil.configure_url(request),
                                   basePfUrlName=IdpConstants.BASE_PF_URL,
                                   basePfUrl=ConfigurationManager.get_configuration(IdpConstants.BASE_PF_URL),
                                   adapterUsernameName=IdpConstants.ADAPTER_USERNAME,
                                   adapterUsername=ConfigurationManager.get_configuration(
                                       IdpConstants.ADAPTER_USERNAME),
                                   adapterPassphraseName=IdpConstants.ADAPTER_PASSWORD,
                                   adapterPassphrase=ConfigurationManager.get_configuration(
                                       IdpConstants.ADAPTER_PASSWORD),
                                   adapterIdName=IdpConstants.ADAPTER_ID,
                                   adapterId=ConfigurationManager.get_configuration(IdpConstants.ADAPTER_ID),
                                   targetUrlName=IdpConstants.TARGET_URL,
                                   targetUrl=ConfigurationManager.get_configuration(IdpConstants.TARGET_URL),
                                   partnerIdName=IdpConstants.PARTNER_ENTITY_ID,
                                   partnerId=ConfigurationManager.get_configuration(IdpConstants.PARTNER_ENTITY_ID))
        else:
            try:
                ConfigurationManager.save_configuration(request)
                ConfigurationManager.load_configuration()
                return redirect(UrlUtil.sso_url(), code=302)
            except Exception as e:
                return render_template('Configuration.html',
                                       configurationError=e,
                                       configureUrl=UrlUtil.configure_url(request),
                                       basePfUrlName=IdpConstants.BASE_PF_URL,
                                       basePfUrl=request.form[IdpConstants.BASE_PF_URL],
                                       adapterUsernameName=IdpConstants.ADAPTER_USERNAME,
                                       adapterUsername=request.form[IdpConstants.ADAPTER_USERNAME],
                                       adapterPassphraseName=IdpConstants.ADAPTER_PASSWORD,
                                       adapterPassphrase=request.form[IdpConstants.ADAPTER_PASSWORD],
                                       adapterIdName=IdpConstants.ADAPTER_ID,
                                       adapterId=request.form[IdpConstants.ADAPTER_ID],
                                       targetUrlName=IdpConstants.TARGET_URL,
                                       targetUrl=request.form[IdpConstants.TARGET_URL],
                                       partnerIdName=IdpConstants.PARTNER_ENTITY_ID,
                                       partnerId=request.form[IdpConstants.PARTNER_ENTITY_ID])
