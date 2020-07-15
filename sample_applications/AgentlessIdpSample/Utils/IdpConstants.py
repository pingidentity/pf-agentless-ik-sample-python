class IdpConstants:
    # endpoints
    PICKUP_ENDPOINT = "/ext/ref/pickup"
    DROPOFF_ENDPOINT = "/ext/ref/dropoff"
    AGENTLESS_BASE = "AgentlessIdPSample/app"
    START_SP_SSO = "/sp/startSSO.ping"

    # attribute keys
    SUBJECT = "subject"
    AUTH_INST = "authnInst"

    # POST keys
    USERNAME = "username"
    PASSWORD = "password"
    REF = "REF"
    RESUME_PATH = "resumePath"
    CURRENT_BASE_URL = "currentBaseUrl"

    # adapter configuration keys
    CONFIG_SECTION = "idpAdapterConfiguration"
    BASE_PF_URL = "basePfUrl"
    ADAPTER_USERNAME = "username"
    ADAPTER_PASSWORD = "passphrase"
    ADAPTER_ID = "adapterId"
    TARGET_URL = "targetURL"
    PARTNER_ENTITY_ID = "partnerEntityId"

    # PF headers
    PING_UNAME_HEADER = "ping.uname"
    PING_PASSWORD_HEADER = "ping.pwd"
    PING_ADAPTER_HEADER = "ping.instanceId"
