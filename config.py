class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "05Fnq8U6DXrMFvbH9jLdj)"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "flasktest"
    DB_USER = "flasktest"
    DB_PASS = "flasktest"
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True