from sample_applications.AgentlessIdpSample.Controller.RequestController import RequestController
from flask import render_template, redirect
import json

import sample_applications.AgentlessIdpSample.Utils.ReferenceIdAdapterUtil as ReferenceAdapterUtil
from sample_applications.AgentlessIdpSample.Utils.IdpConstants import IdpConstants
import sample_applications.AgentlessIdpSample.Utils.UrlUtil as UrlUtil
import sample_applications.AgentlessIdpSample.Utils.PickupUtil as PickupUtil


class AppController(RequestController):

    def handle(self, request):
        if request.method == 'POST':
            reference_value = request.form[IdpConstants.REF]

            response = PickupUtil.pickup_attributes(reference_value)
            response_json = json.dumps(response.json(), indent=4)

            return render_template('Login.html',
                                   resumePath=request.form[IdpConstants.RESUME_PATH],
                                   REF=reference_value,
                                   responseBody=response_json,
                                   pickupEndpoint=IdpConstants.PICKUP_ENDPOINT,
                                   configureUrl=UrlUtil.configure_url(request),
                                   loginUrl=UrlUtil.login_url(request),
                                   httpStatus=ReferenceAdapterUtil.http_status(response.status_code),
                                   rawRequest=ReferenceAdapterUtil.pickup_request(reference_value),
                                   rawResponse=ReferenceAdapterUtil.session_response(response.headers, response_json),
                                   loginError=None)
        else:
            return redirect(UrlUtil.sso_url(), code=302)
