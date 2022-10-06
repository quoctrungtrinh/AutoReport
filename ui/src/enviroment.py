import os

class Enviroment:
    SERVER_IP = os.environ.get('BACKEND_IP', '192.168.221.128')
    SERVER_PORT = os.environ.get('BACKEND_PORT', '8080')
    SERVER_URL = f'http://{SERVER_IP}:{SERVER_PORT}'
    PROXIES =   {
                    "http": 'de.coia.siemens.net',
                    "https": 'de.coia.siemens.net',
                    "no_proxy": SERVER_IP
                }