import logging
import typing

log = logging.getLogger('aiogram.Middleware')


class MiddlewareManager:
    """
    Middlewares manager. Works only with dispatcher.
    """

    def __init__(self, dispatcher):
        """
        Init

        :param dispatcher: instance of Dispatcher
        """
        self.dispatcher = dispatcher
        self.loop = dispatcher.loop
        self.bot = dispatcher.bot
        self.storage = dispatcher.storage
        self.applications = []

    def setup(self, middleware):
        """
        Setup middleware

        :param middleware:
        :return:
        """
        if not isinstance(middleware, BaseMiddleware):
            raise TypeError(f"`middleware` must be an instance of BaseMiddleware, not {type(middleware)}")
        if middleware.is_configured():
            raise ValueError('That middleware is already used!')

        self.applications.append(middleware)
        middleware.setup(self)
        log.debug(f"Loaded middleware '{middleware.__class__.__name__}'")
        return middleware

    async def trigger(self, action: str, args: typing.Iterable):
        """
        Call action to middlewares with args lilt.

        :param action:
        :param args:
        :return:
        """
        for app in self.applications:
            await app.trigger(action, args)


class BaseMiddleware:
    """
    Base class for middleware.

    All methods on the middle always must be coroutines and name starts with "on_" like "on_process_message".
    """

    def __init__(self):
        self._configured = False
        self._manager = None

    @property
    def manager(self) -> MiddlewareManager:
        """
        Instance of MiddlewareManager
        """
        if self._manager is None:
            raise RuntimeError('Middleware is not configured!')
        return self._manager

    def setup(self, manager):
        """
        Mark middleware as configured

        :param manager:
        :return:
        """
        self._manager = manager
        self._configured = True

    def is_configured(self) -> bool:
        """
        Check middleware is configured

        :return:
        """
        return self._configured

    async def trigger(self, action, args):
        """
        Trigger action.

        :param action:
        :param args:
        :return:
        """
        handler_name = f"on_{action}"
        handler = getattr(self, handler_name, None)
        if not handler:
            return None
        await handler(*args)
