import uuid
from abc import ABC
from dataclasses import dataclass


from abc import ABC
from dataclasses import dataclass, field

@dataclass
class EntitySocNet(ABC):
    id: uuid.UUID = uuid.uuid4()
    subscribers: list | None = None
    _num_requests: int | None = None
    num_usage_skips: int | None = None
    status_block: bool | None = None

    @property


    @property
    def num_requests(self):
        return self._num_requests

    @num_requests.setter
    def num_requests(self, value):
        self.ping_change()
        self._num_requests = value


    def add_subscriber(self, subscriber):
        if self.subscribers is None:
            self.subscribers = []
        self.subscribers.append(subscriber)

    def ping_change(self):
        if self.subscribers:
            for subscriber in self.subscribers:
                pass

@dataclass
class Proxy(EntitySocNet):
    proxy_str: str = None # ✅ Обязательное поле идёт первым

@dataclass
class InstagramAccount(EntitySocNet):
    login: str| None = None
    password: str| None = None
    session_id: str | None = None
    token: str | None = None
    initialization_status: bool | None = None




    def __str__(self):
        return 'instagram_account'



@dataclass
class TelegramAccount(EntitySocNet):
    api_id: int = None
    api_hash: str = None
    token_session: str | None = None
    initialization_status: bool | None = None

    def __str__(self):
        return 'telegram_account'