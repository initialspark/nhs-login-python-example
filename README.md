# NHS login python demo 

This repo contains a sample application of how to connect to NHS login using python and Flask.

## Prerequisites:

 - Python 3.7
 - pipenv
 - Generated keypair
 - Access to NHS login sandpit

## Getting started:

Create a virtual environment and install packages.
```
    pipenv install
```

Create an .env file in the root of the project and add your client details.

**.env**
```
FLASK_APP=app
NHS_LOGIN_AUTHORITY_URL=https://auth.sandpit.signin.nhs.uk
NHS_LOGIN_CLIENT_ID=YOUR-CLIENT-ID
NHS_LOGIN_SCOPES=openid profile
NHS_LOGIN_CALLBACK_URL=http://localhost:5000/oidc-callback
FLASK_DEBUG=true
```

Add private key to the private_key.pem file

To run the sample, run the following command in the root of the project.
```
    flask run
```

## Note:
> This application is provided as a demo to get started integrating with NHS login and shouldn't be deployed into a production environment :)
