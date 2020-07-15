from flask import render_template
import json

from sample_applications.AgentlessSpSample.Controller.RequestController import RequestController
import sample_applications.AgentlessSpSample.Utils.ReferenceIdAdapterUtil as ReferenceIdAdapterUtil
import sample_applications.AgentlessSpSample.Utils.PickupUtil as PickupUtil
from sample_applications.AgentlessSpSample.Utils.SpConstants import SpConstants
import sample_applications.AgentlessSpSample.Utils.UrlUtil as UrlUtil


class AppController(RequestController):

    def handle(self, request):
        if request.method == 'POST':
            reference_value = request.form[SpConstants.REF]

            response = PickupUtil.pickup_attributes(reference_value)
            response_json = json.dumps(response.json(), indent=4)

            return render_template('Pickup.html',
                                   configureUrl=UrlUtil.configure_url(request),
                                   httpStatus=ReferenceIdAdapterUtil.http_status(response.status_code),
                                   pickupEndpoint=SpConstants.PICKUP_ENDPOINT,
                                   rawRequest=ReferenceIdAdapterUtil.pickup_request(reference_value),
                                   REF=reference_value,
                                   rawResponse=ReferenceIdAdapterUtil.session_response(response.headers, response_json),
                                   responseBody=response_json,
                                   ssoUrl=UrlUtil.sso_url(),
                                   sloUrl=UrlUtil.slo_url(request),
                                   spSsoEndpoint=SpConstants.SP_SLO_ENDPOINT)
        else:
            return render_template('Pickup.html',
                                   showData=None,
                                   configureUrl=UrlUtil.configure_url(request),
                                   ssoUrl=UrlUtil.sso_url())

