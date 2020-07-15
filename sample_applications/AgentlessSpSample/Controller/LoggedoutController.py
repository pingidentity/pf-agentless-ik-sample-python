from flask import render_template

from sample_applications.AgentlessSpSample.Controller.RequestController import RequestController
import sample_applications.AgentlessSpSample.Utils.UrlUtil as UrlUtil


class LoggedoutController(RequestController):

    def handle(self, request):

        return render_template('Loggedout.html',
                               IdpSsoUrl=UrlUtil.sso_url(),
                               SpSsoUrl=UrlUtil.application_sso_url(request))
