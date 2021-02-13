class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "05Fnq8U6DXrMFvbH9jLdj)"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "pelpro"
    DB_USER = "pelprousr"
    DB_PASS = "pelpropass"
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@db/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
