import os

class Config(object):
    BOT_TOKEN = os.environ.get("7460486995:AAEuH7MFdOHyPmmCy0izmDsXhDN1JzCP4Ow")
    API_ID = int(os.environ.get("20369373"))
    API_HASH = os.environ.get("0d53cc7f978163fed3263be5cbb20ab0")
    VIP_USER = os.environ.get('VIP_USERS', '7170328188').split(',')
    VIP_USERS = [int() for user_id in VIP_USER]

