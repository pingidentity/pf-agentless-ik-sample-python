from flask import render_template, redirect

from sample_applications.AgentlessIdpSample.Controller.RequestController import RequestController
from sample_applications.AgentlessIdpSample.Controller.DropoffController import DropoffController
from sample_applications.AgentlessIdpSample.Utils.IdpConstants import IdpConstants
from sample_applications.AgentlessIdpSample.Model.Authenticator import Authenticator
import sample_applications.AgentlessIdpSample.Utils.UrlUtil as UrlUtil


class LoginController(RequestController):

    def handle(self, request):
        if request.method == 'POST':
            if Authenticator.authenticate(request.form[IdpConstants.USERNAME], request.form[IdpConstants.PASSWORD]):
                return DropoffController().handle(request)
            else:
                return render_template('Login.html',
                                       showData=None,
                                       loginError="Invalid Login.",
                                       resumePath=request.form[IdpConstants.RESUME_PATH])
        else:
            return redirect(UrlUtil.sso_url(), code=302)
