import random
from abc import ABC, abstractmethod


# from foxycon.data_structures.utils_type import TelegramAccount, Proxy

from socnet_entity.entitys import Proxy, InstagramAccount, TelegramAccount, EntitySocNet

class EntitySocNetBalancer(ABC):

    @abstractmethod
    def call_next(self):
        pass


class ProxyBalancer(EntitySocNetBalancer):
    def __init__(self, balancing_objects: list[Proxy]):
        super().__init__()
        self._balancing_objects = []

        for balancing_object in balancing_objects:
            if balancing_object.num_requests is None:
                balancing_object.num_requests = self.get_number_requests()
            self._balancing_objects = balancing_object

    @staticmethod
    def get_number_requests():
        return random.randrange(2, 4, 1)

    def call_next(self):
        pass

class InstagramBalancer(EntitySocNetBalancer):
    def __init__(self, balancing_objects: list[InstagramAccount]):
        self._balancing_objects = []

        for balancing_object in balancing_objects:
            if balancing_object.num_requests is None:
                balancing_object.num_requests = self.get_number_requests()
            self._balancing_objects = balancing_object

    @staticmethod
    def get_number_requests():
        return random.randrange(2, 4, 1)

    def call_next(self):
        pass

class TelegramBalancer(EntitySocNetBalancer):
    def __init__(self, balancing_objects: list[TelegramAccount]):
        self._balancing_objects = []

        for balancing_object in balancing_objects:
            if balancing_object.num_requests is None:
                balancing_object.num_requests = self.get_number_requests()
            self._balancing_objects = balancing_object

    @staticmethod
    def get_number_requests():
        return random.randrange(2, 4, 1)

    def call_next(self):
        pass