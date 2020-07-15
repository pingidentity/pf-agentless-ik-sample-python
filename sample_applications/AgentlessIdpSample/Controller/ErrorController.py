from flask import render_template
from sample_applications.AgentlessIdpSample.Controller.RequestController import RequestController


class ErrorController(RequestController):

    def handle(self, request):
        return render_template('Error.html')

