"""
ASGI config for base_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from chat import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base_app.settings")

# Handles routing protocols for Django Channels
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        # Point root routing to chat/routing.py
        "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
    }
)
