import os

os.environ.setdefault("DJANGO_SECRET_KEY", 'not-a-secret')
os.environ.setdefault('DATABASE_URL', "postgresql://postgres:@localhost:5432/snaas")

from snaas.settings import *
