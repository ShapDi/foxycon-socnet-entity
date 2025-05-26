import json
import os


class EntitySocNetStorage:
    def __init__(self, storage_path: str):
        self.storage_path = storage_path

    def init_storage(self):
        if not os.path.exists(self.storage_path):
            return {}
        try:
            with open(self.storage_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}


