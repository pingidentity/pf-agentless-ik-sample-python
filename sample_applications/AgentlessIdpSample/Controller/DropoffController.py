from flask import render_template
import requests
import json
from datetime import datetime

import sample_applications.AgentlessIdpSample.Utils.ReferenceIdAdapterUtil as ReferenceAdapterUtil
from sample_applications.AgentlessIdpSample.Controller.RequestController import RequestController
from sample_applications.AgentlessIdpSample.Utils.IdpConstants import IdpConstants
from sample_applications.AgentlessIdpSample.Model.IdpSampleUserLoader import IdpSampleUserLoader
import sample_applications.AgentlessIdpSample.Utils.UrlUtil as UrlUtil
from sample_applications.AgentlessIdpSample.Configuration.ConfigurationManager import ConfigurationManager


class DropoffController(RequestController):

    def handle(self, request):
        username = request.form[IdpConstants.USERNAME]
        # create dictionary containing user attributes
        idp_user_attributes = dict.get(IdpSampleUserLoader.get_user(username), "attributes")
        idp_user_attributes.update({IdpConstants.SUBJECT: username})
        idp_user_attributes.update({IdpConstants.AUTH_INST: datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")})

        # Drop the attributes into PingFederate
        dropoff_location = UrlUtil.dropoff_url()
        username = ConfigurationManager.get_configuration(IdpConstants.ADAPTER_USERNAME)
        password = ConfigurationManager.get_configuration(IdpConstants.ADAPTER_PASSWORD)

        headers = {
            "Content-type": "application/json",
            IdpConstants.PING_ADAPTER_HEADER: ConfigurationManager.get_configuration(IdpConstants.ADAPTER_ID)
        }

        # For simplicity, trust any certificate. Do not use in production.
        response = requests.post(dropoff_location, json=idp_user_attributes, auth=(username, password), headers=headers, verify=False)
        response_dict = json.loads(response.text)
        response_json = json.dumps(response.json(), indent=4)

        idp_user_attributes = json.dumps(idp_user_attributes, indent=4)

        return render_template('Dropoff.html',
                               resumePath=request.form[IdpConstants.RESUME_PATH],
                               resumeUrl=UrlUtil.resume_url(request),
                               REF=response_dict[IdpConstants.REF],
                               configureUrl=UrlUtil.configure_url(request),
                               userAttributes=idp_user_attributes,
                               httpStatus=ReferenceAdapterUtil.http_status(response.status_code),
                               dropoffEndpoint=IdpConstants.DROPOFF_ENDPOINT,
                               ssoUrl=UrlUtil.sso_url(),
                               rawRequest=ReferenceAdapterUtil.dropoff_post(idp_user_attributes),
                               rawResponse=ReferenceAdapterUtil.session_response(response.headers, response_json))

