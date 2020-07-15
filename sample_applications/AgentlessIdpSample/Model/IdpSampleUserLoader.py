import json
import os

from sample_applications.AgentlessIdpSample.Utils.IdpConstants import IdpConstants


class IdpSampleUserLoader:

    users = dict()

    @classmethod
    def __init__(cls):
        current_dir = os.path.dirname(__file__)
        rel_path = "Configuration/idp-sample-users.json"
        config_dir = os.path.join(current_dir, "..", rel_path)
        with open(config_dir) as file:
            cls.users = json.load(file)

    @classmethod
    def get_user(cls, username):
        for user in cls.users:
            if user.get(IdpConstants.ADAPTER_USERNAME) == username:
                return user
        return None
