import time
import uuid
from abc import ABC
from dataclasses import dataclass, field
from socnet_entity.storage import Storage
from socnet_entity.utils.types import Status, CastableMixin, EntityListenerMixin
from socnet_entity.utils.validators import validate_proxy, validate_count, validate_telegram_api_id, \
    validate_telegram_api_hash, validate_telegram_session_token, validate_instagram_session_id, validate_instagram_csrf


@dataclass
class Entity(ABC, CastableMixin):
    id: uuid.UUID = uuid.uuid4()
    _subscribers: list[EntityListenerMixin] | None = None
    _uses: int = 0
    _fails: int = 0
    _status: Status = Status.WORKING
    _in_use: bool = False
    _last_used: float = field(default_factory=time.time)

    @property
    def subscribers(self):
        return self._subscribers

    @subscribers.setter
    def subscribers(self, value: list[EntityListenerMixin]):
        self._subscribers = value
        self.ping_change()

    @property
    def uses(self):
        return self._uses

    @uses.setter
    def uses(self, value: int):
        validate_count(value, 'Number of uses')
        self._uses = value
        self.ping_change()

    @property
    def fails(self):
        return self._fails

    @fails.setter
    def fails(self, value: int):
        validate_count(value, 'Number of fails')
        self._fails = value
        self.ping_change()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: Status):
        self._status = value
        self.ping_change()

    @property
    def in_use(self):
        return self._in_use

    @in_use.setter
    def in_use(self, value: bool):
        self._in_use = value
        self.ping_change()

    @property
    def last_used(self):
        return self._last_used

    @last_used.setter
    def last_used(self, value):
        self._last_used = value
        self.ping_change()

    def add_subscriber(self, subscriber):
        if self.subscribers is None:
            self.subscribers = []
        self.subscribers.append(subscriber)

    def ping_change(self):
        if self.subscribers:
            for subscriber in self.subscribers:
                subscriber.notify()


@Storage.register_type
@dataclass
class Proxy(Entity):
    _proxy_str: str = None

    @property
    def proxy_str(self):
        return self._proxy_str

    @proxy_str.setter
    def proxy_str(self, value: str):
        validate_proxy(value)
        self._proxy_str = value
        self.ping_change()

@Storage.register_type
@dataclass
class InstagramAccount(Entity):
    _login: str | None = None
    _password: str | None = None
    _session_id: str | None = None
    _token: str | None = None
    _is_initialized: bool | None = None

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value
        self.ping_change()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
        self.ping_change()

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value: str):
        validate_instagram_session_id(value)
        self._session_id = value
        self.ping_change()

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value: str):
        validate_instagram_csrf(value)
        self._token = value
        self.ping_change()

    @property
    def is_initialized(self):
        return self._is_initialized

    @is_initialized.setter
    def is_initialized(self, value):
        self._is_initialized = value
        self.ping_change()

    def __str__(self):
        return "instagram_account"

@Storage.register_type
@dataclass
class TelegramAccount(Entity):
    _api_id: int = None
    _api_hash: str = None
    _token_session: str | None = None
    _is_initialized: bool | None = None

    @property
    def api_id(self):
        return self._api_id

    @api_id.setter
    def api_id(self, value: int):
        validate_telegram_api_id(value)
        self._api_id = value
        self.ping_change()

    @property
    def api_hash(self):
        return self._api_hash

    @api_hash.setter
    def api_hash(self, value: str):
        validate_telegram_api_hash(value)
        self._api_hash = value
        self.ping_change()

    @property
    def token_session(self):
        return self._token_session

    @token_session.setter
    def token_session(self, value: str):
        validate_telegram_session_token(value)
        self._token_session = value
        self.ping_change()

    @property
    def is_initialized(self):
        return self._is_initialized

    @is_initialized.setter
    def is_initialized(self, value):
        self._is_initialized = value
        self.ping_change()

    def __str__(self):
        return "telegram_account"
