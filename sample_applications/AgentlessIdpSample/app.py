from flask import Flask, request
from sample_applications.AgentlessIdpSample.Configuration.ConfigurationManager import ConfigurationManager
from sample_applications.AgentlessIdpSample.Controller.AppController import AppController
from sample_applications.AgentlessIdpSample.Controller.LoginController import LoginController
from sample_applications.AgentlessIdpSample.Controller.LogoutController import LogoutController
from sample_applications.AgentlessIdpSample.Controller.ResumeController import ResumeController
from sample_applications.AgentlessIdpSample.Controller.ConfigurationController import ConfigurationController


app = Flask(__name__)


@app.route('/AgentlessIdPSample/app', methods=['POST', 'GET'])
def index():
    controller = AppController()
    return controller.handle(request)


@app.route('/AgentlessIdPSample/app/login', methods=['POST', 'GET'])
def login():
    controller = LoginController()
    return controller.handle(request)


@app.route('/AgentlessIdPSample/app/resume', methods=['POST'])
def resume():
    controller = ResumeController()
    return controller.handle(request)


@app.route('/AgentlessIdPSample/app/logout', methods=['POST', 'GET'])
def logout():
    controller = LogoutController()
    return controller.handle(request)


@app.route('/AgentlessIdPSample/app/configure', methods=['POST', 'GET'])
def configure():
    controller = ConfigurationController()
    return controller.handle(request)


if __name__ == "__main__":
    ConfigurationManager()
    app.run(host='127.0.0.1', port=8080, ssl_context='adhoc')
