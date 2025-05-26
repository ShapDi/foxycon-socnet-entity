import uuid
from abc import ABC
from dataclasses import dataclass


@dataclass
class EntitySocNet(ABC):
    id: uuid.UUID = uuid.uuid4()
    _subscribers: list | None = None
    _num_requests: int | None = None
    _num_usage_skips: int | None = None
    _status_block: bool | None = None

    @property
    def subscribers(self):
        return self._subscribers

    @subscribers.setter
    def subscribers(self, value):
        self.ping_change()
        self._subscribers = value

    @property
    def num_requests(self):
        return self._num_requests

    @num_requests.setter
    def num_requests(self, value):
        self.ping_change()
        self._num_requests = value

    @property
    def num_usage_skips(self):
        return self._num_usage_skips

    @num_usage_skips.setter
    def num_usage_skips(self, value):
        self.ping_change()
        self._num_usage_skips = value

    @property
    def status_block(self):
        return self._status_block

    @status_block.setter
    def status_block(self, value):
        self.ping_change()
        self._status_block = value

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
    _proxy_str: str = None

    @property
    def proxy_str(self):
        return self._proxy_str

    @proxy_str.setter
    def proxy_str(self, value):
        self.ping_change()
        self._proxy_str = value


@dataclass
class InstagramAccount(EntitySocNet):
    _login: str | None = None
    _password: str | None = None
    _session_id: str | None = None
    _token: str | None = None
    _initialization_status: bool | None = None

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self.ping_change()
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self.ping_change()
        self._password = value

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self.ping_change()
        self._session_id = value

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self.ping_change()
        self._token = value

    @property
    def initialization_status(self):
        return self._initialization_status

    @initialization_status.setter
    def initialization_status(self, value):
        self.ping_change()
        self._initialization_status = value

    def __str__(self):
        return "instagram_account"


@dataclass
class TelegramAccount(EntitySocNet):
    _api_id: int = None
    _api_hash: str = None
    _token_session: str | None = None
    _initialization_status: bool | None = None

    @property
    def api_id(self):
        return self._api_id

    @api_id.setter
    def api_id(self, value):
        self.ping_change()
        self._api_id = value

    @property
    def api_hash(self):
        return self._api_hash

    @api_hash.setter
    def api_hash(self, value):
        self.ping_change()
        self._api_hash = value

    @property
    def token_session(self):
        return self._token_session

    @token_session.setter
    def token_session(self, value):
        self.ping_change()
        self._token_session = value

    @property
    def initialization_status(self):
        return self._initialization_status

    @initialization_status.setter
    def initialization_status(self, value):
        self.ping_change()
        self._initialization_status = value

    def __str__(self):
        return "telegram_account"
