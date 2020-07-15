from sample_applications.AgentlessIdpSample.Model.IdpSampleUserLoader import IdpSampleUserLoader
from sample_applications.AgentlessIdpSample.Utils.IdpConstants import IdpConstants


class Authenticator:

    @staticmethod
    def authenticate(username, password):
        user = IdpSampleUserLoader.get_user(username)
        if user is None:
            return False
        elif user.get(IdpConstants.PASSWORD) != password:
            return False
        else:
            return True

