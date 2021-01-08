import os

from src.app import init_app


if __name__ == '__main__':
    ##retrieve the environment variable from the terminal 
    env_name = os.getenv('FLASK_ENV')

    app =init_app(env_name)

    ## run the app 
    app.run()