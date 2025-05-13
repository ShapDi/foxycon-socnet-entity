from socnet_entity.storage import EntitySocNetStorage


class EntitySocNetController:
    def __init__(self, storage: str|None = None):
        self.virtual_storage = []
        self.storage = EntitySocNetStorage(storage) if storage is not None else None

