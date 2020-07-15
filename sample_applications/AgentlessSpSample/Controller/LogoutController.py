from flask import render_template
import json

from sample_applications.AgentlessSpSample.Controller.RequestController import RequestController
import sample_applications.AgentlessSpSample.Utils.ReferenceIdAdapterUtil as ReferenceIdAdapterUtil
from sample_applications.AgentlessSpSample.Utils.SpConstants import SpConstants
import sample_applications.AgentlessSpSample.Utils.UrlUtil as UrlUtil
import sample_applications.AgentlessSpSample.Utils.PickupUtil as PickupUtil


class LogoutController(RequestController):

    def handle(self, request):
        if request.method == 'POST':
            reference_value = request.form[SpConstants.REF]

            response = PickupUtil.pickup_attributes(reference_value)
            response_dict = json.loads(response.text)
            response_json = json.dumps(response.json(), indent=4)

            return render_template('Logout.html',
                                   resumePath=response_dict[SpConstants.RESUME_PATH],
                                   configureUrl=UrlUtil.configure_url(request),
                                   httpStatus=ReferenceIdAdapterUtil.http_status(response.status_code),
                                   pickupEndpoint=SpConstants.PICKUP_ENDPOINT,
                                   rawRequest=ReferenceIdAdapterUtil.pickup_request(reference_value),
                                   REF=reference_value,
                                   rawResponse=ReferenceIdAdapterUtil.session_response(response.headers, response_json),
                                   responseBody=response_json,
                                   redirectUrl=UrlUtil.resume_logout_url(response.json(), reference_value),
                                   ssoUrl=UrlUtil.sso_url())
        else:
            return render_template('Error.html',
                                   configureUrl=UrlUtil.configure_url(request),
                                   ssoUrl=UrlUtil.sso_url())
