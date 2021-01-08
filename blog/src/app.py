from flask import Flask

##import the app_config dict from the config module
from .config import app_config

def init_app(env_name):

    ## initialize the flask app
    app = Flask(__name__)
    
    ##object being the app_config 
    app.config.from_object(app_config[env_name])


    @app.route('/', methods=['GET'])
    def helloWorld():
        return 'Hello World!'
    
    return app