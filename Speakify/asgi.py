"""
ASGI config for Speakify project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from Home import routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Speakify.settings")
django_asgi_app = get_asgi_application()
 
application = ProtocolTypeRouter(
    {
        "http" : get_asgi_application() ,
        "websocket" : AuthMiddlewareStack(
            URLRouter(
                routing.ws_urlpatterns
            )   
        )
    }
)

