"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see:
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# ✅ Standard ASGI application
application = get_asgi_application()

# ✅ Placeholder for future WebSockets/Channels support
# from channels.routing import ProtocolTypeRouter
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     # "websocket": AuthMiddlewareStack(URLRouter(your_routes_here))
# })


