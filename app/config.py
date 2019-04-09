class Config:
    '''
    General configurations parent class
    '''
    pass
    
    
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
    