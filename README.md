<p align="center">
    <img src="https://assets.pingone.com/ux/end-user/0.14.0/images/ping-logo.svg" height="150" width="150" />
</p>

# PingFederate Agentless Integration Kit Sample Applications for Python

## Overview

These sample applications let you test an integration with the Agentless Integration Kit. PingFederate acts as both the identity provider (IdP) and service provider (SP), showing the complete end-to-end configuration and user experience.

The package includes two independent Python web applications, one for each of the IdP and SP roles. You can see the source code and deploy the applications easily using the built-in Flask development server.
The included PingFederate configuration archive allows a single instance of PingFederate to run both sample applications.

<p align="center">
    <img src="/images/example.gif"/>
</p>

## System requirements and dependencies

* PingFederate 8.x or later
* PingFederate Agentless Integration Kit 1.5 or later
* Python 3.5 or later

### Browser compatibility

The samples work with all major browsers, including Chrome, Firefox, and Microsoft Edge.

## Setup

### Deploying the PingFederate configuration archive
The included configuration archive creates the adapter instances and connections needed to run the sample applications.

To deploy the configuration archive, import the `configuration_archive/data.zip` file through the administrator console or copy it to the drop-in-deployer directory. For instructions, see [Configuration archive](https://docs.pingidentity.com/csh?Product=pf-latest&topicname=oor1564002974031.html) in the PingFederate documentation.

**Caution:** Deploying the configuration archive will destroy your existing PingFederate configuration. We recommend that you deploy it on a fresh installation of PingFederate or back up your current configuration as shown in [Exporting an archive](https://docs.pingidentity.com/csh?Product=pf-latest&topicname=amd1564002974196.html) in the PingFederate documentation.

### Running the applications
You can run the applications within the Python-provided development application server.

1. If you want to use a hostname and port other than `https://localhost:8080` for the IdP sample application and `https://localhost:8081`
for the SP sample application, make the following changes.
   1. Modify the `app.py` file in `sample_applications/AgentlessIdPSample` for the IdP application, and equivalent file for the SP application.
   2. Modify the adapter and connection configurations in PingFederate.
2. Go to the root directory of the project.
3. Install the necessary Python dependencies by entering the following command: `pip3 install -r requirements.txt`
4. In the `sample_applications/AgentlessIdpSample` directory, start the IdP application by entering the following command. Adjust the `PYTHONPATH` value as needed.
`PYTHONPATH=<path_to_pf-agentless-ik-sample-python_directory> python3 app.py`
5. Start the SP application by repeating step 4 from the `AgentlessSpSample` directory.
6. In your browser, go to the following URL to start IdP single sign-on flow: `https://localhost:9031/sp/startSSO.ping?PartnerIdpId=PF-DEMO`

## Modifying your application
When you are ready to make changes to your own application, see the examples in the `example_code` directory to help you get started.

## Documentation

For the latest documentation, see [Agentless Integration Kit](https://docs.pingidentity.com/bundle/integrations/page/ygj1563994984859.html) in the Ping Identity [Support Home](https://support.pingidentity.com/s/).

## Known limitations

To keep the app simple and focused on interactions with PingFederate, it does not support browser page refreshes.

## Reporting bugs

Please use this project's issue tracker to report any bugs.

## License

This project is licensed under the Apache license. See the [LICENSE](LICENSE) file for more information.