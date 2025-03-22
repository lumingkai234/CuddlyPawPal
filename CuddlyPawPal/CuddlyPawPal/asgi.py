"""
ASGI config for CuddlyPawPal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from api.consumers import ChipConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CuddlyPawPal.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP 协议
    "websocket": AuthMiddlewareStack(  # WebSocket 协议
        URLRouter([
            path('ws/chip/', ChipConsumer.as_asgi()),  # WebSocket 路由
        ])
    ),
})