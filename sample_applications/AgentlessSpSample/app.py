from flask import Flask, request

from sample_applications.AgentlessSpSample.Controller.AppController import AppController
from sample_applications.AgentlessSpSample.Controller.LoggedoutController import LoggedoutController
from sample_applications.AgentlessSpSample.Controller.LogoutController import LogoutController
from sample_applications.AgentlessSpSample.Controller.ConfigureController import ConfigurationController
from sample_applications.AgentlessSpSample.Configuration.ConfigurationManager import ConfigurationManager

app = Flask(__name__)


@app.route('/AgentlessSPSample/app', methods=['POST', 'GET'])
def index():
    controller = AppController()
    return controller.handle(request)


@app.route('/AgentlessSPSample/app/logout', methods=['POST', 'GET'])
def logout():
    controller = LogoutController()
    return controller.handle(request)


@app.route('/AgentlessSPSample/app/loggedout', methods=['GET'])
def loggedout():
    controller = LoggedoutController()
    return controller.handle(request)


@app.route('/AgentlessSPSample/app/configure', methods=['POST', 'GET'])
def configure():
    controller = ConfigurationController()
    return controller.handle(request)


if __name__ == '__main__':
    ConfigurationManager()
    app.run(host='127.0.0.1', port=8081, ssl_context='adhoc')
