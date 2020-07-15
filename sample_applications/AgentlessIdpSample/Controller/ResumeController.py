from sample_applications.AgentlessIdpSample.Controller.RequestController import RequestController
from flask import redirect
import sample_applications.AgentlessIdpSample.Utils.UrlUtil as UrlUtil


class ResumeController(RequestController):

    def handle(self, request):
        return redirect(UrlUtil.resume_to_pf_url(request), code=302)
