import json
import os


def load():
    config_path = os.path.join('config', 'configuration.json')
    with open(config_path, 'r') as file:
        config = file.read()
    return json.loads(config)
