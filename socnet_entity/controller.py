import uuid

from socnet_entity.balancers import EntitySocNetBalancer
from socnet_entity.entitys import EntitySocNet
from socnet_entity.storage import EntitySocNetStorage


class EntitySocNetController:
    def __init__(self, storage_path: str | None = None):
        self.virtual_storage = {}
        self.storage_path = (
            EntitySocNetStorage(storage_path) if storage_path is not None else None
        )
        self.entity_balancer = EntitySocNetBalancer()

        if storage_path is not None:
            self.storage = EntitySocNetStorage(storage_path)
            self.virtual_storage = self.storage.init_storage()

    def add_entity(self, entity: EntitySocNet):
        pass

    def delete_entity(self, entity: EntitySocNet):
        pass

    def get_entity(
        self, entity_id: uuid.UUID | None = None, entity_name: str | None = None
    ):
        pass

