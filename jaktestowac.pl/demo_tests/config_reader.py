import os

def load():
    config_path = os.path.join('config','configuration.txt')
    with open(config_path, 'r') as file:
        config = file.readlines()
        return config