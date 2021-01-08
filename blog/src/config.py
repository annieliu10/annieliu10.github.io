import os 


##environment configuration


##development environment config 
class Development:
    

    DEBUG= True
    TESTING= False

    ## getting the environment var from the operating system 
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


##production environment config 
class Production:
   
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

app_config = {
    'development': Development(),
    'production': Production(),
}