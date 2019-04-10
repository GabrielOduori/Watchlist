class Config:
    '''
    General configurations parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    
    
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
    
    
    