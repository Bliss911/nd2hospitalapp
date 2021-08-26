#--------- Flask settings
SERVER_HOST = 'https://nd2hospitalapp.azurewebsites.net' # Update this for the appropriate front-end website when up
# SERVER_HOST ='0.0.0.0'
SERVER_PORT = 5000
FLASK_DEBUG = True # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants

# API_URL format: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net"
#API_URL = " https://neighborlyapi.azurewebsites.net/api/"

# for local host if Azure functions served locally
# API_URL = "http://localhost:7071/api"# Inside file settings.py

# ------- For production -------
# where APP_NAME is your Azure Function App name 

API_URL = "https://nd2hospitalfunc.azurewebsites.net/api/"
