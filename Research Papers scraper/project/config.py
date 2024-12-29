import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change-in-production'
    SERPAPI_KEY = "70bcd518723ea82d25362079dcb2da0a6b76fec65e9660a05f2848180581bb7a"