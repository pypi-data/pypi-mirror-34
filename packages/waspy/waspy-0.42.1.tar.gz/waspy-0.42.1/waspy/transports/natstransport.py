"""
This is a very slimmed down, alpha implementation of nats as the message bus
you will need to install: https://github.com/nats-io/asyncio-nats
(pip install asyncio-nats-client)
for this to work
"""
import asyncio

from nats.aio.client import Client as NATSClient
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

from .transportabc import TransportABC


class NatsTransport(TransportABC):
    def __init__(self):
        self.nc = NATSClient()
        self._handler = None
        self._done_future = asyncio.Future()

    def get_client(self):
        pass

    async def start(self, request_handler: callable):
        self._handler = request_handler

        await self.nc.subscribe('test', cb=self.handle_request)
        try:
            await self._done_future
        except asyncio.CancelledError:
            pass

    def listen(self, *, loop, config):
        pass

    def shutdown(self):
        pass

    async def close(self):
        pass

    async def handle_request(self):
        pass
