import  os
class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY="5285bfd9-e3f0-45d9-af37-a5c3407e9b59"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rustique:uwimpaye12@localhost/pitch'
    
    #markdown configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    '''
    mail configurations
    '''

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'rustique'
    MAIL_PASSWORD = 'uwimpaye12'

class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rustique:uwimpaye12@localhost/pitch'
class DevConfig(Config):
    
    DEBUG=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_options={
'development':DevConfig,
"production":ProdConfig,
'test':TestConfig
}
