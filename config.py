#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

# dialect+dirver://username:passwordj@host:port/database?charset=utf8
DIALECT = 'mysql'
DIRVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zhiliao_demo'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DIRVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
