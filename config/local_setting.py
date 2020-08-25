# -*- coding: utf-8 -*-
# 本地开发环境配置文件
from config.base_setting import *

# SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/movie_cat"
SQLALCHEMY_TRACK_MODIFICATIONS = False


SECRET_KEY = "local"

DOMAIN = {
    "www": "http://127.0.0.1:5000"
}

# RELEASE_PATH = "/home/www/release_version"
