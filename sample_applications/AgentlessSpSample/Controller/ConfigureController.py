from sample_applications.AgentlessSpSample.Controller.RequestController import RequestController
from flask import render_template, redirect
import sample_applications.AgentlessSpSample.Utils.UrlUtil as UrlUtil
from sample_applications.AgentlessSpSample.Utils.SpConstants import SpConstants
from sample_applications.AgentlessSpSample.Configuration.ConfigurationManager import ConfigurationManager


class ConfigurationController(RequestController):

    def handle(self, request):
        if request.method == 'GET':
            return render_template('Configuration.html',
                                   configurationError=None,
                                   configureUrl=UrlUtil.configure_url(request),
                                   basePfUrlName=SpConstants.BASE_PF_URL,
                                   basePfUrl=ConfigurationManager.get_configuration(SpConstants.BASE_PF_URL),
                                   adapterUsernameName=SpConstants.ADAPTER_USERNAME,
                                   adapterUsername=ConfigurationManager.get_configuration(
                                       SpConstants.ADAPTER_USERNAME),
                                   adapterPassphraseName=SpConstants.ADAPTER_PASSWORD,
                                   adapterPassphrase=ConfigurationManager.get_configuration(
                                       SpConstants.ADAPTER_PASSWORD),
                                   adapterIdName=SpConstants.ADAPTER_ID,
                                   adapterId=ConfigurationManager.get_configuration(SpConstants.ADAPTER_ID),
                                   targetUrlName=SpConstants.TARGET_URL,
                                   targetUrl=ConfigurationManager.get_configuration(SpConstants.TARGET_URL),
                                   partnerIdName=SpConstants.PARTNER_ENTITY_ID,
                                   partnerId=ConfigurationManager.get_configuration(SpConstants.PARTNER_ENTITY_ID))
        else:
            try:
                ConfigurationManager.save_configuration(request)
                ConfigurationManager.load_configuration()
                return redirect(UrlUtil.sso_url(), code=302)
            except Exception as e:
                return render_template('Configuration.html',
                                       configurationError=e,
                                       configureUrl=UrlUtil.configure_url(request),
                                       basePfUrlName=SpConstants.BASE_PF_URL,
                                       basePfUrl=request.form[SpConstants.BASE_PF_URL],
                                       adapterUsernameName=SpConstants.ADAPTER_USERNAME,
                                       adapterUsername=request.form[SpConstants.ADAPTER_USERNAME],
                                       adapterPassphraseName=SpConstants.ADAPTER_PASSWORD,
                                       adapterPassphrase=request.form[SpConstants.ADAPTER_PASSWORD],
                                       adapterIdName=SpConstants.ADAPTER_ID,
                                       adapterId=request.form[SpConstants.ADAPTER_ID],
                                       targetUrlName=SpConstants.TARGET_URL,
                                       targetUrl=request.form[SpConstants.TARGET_URL],
                                       partnerIdName=SpConstants.PARTNER_ENTITY_ID,
                                       partnerId=request.form[SpConstants.PARTNER_ENTITY_ID])

