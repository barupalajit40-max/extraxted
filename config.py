#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8477291329:AAFwhbRy93L7L7LoPHRqH5R_s6TAwUaj1eA")
    API_ID = int(os.environ.get("API_ID", "34156893"))
    API_HASH = os.environ.get("API_HASH", "f40061f9c273fed4a35bc061a2725e9d")
    AUTH_USERS = "8477291329"


