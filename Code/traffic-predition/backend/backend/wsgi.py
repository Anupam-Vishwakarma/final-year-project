"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information, see:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# ✅ Ensure project root is in `sys.path` (for better module resolution)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ✅ Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
