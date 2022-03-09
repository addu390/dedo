from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from core import consumers
from tuktuk import middleware


application = ProtocolTypeRouter(
    {
        "websocket": middleware.TokenAuthMiddlewareStack(URLRouter([
            path('taxi/', consumers.DriverConsumer),
        ]))
    }
)
