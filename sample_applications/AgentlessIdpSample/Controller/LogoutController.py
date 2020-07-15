import json

import requests
from flask import render_template

from sample_applications.AgentlessIdpSample.Controller.RequestController import RequestController
from sample_applications.AgentlessIdpSample.Utils import PickupUtil
from sample_applications.AgentlessIdpSample.Utils.IdpConstants import IdpConstants
import sample_applications.AgentlessIdpSample.Utils.UrlUtil as UrlUtil
import sample_applications.AgentlessIdpSample.Utils.ReferenceIdAdapterUtil as ReferenceAdapterUtil


class LogoutController(RequestController):

    def handle(self, request):
        if request.method == 'POST':
            reference_value = request.form[IdpConstants.REF]

            response = PickupUtil.pickup_attributes(reference_value)
            response_json = json.dumps(response.json(), indent=4)

            return render_template('Logout.html',
                                   resumeUrl=UrlUtil.resume_logout_url(request, reference_value),
                                   resumePath=request.form['resumePath'],
                                   ssoUrl=UrlUtil.sso_url(),
                                   httpStatus=ReferenceAdapterUtil.http_status(response.status_code),
                                   REF=reference_value,
                                   pickupEndpoint=IdpConstants.PICKUP_ENDPOINT,
                                   configureUrl=UrlUtil.configure_url(request),
                                   responseBody=response_json,
                                   rawRequest=ReferenceAdapterUtil.pickup_request(reference_value),
                                   rawResponse=ReferenceAdapterUtil.session_response(response.headers, response_json))
        else:
            return render_template('Error.html',
                                   configureUrl=UrlUtil.configure_url(request),
                                   ssoUrl=UrlUtil.sso_url())
