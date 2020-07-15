class SpConstants:
    # endpoints
    PICKUP_ENDPOINT = "/ext/ref/pickup"
    SP_SSO_ENDPOINT = "/sp/startSSO.ping"
    SP_SLO_ENDPOINT = "/sp/startSLO.ping"
    AGENTLESS_BASE = "AgentlessSPSample/app"

    # POST keys
    REF = "REF"
    RESUME_PATH = "resumePath"
    CURRENT_BASE_URL = "currentBaseUrl"

    # adapter configuration keys
    CONFIG_SECTION = "spAdapterConfiguration"
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
