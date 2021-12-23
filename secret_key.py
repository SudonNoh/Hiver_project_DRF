import os
import json
from django.core.exceptions import ImproperlyConfigured

def secret_key(BASE_DIR):
    secret_file = os.path.join(BASE_DIR, 'secrets.json')

    with open(secret_file) as f:
        secrets = json.loads(f.read())
        
    def get_secret(setting, secrets=secrets):
        try:
            return secrets[setting]
        except KeyError:
            error_msg = "Set the {0} enviroment variable".format(setting)
            raise ImproperlyConfigured(error_msg)
        
    SECRET_KEY = get_secret("SECRET_KEY")
    
    return SECRET_KEY