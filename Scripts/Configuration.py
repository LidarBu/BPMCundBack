import json
import os


class Configuration:

    def __init__(self):
        dir_name = os.path.dirname(__file__)
        path = os.path.join(dir_name, "../config/settings.json")

        with open(path, "r") as file:
            self.conf = json.load(file)
