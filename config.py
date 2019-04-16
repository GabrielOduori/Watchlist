import os

class Config:
    '''
    General configurations parent class
    '''
    BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    
class ProdConfig(Config):
    '''
    General configuration child class
    
    Args:
        Config: The parent configuration class with Genral 
        configuration settings
    '''
    pass
  
    
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with gerenal 
        configuration settings
    '''
    
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
    
    
    